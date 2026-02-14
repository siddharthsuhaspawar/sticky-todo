# 📝 Sticky ToDo

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/sticky-todo)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#)

A minimal, elegant todo application with beautiful typography and intuitive design. Built with modern web technologies and packaged as a native desktop application.

![Sticky ToDo Screenshot](screenshot.png)

## ✨ Features

- **Beautiful Typography** - Elegant *Playfair Display* italic font for the brand with graceful styling
- **Dark & Light Themes** - Toggle between gorgeous dark and light modes
- **Drag & Drop** - Reorder tasks intuitively with smooth animations
- **Persistent Storage** - Tasks and preferences are saved automatically
- **Keyboard Shortcuts** - Press `/` to focus input, `Esc` to clear
- **Clean UI** - Minimalist design with subtle animations and premium feel
- **Cross-Platform** - Runs on Windows, macOS, and Linux

## 🚀 Quick Start

### Web Version
Simply open `todo.html` in any modern web browser.

### Desktop App

#### Windows (Recommended)
1. Download the latest release from [Releases](../../releases)
2. Run `StickyToDo.exe`
3. No installation required!

#### From Source
```bash
# Clone the repository
git clone https://github.com/yourusername/sticky-todo.git
cd sticky-todo

# Install dependencies
pip install -r requirements.txt

# Run the application
python todo.py
```

## 🛠️ Building from Source

### Prerequisites
- Python 3.8 or higher
- pip

### Windows Executable
```bash
# Install build dependencies
pip install pyinstaller

# Build the executable
python build.py

# Or create a single-file executable
python build.py --onefile

# Create an installer
python build.py --installer
```

The executable will be created in the `dist/` directory.

## 📁 Project Structure

```
sticky-todo/
├── todo.html          # Main UI (HTML/CSS/JS)
├── todo.py            # Desktop application wrapper
├── build.py           # Build script for Windows executable
├── requirements.txt   # Python dependencies
├── README.md          # This file
├── LICENSE            # MIT License
└── screenshot.png     # App screenshot
```

## 🎨 Design Philosophy

Sticky ToDo embraces **less is more**:

- **Typography**: *Playfair Display* for elegant branding, *Inter* for clean readability
- **Colors**: Carefully crafted dark/light palettes with proper contrast
- **Motion**: Subtle animations that feel responsive and delightful
- **Focus**: No unnecessary features - just a simple, beautiful todo list

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `/` | Focus the input field |
| `Enter` | Add task (when input is focused) |
| `Esc` | Clear input and unfocus |
| `Space/Enter` | Toggle task completion (when checkbox is focused) |

## 🧪 Development

### Running in Debug Mode
```bash
python todo.py --debug
```

### Custom Data Directory
```bash
python todo.py --data-dir /path/to/data
```

### Project Architecture

```
┌─────────────────┐
│   WebView UI    │  ← todo.html (HTML/CSS/JS)
│  (Edge/WebKit)  │
└────────┬────────┘
         │ JS API
         ▼
┌─────────────────┐
│   Python API    │  ← todo.py (TodoAPI class)
│    (Bridge)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   TaskStore     │  ← JSON persistence
│  (Data Layer)   │
└─────────────────┘
```

## 📦 Data Storage

- **Windows**: `%APPDATA%\StickyTodo\`
- **macOS**: `~/.sticky-todo/`
- **Linux**: `~/.sticky-todo/`

Files:
- `tasks.json` - Your todo items
- `settings.json` - App preferences
- `tasks.backup.json` - Automatic backup

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [pywebview](https://github.com/r0x0r/pywebview) - For the desktop app wrapper
- [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) - Beautiful serif typeface
- [Inter](https://rsms.me/inter/) - Clean sans-serif font

---

<p align="center">
  Made with ❤️ for beautiful productivity
</p>
