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

---

# 🤖 AI Agent Integration Guide

Sticky ToDo is designed to be AI-agent friendly with multiple integration points.

## Quick Start for AI Agents

```javascript
// The app exposes a global API
TodoAgentAPI.help()  // Show all available commands

// Common operations
TodoAgentAPI.addTask("Buy groceries", "high")
TodoAgentAPI.getPendingTasks()
TodoAgentAPI.toggleTask(0)  // Complete first task
TodoAgentAPI.search("meeting")
```

## Global API Reference

### Task Management

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `getTasks()` | none | Array | All tasks with full details |
| `getPendingTasks()` | none | Array | Incomplete tasks only |
| `getCompletedTasks()` | none | Array | Completed tasks only |
| `addTask(text, priority)` | string, string (high/medium/low) | Object | Add new task |
| `toggleTask(index)` | number | Object | Toggle completion status |
| `deleteTask(index)` | number | Object | Delete task by index |
| `clearCompleted()` | none | Object | Remove all completed tasks |

### Search & Filter

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `search(query)` | string | Object | Search tasks by text |
| `clearSearch()` | none | Object | Clear search results |
| `setFilter(filter)` | string (all/active/completed) | Object | Set task filter |

### Data & Settings

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `export()` | none | Object | Export all data as JSON |
| `import(data)` | Object | Object | Import data from JSON |
| `toggleTheme()` | none | Object | Switch dark/light mode |
| `getStats()` | none | Object | Get task statistics |

### Natural Language

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `command(text)` | string | Object | Process natural language command |

## Natural Language Commands

AI agents (and humans) can use natural language via `AICommandProcessor.process()`:

```javascript
// Adding tasks
AICommandProcessor.process("add buy groceries")
AICommandProcessor.process("add high priority call mom")
AICommandProcessor.process("create a low priority task to read book")

// Completing tasks
AICommandProcessor.process("complete task 1")
AICommandProcessor.process("finish first task")
AICommandProcessor.process("check off last task")

// Managing tasks
AICommandProcessor.process("delete task 2")
AICommandProcessor.process("remove last task")

// Searching and filtering
AICommandProcessor.process("search meeting")
AICommandProcessor.process("find urgent")
AICommandProcessor.process("show completed")
AICommandProcessor.process("list active tasks")

// Stats and info
AICommandProcessor.process("stats")
AICommandProcessor.process("how many tasks")
AICommandProcessor.process("progress")

// Clear completed
AICommandProcessor.process("clear completed")
AICommandProcessor.process("clear all completed tasks")

// Help
AICommandProcessor.process("help")
AICommandProcessor.process("what can you do")
```

## Data Schema

### Task Object
```javascript
{
  id: string,           // Unique identifier
  text: string,         // Task description
  done: boolean,        // Completion status
  priority: string,     // "high" | "medium" | "low"
  pinned: boolean,      // Pinned to top
  createdAt: string     // ISO 8601 timestamp
}
```

### Stats Object
```javascript
{
  total: number,        // Total tasks
  completed: number,    // Completed tasks
  pending: number,      // Pending tasks
  highPriority: number, // High priority pending tasks
  completionRate: number // Percentage (0-100)
}
```

## Browser Console Access

When the app loads, it logs helpful information:

```
🤖 Sticky ToDo - AI Agent API Ready
Type TodoAgentAPI.help() to see available commands
Or click the 🤖 button to open AI Mode UI
```

## AI Mode UI (Human-Friendly)

The app includes a built-in AI assistant panel that humans can use:

1. Click the 🤖 button (bottom-right corner)
2. Type natural language commands
3. Click suggestion chips for quick actions
4. View API reference for programmatic access

## Structured Data (Schema.org)

The app includes JSON-LD structured data for web crawlers:

```json
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Sticky ToDo",
  "applicationCategory": "ProductivityApplication",
  "featureList": [
    "Task management with priorities",
    "Dark and light themes",
    "AI agent API access"
  ]
}
```

## Example Integration Scenarios

### Daily Standup Report
```javascript
const pending = TodoAgentAPI.getPendingTasks();
const stats = TodoAgentAPI.getStats();
console.log(`Today: ${stats.pending} tasks pending, ${stats.highPriority} high priority`);
```

### Batch Task Creation
```javascript
const tasks = ["Email team", "Review PRs", "Update docs"];
tasks.forEach(t => TodoAgentAPI.addTask(t, "medium"));
```

### End-of-Day Cleanup
```javascript
TodoAgentAPI.clearCompleted();
TodoAgentAPI.toggleTheme(); // Switch to dark mode
```

### Voice Assistant Integration
```javascript
// Parse voice input and route to command processor
function handleVoiceCommand(transcript) {
  const result = AICommandProcessor.process(transcript);
  speak(result.message || "Done");
}
```

## Tips for AI Agents

1. **Check return values** - All methods return `{success: boolean, ...}`
2. **Index is 0-based** - First task is index 0
3. **Persistence** - Data auto-saves to localStorage
4. **UI updates** - API calls automatically update the UI
5. **Error handling** - Invalid operations return `{success: false, error: "..."}`

## Security Notes

- All data is client-side only (localStorage)
- No server or API keys required
- Safe to eval() in isolated browser context
- No external dependencies for AI features
