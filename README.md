# nano-banana-claude-code

A project configured to use the Claude Code playground plugin.

## Getting Started

This repository is set up to use Claude Code's **playground plugin**, which creates interactive HTML playgrounds for various use cases.

### Available Playground Templates

You can ask Claude to create playgrounds using these templates:

| Template | Use Case |
|----------|----------|
| **design-playground** | Visual design decisions (components, layouts, spacing, colors, typography) |
| **data-explorer** | Data and query building (SQL, APIs, pipelines, regex) |
| **concept-map** | Learning and exploration (concept maps, knowledge gaps, scope mapping) |
| **document-critique** | Document review with approve/reject/comment workflow |
| **diff-review** | Code review for git diffs, commits, PRs with line-by-line commenting |
| **code-map** | Codebase architecture visualization (component relationships, data flow) |

### How to Use

1. Start a Claude Code session in this directory
2. Ask Claude to create a playground, for example:
   - "Create a design playground to explore button styles"
   - "Make a data explorer for testing SQL queries"
   - "Build a concept map for learning React hooks"
   - "Create a code map to visualize the project architecture"

3. Claude will generate a single HTML file with:
   - Live preview that updates instantly
   - Visual controls for experimentation
   - Natural language prompt output with copy button
   - Dark theme with sensible defaults

### Example Prompts

```
"Create a design playground to explore different card component layouts"

"Make a data explorer to help me build and test regex patterns"

"Create a concept map to understand the authentication flow in this project"

"Build a diff-review playground to analyze the recent commits"
```

### Configuration

The playground plugin is configured in `.claude/settings.json`. You can customize permissions and add additional plugins as needed.

## Project Structure

```
nano-banana-claude-code/
├── .claude/
│   └── settings.json    # Claude Code configuration
├── playgrounds/         # Generated playground HTML files (created on demand)
└── README.md
```
