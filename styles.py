# Dictionary containing style modifiers to inject into the user prompt
STYLE_MODIFIERS = {
    "Cyberpunk": "cyberpunk aesthetic, neon lights, futuristic cityscape, highly detailed, synthwave vibe, 8k resolution",
    "Anime": "anime style, vibrant colors, crisp lines, studio ghibli or makoto shinkai aesthetic, detailed background",
    "Cinematic": "cinematic lighting, photorealistic, dramatic shadows, 35mm lens effect, depth of field, masterpiece",
    "Oil Painting": "classical oil painting style, textured canvas, visible rich brush strokes, fine art, museum quality",
    "Pixel Art": "16-bit retro pixel art style, vibrant color palette, crisp pixel grid, video game aesthetic"
}

def apply_style(base_prompt: str, style_name: str) -> str:
    """Modifies the user's base prompt with specific style tokens."""
    modifier = STYLE_MODIFIERS.get(style_name, "")
    if modifier:
        return f"{base_prompt}, {modifier}"
    return base_prompt