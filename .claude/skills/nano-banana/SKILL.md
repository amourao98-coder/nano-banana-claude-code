# Nano Banana Pro - Image Generation Skill

Generate images using Google's Gemini image generation model (Nano Banana Pro).

## When to Use

Activate this skill when the user asks to:
- Generate images, illustrations, or graphics
- Create branding assets, icons, or visual content
- Edit or modify existing images
- Create variations of a reference image

## Prerequisites

Before using, ensure the following are configured:

1. **Gemini API Key**: Set the environment variable `GEMINI_API_KEY`
2. **Gemini CLI**: Install with `npm install -g @anthropic-ai/gemini-cli`

## Image Generation

To generate an image, use the Gemini CLI with the nanobanana extension:

```bash
gemini nanobanana generate "<prompt>" --output ./branding/generated/<filename>.png
```

### Options

| Option | Values | Description |
|--------|--------|-------------|
| `--model` | flash, pro | flash = fast, pro = high quality |
| `--aspect` | 1:1, 16:9, 9:16, 4:3, 3:4 | Image aspect ratio |
| `--size` | 1K, 2K, 4K | Resolution (pro model only) |

### Examples

```bash
# Generate a branding illustration
gemini nanobanana generate "A woman with curly dark hair wearing a leopard print jacket, flat vector illustration style, bold dark outlines, coral pink and teal accents, cream background with pink circular frame, modern professional aesthetic" --model pro --aspect 1:1 --output ./branding/generated/portrait.png

# Generate an icon
gemini nanobanana generate "Hexagonal icon representing data analytics, flat vector style, teal and coral colors, bold outlines" --model flash --aspect 1:1 --output ./branding/generated/icon.png
```

## Image Editing

To edit an existing image with a prompt:

```bash
gemini nanobanana edit "<prompt>" --input ./path/to/image.png --output ./branding/generated/edited.png
```

## Branding Style Reference

When generating images for nano-banana branding, always include these style elements:

- **Art style**: flat vector illustration
- **Outlines**: bold dark outlines
- **Colors**: coral pink (#E8A0A0), teal (#5B9A9A), cream (#F5F0EB), tan (#C4A574)
- **Composition**: clean edges, geometric accents
- **Aesthetic**: modern, professional, approachable

## Output Location

All generated images should be saved to `./branding/generated/` with descriptive filenames.

## Iterative Improvement Workflow

1. **Generate**: Create initial image with prompt
2. **Review**: User reviews the output
3. **Annotate**: Use playground to mark areas for improvement
4. **Refine**: Generate new version with refined prompt
5. **Repeat**: Continue until satisfied
