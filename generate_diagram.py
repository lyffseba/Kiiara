"""
Generate architecture diagram for Kiiara.
"""

from PIL import Image, ImageDraw, ImageFont
import os


def create_diagram():
    width, height = 1200, 800
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # Try to load a font
    try:
        font = ImageFont.truetype("arial.ttf", 14)
        font_title = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
        font_title = font

    # Draw title
    draw.text(
        (width // 2 - 200, 30),
        "Kiiara Architecture Diagram",
        fill="black",
        font=font_title,
    )

    # Define boxes (x, y, width, height, label, color)
    boxes = [
        (50, 100, 180, 120, "Frontend\n(React PWA)", "#4CAF50"),
        (50, 300, 180, 80, "Nostr Auth", "#9C27B0"),
        (300, 100, 180, 120, "Backend\n(Python ADK)", "#2196F3"),
        (300, 300, 180, 80, "Financial\nTools", "#FF9800"),
        (300, 450, 180, 80, "Autoresearch\nOptimizer", "#E91E63"),
        (550, 100, 180, 120, "Gemini Live\nAPI", "#F44336"),
        (550, 300, 180, 80, "Google Cloud\n(Firestore, Drive)", "#00BCD4"),
        (800, 100, 180, 120, "User", "#795548"),
        (800, 300, 180, 80, "Nostr\nRelays", "#607D8B"),
    ]

    for x, y, w, h, label, color in boxes:
        draw.rectangle([x, y, x + w, y + h], fill=color, outline="black", width=2)
        draw.text((x + w // 2 - 40, y + h // 2 - 20), label, fill="white", font=font)

    # Draw arrows
    arrows = [
        (230, 160, 300, 160),  # Frontend -> Backend
        (230, 340, 300, 340),  # Nostr Auth -> Financial Tools
        (480, 160, 550, 160),  # Backend -> Gemini
        (480, 340, 550, 340),  # Financial Tools -> Google Cloud
        (480, 490, 550, 340),  # Autoresearch -> Google Cloud
        (730, 160, 800, 160),  # Gemini -> User
        (730, 340, 800, 340),  # Google Cloud -> Nostr Relays
        (230, 380, 300, 490),  # Nostr Auth -> Autoresearch
    ]

    for x1, y1, x2, y2 in arrows:
        draw.line([x1, y1, x2, y2], fill="black", width=2)
        # arrowhead
        draw.polygon([(x2, y2), (x2 - 10, y2 - 5), (x2 - 10, y2 + 5)], fill="black")

    # Legend
    draw.text(
        (50, height - 100),
        "Arrows indicate data flow. All communication is encrypted with Nostr keys.",
        fill="black",
        font=font,
    )

    # Save
    output_path = os.path.join(os.path.dirname(__file__), "architecture.png")
    img.save(output_path, "PNG")
    print(f"Diagram saved to {output_path}")


if __name__ == "__main__":
    create_diagram()
