# Three Lists

A Marc Andreessen-style desk: **To-Do**, **Watch**, and **Later**. Keep the first list tight. Park everything else.

**[Open it](https://siddharthsuhaspawar.github.io/sticky-todo/)** · MIT · no backend

## The three lists

| List | For |
| --- | --- |
| **To-Do** | What you must do. Commitments only. |
| **Watch** | What you are tracking. Follow-ups, references. |
| **Later** | Someday / maybe. Ideas, quotes, clippings. |

To-Do is a task list (sub-trees, Enter to chain, Tab to indent, clear completed). Watch and Later take text, images, and quotes.

## Run it

Browser: open `index.html` (or `todo.html`, they are the same file).

Desktop: Tauri app in `src-tauri/`. Build with `build\build_tauri.cmd` on Windows (needs VS C++ build tools and Rust).

Data stays in `localStorage`. Nothing is sent to a server. Import / export JSON if you want a file backup.

## Repo

```
index.html / todo.html   the app
src-tauri/               desktop shell
screenshots/             older Sticky ToDo shots (the live app is Three Lists)
LICENSE                  MIT
```

The GitHub repo is still named `sticky-todo`. The product is Three Lists.

## License

MIT. See [LICENSE](LICENSE).
