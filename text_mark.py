from PIL import Image, ImageDraw, ImageFont, ImageColor


class TextMark:
    def __init__(self, text, target, colour, alpha, num):
        self.text = text
        self.target = target
        self.col = colour
        self.alpha = alpha
        self.num = num

    def add_mark(self):
        try:
            photo = Image.open(self.target).convert("RGBA")
        except FileNotFoundError:
            return False

        font_size = 1
        font = ImageFont.truetype("Arial", font_size)
        while font.getsize(self.text)[0] < photo.size[0]:
            font_size += 1
            font = ImageFont.truetype("Arial", font_size)

        r, g, b = ImageColor.getrgb(self.col)
        new_layer = Image.new('RGBA', photo.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(new_layer)
        text_width, text_height = draw.textsize(self.text, font)
        width, height = photo.size
        y = height / 2 - text_height / 2
        draw.text((0, y), self.text, fill=(int(r), int(g), int(b), int(self.alpha)), font=font)

        comp = Image.alpha_composite(photo, new_layer)
        comp.save(f"watermarked_img_{self.num}.png")

        return True
