# nano-banana-claude-code

A branding illustration workspace using Claude Code playground plugin.

## Quick Start

**Open the Illustration Prompt Builder:**
```
playgrounds/illustration-prompt-builder.html
```
Open this file in your browser to start creating consistent AI image prompts for your branding.

---

## What This Project Does

This workspace helps you create consistent branding illustrations by:
1. **Crafting prompts** for AI image generators (DALL-E, Midjourney, etc.)
2. **Maintaining style consistency** across all generated illustrations
3. **Documenting your visual identity** for reference

## Project Structure

```
nano-banana-claude-code/
├── .claude/
│   └── settings.json              # Claude Code configuration
├── branding/
│   ├── reference-images/          # Store your base/reference images
│   ├── generated/                 # Save generated illustrations
│   └── style-guide/
│       └── STYLE_GUIDE.md         # Complete style documentation
├── playgrounds/
│   └── illustration-prompt-builder.html  # Interactive prompt builder
└── README.md
```

## Your Style Guide

Based on your reference illustration, your brand style includes:

| Element | Specification |
|---------|---------------|
| **Art Style** | Flat vector illustration |
| **Outlines** | Bold, dark brown/black |
| **Colors** | Coral (#E8A0A0), Teal (#5B9A9A), Cream (#F5F0EB), Tan (#C4A574) |
| **Composition** | Circular pink backdrop, geometric accents |
| **Aesthetic** | Modern, professional, approachable |

See `branding/style-guide/STYLE_GUIDE.md` for complete documentation.

## How to Use

### 1. Use the Prompt Builder
Open `playgrounds/illustration-prompt-builder.html` in your browser:
- Select a preset (Portrait, Scene, Icon, Social, Marketing)
- Customize subject, action, colors, and style elements
- Click "Generate Prompt" and copy to your AI image tool

### 2. Example Prompts

**Portrait illustration:**
```
A woman with curly dark hair, confident smile, flat vector illustration,
bold dark outlines, limited palette (coral pink, teal, cream),
clean crisp edges, cream background with pink circular frame,
modern professional aesthetic
```

**Icon/Element:**
```
Hexagonal icons representing data and creativity, flat vector style,
teal and coral accents, bold outlines, geometric shapes,
professional branding illustration
```

### 3. Store Your Work
- Put reference images in `branding/reference-images/`
- Save generated images in `branding/generated/`
- Update the style guide as your brand evolves

## Available Claude Code Playgrounds

You can also ask Claude to create additional playgrounds:

| Template | Use Case |
|----------|----------|
| **design-playground** | Explore layouts, colors, typography |
| **concept-map** | Map out brand concepts and ideas |
| **document-critique** | Review brand guidelines |

## Configuration

The playground plugin is configured in `.claude/settings.json`.
