from PIL import Image


class ImageMark:
    def __init__(self, target, mark, num):
        self.num = num
        self.wm = mark
        self.target = target

    def add_mark(self):
        try:
            photo = Image.open(self.target).convert("RGBA")
        except FileNotFoundError:
            return False
        else:
            comp = photo.copy()
            width, height = photo.size

        try:
            new_layer = Image.open(self.wm)
        except FileNotFoundError:
            return False
        else:
            width_l2, height_l2 = new_layer.size

        x = int(width / 2 - width_l2 / 2)
        y = int(height / 2 - height_l2 / 2)
        comp.paste(new_layer, (x, y))
        comp.save(f"watermarked_img_{self.num}.png")

        return True
