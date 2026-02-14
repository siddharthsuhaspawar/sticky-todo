# Sticky ToDo - Agent Notes

## Project Structure

```
todo/
├── todo.html              # Main UI (HTML/CSS/JS) - Complete app in one file
├── README.md              # User documentation
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
└── AGENTS.md             # This file
```

## Key Features

### Typography
- **Serif italic font** - Elegant branding with beautiful styling
- **System fonts** - Clean sans-serif for UI elements using system font stack
- Gradient underline under "Sticky" for premium feel

### Architecture
- Pure HTML/CSS/JS single-file application
- Works entirely in the browser
- Uses localStorage for data persistence
- Can be installed as PWA

## Development

### Run Locally
Simply open `todo.html` in any browser, or serve with any static server:

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

### Deploy to GitHub Pages
Push changes to the main branch. GitHub Pages serves `todo.html` automatically.

## Data Storage

All data is stored in browser localStorage:
- `sticky-todo-tasks` - Task data
- `sticky-todo-dark` - Theme preference
- `sticky-todo-accent` - Accent color

## Code Style

- HTML: Semantic, accessible markup
- CSS: CSS variables for theming, consistent naming
- JavaScript: ES6+ class-based, clean async patterns
