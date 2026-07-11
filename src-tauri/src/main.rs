// Prevents a console window from opening alongside the app on Windows release builds.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::Manager;

/// Current desktop wallpaper as a data URL. Sources, in order of freshness:
/// CachedFiles (per-monitor current), TranscodedWallpaper, then the registry path.
/// The webview refracts this image behind the glass cards (Liquid Glass).
#[tauri::command]
fn get_wallpaper() -> String {
    use base64::Engine;
    let appdata = match std::env::var("APPDATA") { Ok(v) => v, Err(_) => return String::new() };
    let themes = std::path::Path::new(&appdata).join("Microsoft").join("Windows").join("Themes");
    let mut paths: Vec<std::path::PathBuf> = Vec::new();
    if let Ok(rd) = std::fs::read_dir(themes.join("CachedFiles")) {
        for e in rd.flatten() { paths.push(e.path()); }
    }
    paths.push(themes.join("TranscodedWallpaper"));
    // registry fallback (original file the user picked)
    {
        use std::os::windows::process::CommandExt;
        if let Ok(out) = std::process::Command::new("reg")
            .args(["query", "HKCU\\Control Panel\\Desktop", "/v", "WallPaper"])
            .creation_flags(0x0800_0000) // CREATE_NO_WINDOW
            .output()
        {
            if let Ok(s) = String::from_utf8(out.stdout) {
                if let Some(line) = s.lines().find(|l| l.contains("REG_SZ")) {
                    if let Some(idx) = line.find("REG_SZ") {
                        let p = line[idx + 6..].trim();
                        if !p.is_empty() { paths.push(std::path::PathBuf::from(p)); }
                    }
                }
            }
        }
    }
    for p in paths {
        if let Ok(bytes) = std::fs::read(&p) {
            if bytes.len() > 16 {
                let mime = if bytes.starts_with(&[0x89, 0x50]) { "image/png" } else { "image/jpeg" };
                return format!("data:{};base64,{}", mime, base64::engine::general_purpose::STANDARD.encode(bytes));
            }
        }
    }
    String::new()
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![get_wallpaper])
        .setup(|app| {
            // WebView2's HTTP cache can keep serving stale embedded assets after an
            // update (observed: new exe, old index.html). Purge it before the webview
            // starts — assets are local, so a cold cache costs nothing.
            if let Ok(dir) = app.path().app_local_data_dir() {
                for sub in ["EBWebView/Default/Cache", "EBWebView/Default/Code Cache"] {
                    let _ = std::fs::remove_dir_all(dir.join(sub));
                }
            }
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running Three Lists");
}
