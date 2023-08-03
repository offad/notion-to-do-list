import sys
import os
import re
import ast
from PIL import Image, ImageFont, ImageDraw

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

SPACING = 48
WHITE = (255, 255, 255)
LIST_WIDTH = 560

def main(data):
    # Step 2. Edit the template Wallpaper
    image = Image.open(os.path.join(__location__, "assets/template.jpg"))
    draw = ImageDraw.Draw(image)
    mf = ImageFont.truetype('assets/font.ttf', 40)
    mf2 = ImageFont.truetype('assets/font.ttf', 32)

    # Properties
    width = image.width
    height = image.height - 80

    def calc(index):
        yPos = index * SPACING
        q, mod = divmod(yPos, height)
        if (q > 0):
            yPos -= height
            yPos += SPACING

        # Move 300 pixels away from the edge
        xPos = width - (LIST_WIDTH * (q + 1)) - 300
        return (xPos, yPos)

    def create(key, tasks, index):
        xPos, yPos = calc(index)
        # Header
        draw.text((xPos, yPos), key, fill=WHITE, font=mf)

        # Line
        linePos = yPos + SPACING / 2 + 8
        draw.line([(xPos, linePos), (xPos + LIST_WIDTH - 24, linePos)], fill=WHITE)

        # Tasks
        for i, task in enumerate(tasks):
            xPos, yPos = calc(index + (i + 1))
            draw.text((xPos, yPos), task, fill=WHITE, font=mf2)

        return index + len(tasks) + 1

    # Add Text to an image
    index = 0
    for key in data:
        tasks = data.get(key)
        index = create(key, tasks, index + 1)

    # Display edited image on which we have added the text
    #image.show()

    # Step 3. Update Sticky Notes Wallpaper
    image.save("wallpaper.jpg")

if __name__ == "__main__":
    input = sys.argv[-1] if len(sys.argv) > 1 else "{}"
    match = input[input.find('{'):].strip()
    data = ast.literal_eval(match)
    main(data)

