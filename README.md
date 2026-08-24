# Marc's Three Lists

A Marc Andreessen-style desk: **To-Do**, **Watch**, and **Later**.
Keep the first list tight. Park everything else.

Inspired by Marc Andreessen's [Pmarca Guide to Personal Productivity](https://pmarchive.com/guide_to_personal_productivity.html) (June 2007).

**[Open it](https://siddharthsuhaspawar.github.io/marcs-three-lists/)** · MIT · no backend

## Demo

<p align="center">
  <img src="media/hero.gif" alt="Marc's Three Lists — To-Do, Watch, and Later" width="720">
</p>

## The three lists

| List | For |
| --- | --- |
| **To-Do** | Commitments. What you must do. |
| **Watch** | Follow-ups and references. |
| **Later** | Someday / maybe. |

To-Do supports sub-trees, Enter to chain, Tab to indent, and clear completed. Watch and Later take text, images, and quotes.

## Run it

- **Browser:** open `index.html` (or `todo.html` — same app)
- **Desktop:** Tauri shell in `src-tauri/` — `build/build_tauri.cmd` on Windows (VS C++ + Rust)

Data stays in `localStorage`. Nothing leaves your machine. Import / export JSON for backups.

## License

MIT. See [LICENSE](LICENSE).
