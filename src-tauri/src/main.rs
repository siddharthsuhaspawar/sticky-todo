// Prevents a console window from opening alongside the app on Windows release builds.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::Manager;

fn main() {
    tauri::Builder::default()
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
