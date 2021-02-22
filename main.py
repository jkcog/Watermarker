from tkinter import *
from matplotlib.colors import is_color_like
from image_mark import ImageMark
from text_mark import TextMark

image_list = []


def update_img_list():
    img_list_string = ""
    if len(image_list) != 0:
        for img in image_list:
            img_list_string += f"{img}\n"
        image_list_label.config(text=img_list_string)
    else:
        image_list_label.config(text="No Images Currently Selected")


def get_target_img():
    target = target_entry.get()
    image_list.append(target)
    update_img_list()
    notify_label.config(text="")


def remove_img():
    if len(image_list) != 0:
        image_list.pop()
    update_img_list()


def add_watermark_text():
    text = text_entry.get()
    colour = colour_entry.get()

    if not is_color_like(colour):
        notify_label.config(text="Please enter a valid colour and try again.")
        return
    try:
        alpha = int(opacity_entry.get())
    except ValueError:
        notify_label.config(text="Invalid alpha value. Please enter a value between 0 and 255.")
        return

    errors = False
    num = 0

    for img in image_list:
        num += 1
        text_mark = TextMark(text, img, colour, alpha, num)
        if not text_mark.add_mark():
            errors = True

    if errors:
        image_list_label.config(text="No Image Found. Please check the file path and try again")
    else:
        notify_label.config(text="Watermark Added Successfully")
        image_list_label.config(text="No Images Currently Selected")
        image_list.clear()


def add_watermark_img():
    num = 0
    wm = img_mark_entry.get()
    errors = False
    for img in image_list:
        num += 1
        image_mark = ImageMark(img, wm, num)
        if not image_mark.add_mark():
            errors = True

    if errors:
        image_list_label.config(text="No Image Found. Please check the file path and try again")
    else:
        notify_label.config(text="Watermark Added Successfully")
        image_list_label.config(text="No Images Currently Selected")
        image_list.clear()


def add_watermark():
    mark = (var.get())
    if len(image_list) != 0:
        if mark == 1:
            add_watermark_text()
        elif mark == 2:
            add_watermark_img()
        else:
            image_list_label.config(text="Please select the type of watermark you wish to add.")
    else:
        image_list_label.config(text="Please select an target image to add a watermark to.")


def mark_type():
    mark = (var.get())
    if mark == 1:
        text_entry.config(state="normal")
        img_mark_entry.config(state="disabled")
    else:
        img_mark_entry.config(state="normal")
        text_entry.config(state="disabled")

# GUI

root = Tk()
var = IntVar()
root.title("WaterMarker")
root.config(padx=50, bg="#00adb5")

canvas = Canvas(width=400, height=150, bg="#00adb5", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

type_label = Label(text="Watermark type:", bg="#00adb5", pady=40)
type_label.grid(column=0, row=1)

R1 = Radiobutton(text="Text", variable=var, value=1, bg="#00adb5", highlightthickness=0, relief=FLAT, command=mark_type)
R1.grid(column=1, row=1)

R2 = Radiobutton(text="Image", variable=var, value=2, bg="#00adb5", highlightthickness=0, relief=FLAT, command=mark_type)
R2.grid(column=2, row=1, pady=2.5)

img_mark_label = Label(text="File path for watermark image:", bg="#00adb5")
img_mark_label.grid(column=0, row=2)

img_mark_entry = Entry(width=35, bg="#eaeaea", highlightbackground="#393E46", state="disabled")
img_mark_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=5)
img_mark_entry.config(relief=FLAT)

text_label = Label(text="Watermark text:", bg="#00adb5")
text_label.grid(column=0, row=3)

text_entry = Entry(width=35, bg="#eaeaea", highlightbackground="#393E46", state="disabled")
text_entry.grid(column=1, row=3, columnspan=2, sticky="EW", pady=5)
text_entry.insert(0, "Watermark Text Here...")
text_entry.config(relief=FLAT)

colour_label = Label(text="Colour:", bg="#00adb5")
colour_label.grid(column=0, row=4)

colour_entry = Entry(width=35, bg="#eaeaea", highlightbackground="#393E46")
colour_entry.grid(column=1, row=4, sticky="EW", pady=5)
colour_entry.insert(0, "#FFFFFF")
colour_entry.config(relief=FLAT)

opacity_label = Label(text="Opacity:", bg="#00adb5")
opacity_label.grid(column=0, row=5)

opacity_entry = Entry(width=35, bg="#eaeaea", highlightbackground="#393E46")
opacity_entry.grid(column=1, row=5, sticky="EW", pady=5)
opacity_entry.insert(0, "100")
opacity_entry.config(relief=FLAT)

target_select_label = Label(text="File path for target image:", bg="#00adb5")
target_select_label.grid(column=0, row=6)

target_entry = Entry(width=35, bg="#eaeaea", highlightbackground="#393E46")
target_entry.grid(column=1, row=6, columnspan=2, sticky="EW", pady=20)
target_entry.insert(0, "")
target_entry.config(relief=FLAT)

select = Button(text="Select", command=get_target_img, relief=FLAT, bg="#40514e", fg="#eaeaea", highlightthickness=0)
select.grid(column=1, row=7, sticky="EW")

selected_label = Label(text="Selected Images:", bg="#00adb5")
selected_label.grid(column=0, row=8)

image_list_label = Label(text="No Images Currently Selected", bg="#00adb5")
image_list_label.grid(column=1, row=8, pady=20)

remove_img_button = Button(text="Remove Image", command=remove_img, relief=FLAT, bg="#40514e", fg="#eaeaea", highlightthickness=0)
remove_img_button.grid(column=1, row=9, sticky="EW")

add_watermark_button = Button(text="Add Watermark", command=add_watermark, relief=FLAT, bg="#40514e", fg="#eaeaea", highlightthickness=0)
add_watermark_button.grid(column=1, row=10, sticky="EW", pady=20)

notify_label = Label(text="", bg="#00adb5")
notify_label.grid(column=1, row=11)

root.mainloop()