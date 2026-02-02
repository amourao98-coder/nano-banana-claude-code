#!/usr/bin/env python3
"""Generate images using Google Gemini's image generation model."""

import os
import sys
import base64
from pathlib import Path

# Load environment from .env file
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if "=" in line and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

import google.generativeai as genai

def generate_image(prompt: str, output_path: str) -> str:
    """Generate an image from a text prompt."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set")

    genai.configure(api_key=api_key)

    # Use Imagen 3 for image generation
    model = genai.ImageGenerationModel("imagen-3.0-generate-002")

    result = model.generate_images(
        prompt=prompt,
        number_of_images=1,
        aspect_ratio="1:1",
        safety_filter_level="block_only_high",
    )

    # Save the image
    if result.images:
        image = result.images[0]
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Save image data
        with open(output_file, "wb") as f:
            f.write(image._image_bytes)

        return str(output_file)
    else:
        raise RuntimeError("No image generated")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_image.py '<prompt>' '<output_path>'")
        sys.exit(1)

    prompt = sys.argv[1]
    output_path = sys.argv[2]

    try:
        result = generate_image(prompt, output_path)
        print(f"Image saved to: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
