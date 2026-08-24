# Marc's Three Lists

A Marc Andreessen-style desk: **To-Do**, **Watch**, and **Later**. Keep the first list tight. Park everything else.

<<<<<<< HEAD
Inspired by Marc Andreessen's [Pmarca Guide to Personal Productivity](https://pmarchive.com/guide_to_personal_productivity.html) (June 2007), where he wrote: keep three and only three lists — a Todo List, a Watch List, and a Later List.
=======
Inspired by Marc Andreessen’s [Pmarca Guide to Personal Productivity](https://pmarchive.com/guide_to_personal_productivity.html) (June 2007), where he wrote: keep three and only three lists — a Todo List, a Watch List, and a Later List.
>>>>>>> 628c403 (docs: stack Demo GIFs full-width (one section each))

**[Open it](https://siddharthsuhaspawar.github.io/marcs-three-lists/)** · MIT · no backend

## Demo

<p align="center">
  <img src="media/hero.gif" alt="Marc's Three Lists overview — To-Do, Watch, and Later on the desk" width="720">
</p>

### Add a task

<p align="center">
  <img src="media/add-task.gif" alt="Marc's Three Lists — add a task" width="720">
</p>

### Check one off

<p align="center">
  <img src="media/check-off.gif" alt="Marc's Three Lists — check a task off" width="720">
</p>

### Focus

<p align="center">
  <img src="media/focus.gif" alt="Marc's Three Lists — focus on To-Do" width="720">
</p>

### Themes

<p align="center">
  <img src="media/themes.gif" alt="Marc's Three Lists — cycle themes" width="720">
</p>


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

The GitHub repo is `marcs-three-lists`. The product is **Marc's Three Lists**.

## License

MIT. See [LICENSE](LICENSE).