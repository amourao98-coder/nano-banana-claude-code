# nano-banana-claude-code

Generate and iteratively improve branding illustrations using Claude Code with Nano Banana Pro.

## Prerequisites

Before using, you need:

1. **Gemini API Key** - Get one from [Google AI Studio](https://aistudio.google.com/api-keys)
2. **Set the environment variable**:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

## Quick Start

In Claude Code, ask:

> "Generate a branding illustration of [your subject] in my brand style"

Claude will use the Nano Banana skill to generate images matching your brand style.

## The Workflow

### 1. Generate an Image
Ask Claude to generate an image:
```
"Create a portrait illustration of a person presenting data charts, using my brand style"
```

### 2. Review & Annotate
Ask Claude to create a playground for annotation:
```
"Create a playground to annotate this image so I can mark what to improve"
```

### 3. Iterate
After marking improvements:
```
"Regenerate the image with these changes: [your feedback]"
```

### 4. Repeat
Continue the generate → annotate → improve loop until satisfied.

## Your Brand Style

| Element | Specification |
|---------|---------------|
| **Art Style** | Flat vector illustration |
| **Outlines** | Bold, dark brown/black |
| **Colors** | Coral (#E8A0A0), Teal (#5B9A9A), Cream (#F5F0EB), Tan (#C4A574) |
| **Composition** | Circular pink backdrop, geometric accents |
| **Aesthetic** | Modern, professional, approachable |

See `branding/style-guide/STYLE_GUIDE.md` for complete style documentation.

## Project Structure

```
nano-banana-claude-code/
├── .claude/
│   ├── settings.json                # Claude Code configuration
│   └── skills/
│       └── nano-banana/
│           └── SKILL.md             # Image generation skill
├── branding/
│   ├── reference-images/            # Your base/reference images
│   ├── generated/                   # AI-generated illustrations
│   └── style-guide/
│       └── STYLE_GUIDE.md           # Brand style documentation
├── playgrounds/                     # Generated annotation playgrounds
└── README.md
```

## Example Prompts

**Portrait:**
```
Generate a portrait of a woman with curly hair presenting geometric data visualizations,
flat vector illustration, bold dark outlines, coral and teal accents, cream background
with pink circular frame
```

**Icon:**
```
Create a hexagonal icon representing AI and creativity, flat vector style,
teal and coral colors, bold outlines, professional branding aesthetic
```

**Scene:**
```
Generate a hero illustration showing people collaborating around floating data charts,
flat vector art, limited palette (coral, teal, cream), geometric accent shapes
```

## Plugins & Skills

This project uses:
- **playground** - Create interactive annotation tools for image feedback
- **nano-banana** - Generate images using Gemini's Nano Banana Pro model

## Resources

- [Nano Banana Skill](https://github.com/kkoppenhaver/cc-nano-banana)
- [Claude Code Playground Plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/playground)
