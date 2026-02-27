# 📝 Sticky ToDo

[![Live Demo](https://img.shields.io/badge/🌐-Live%20Demo-blue?style=for-the-badge)](https://siddharthsuhaspawar.github.io/sticky-todo/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/siddharthsuhaspawar/sticky-todo)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**🌐 [Try it now → https://siddharthsuhaspawar.github.io/sticky-todo/](https://siddharthsuhaspawar.github.io/sticky-todo/)**

A minimal, elegant todo application with beautiful typography and intuitive design. Works entirely in your browser — no installation needed!

---

## 📱 Screenshots

<div align="center">

| Dark Mode | Light Mode | Empty State | Customize |
|:---------:|:----------:|:-----------:|:---------:|
| ![Dark Mode](screenshots/dark-mode.png) | ![Light Mode](screenshots/light-mode.png) | ![Empty State](screenshots/empty-state.png) | ![Color Picker](screenshots/color-picker.png) |
| *Beautiful dark theme* | *Clean light theme* | *Celebratory empty state* | *Customize accent colors* |

</div>

---

## ✨ Features

- **Beautiful Typography** - Elegant serif italic font for the brand with graceful styling
- **Dark & Light Themes** - Toggle between gorgeous dark and light modes
- **Subtasks / Checklists** - Break tasks into subtasks displayed as an elegant tree structure with progress tracking
- **Drag & Drop** - Reorder tasks intuitively via dedicated drag handles with smooth animations
- **Priority Levels** - Assign high, medium, or low priority with color-coded indicators
- **Pin Tasks** - Pin important tasks to the top of your list
- **Search** - Quickly filter tasks with `Ctrl+K`
- **Accent Colors** - Customize the app's accent color to your preference
- **Persistent Storage** - Tasks and preferences are saved automatically in your browser
- **Keyboard Shortcuts** - Press `/` to focus input, `Ctrl+K` to search, `Esc` to clear
- **Clean UI** - Minimalist design with subtle animations and premium feel
- **PWA Support** - Install as an app on your device
- **Zero Dependencies** - Single HTML file, no build step, no frameworks

## 🚀 Quick Start

### Web Version (No Installation!)
**👉 [Click here to use Sticky ToDo in your browser](https://siddharthsuhaspawar.github.io/sticky-todo/)**

Or simply open `todo.html` in any modern web browser.

### Install as a Web App (Desktop)

Turn Sticky ToDo into a desktop app that works offline and launches from your taskbar:

#### Microsoft Edge

1. **Open** the [live demo](https://siddharthsuhaspawar.github.io/sticky-todo/) in **Microsoft Edge**

2. **Click the install icon** (⊞) in the address bar  
   *or* press `Ctrl+Shift+A`  
   *or* click **Settings (⋯) → Apps → Install this site as an app**

3. **Click "Install"** in the popup dialog

#### Google Chrome

1. **Open** the [live demo](https://siddharthsuhaspawar.github.io/sticky-todo/) in **Google Chrome**

2. **Click the install icon** (⧉) in the address bar  
   *or* click **⋮ → Cast, save and share → Install page as app**

3. **Click "Install"** in the popup dialog

#### What You Get
Once installed, Sticky ToDo will:
- Appear in your Start Menu / Applications folder
- Have its own taskbar/dock icon
- Work offline
- Launch like a native desktop app
- Open in its own window (no browser chrome)

💡 **Tip:** Right-click the app in your taskbar and select "Pin to taskbar" (Windows) or keep in Dock (Mac) for quick access!

---

### Mobile: Add to Home Screen

**iPhone/iPad (Safari):**
1. Tap the **Share** button (⬆️)
2. Scroll down and tap **"Add to Home Screen"**
3. Tap **"Add"**

**Android (Chrome/Edge):**
1. Tap the **Menu** (⋯)
2. Tap **"Add to Home screen"** or **"Install app"**
3. Tap **"Install"**

## 📁 Project Structure

```
sticky-todo/
├── todo.html          # Main UI (HTML/CSS/JS) - Complete app in one file
├── README.md          # This file
├── LICENSE            # MIT License
├── .gitignore         # Git ignore rules
├── AGENTS.md          # Agent notes
└── screenshots/       # App screenshots
```

## 🎨 Design Philosophy

Sticky ToDo embraces **less is more**:

- **Typography**: Elegant serif for branding, clean sans-serif for readability
- **Colors**: Carefully crafted dark/light palettes with proper contrast
- **Motion**: Subtle animations that feel responsive and delightful
- **Focus**: No unnecessary features - just a simple, beautiful todo list

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `/` | Focus the input field |
| `Ctrl+K` / `Cmd+K` | Open search |
| `Enter` | Add task / save subtask edit |
| `Esc` | Clear input / close search / cancel edit |

## 💾 Data Storage

All data is stored locally in your browser using `localStorage`:
- Tasks (with subtasks, priorities, and pin state) are saved automatically
- Theme preference is remembered
- Accent color choice is preserved
- Data import/export available via the settings panel

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ for beautiful productivity
</p>
