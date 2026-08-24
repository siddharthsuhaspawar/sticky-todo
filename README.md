# Marc's Three Lists

A Marc Andreessen-style desk: **To-Do**, **Watch**, and **Later**. Keep the first list tight. Park everything else.

**[Open it](https://siddharthsuhaspawar.github.io/marcs-three-lists/)** · MIT · no backend

## Demo

<p align="center">
  <img src="media/hero.gif" alt="Marc's Three Lists overview — To-Do, Watch, and Later on the desk" width="720">
</p>

| Add a task | Check one off | Focus | Themes |
| --- | --- | --- | --- |
| <img src="media/add-task.gif" width="220" alt="Marc's Three Lists — add a task"> | <img src="media/check-off.gif" width="220" alt="Marc's Three Lists — check a task off"> | <img src="media/focus.gif" width="220" alt="Marc's Three Lists — focus on To-Do"> | <img src="media/themes.gif" width="220" alt="Marc's Three Lists — cycle themes"> |

## The three lists

| List | For |
| --- | --- |
| **To-Do** | What you must do. Commitments only. |
| **Watch** | What you are tracking. Follow-ups, references. |
| **Later** | Someday / maybe. Ideas, quotes, clippings. |

To-Do is a task list (sub-trees, Enter to chain, Tab to indent, clear completed). Watch and Later take text, images, and quotes.

## Run it

Browser: open `index.html` (or `todo.html`, they are the same file).

Desktop: Tauri app in `src-tauri/`. Build with `build/build_tauri.cmd` on Windows (needs VS C++ build tools and Rust).

Data stays in `localStorage`. Nothing is sent to a server. Import / export JSON if you want a file backup.

## Repo

```
index.html / todo.html   the app
src-tauri/               desktop shell
media/                   demo GIFs
screenshots/             stills
LICENSE                  MIT
```

The GitHub repo is still named `marcs-three-lists`. The product is **Marc's Three Lists**.

## License

MIT. See [LICENSE](LICENSE).
