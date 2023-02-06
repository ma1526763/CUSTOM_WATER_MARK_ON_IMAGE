# from tkinter import *
# from PIL import Image, ImageDraw, ImageFont, ImageTk
#
#
# class WaterMark:
#     def __init__(self, img):
#         self.image = img
#         self.water_mark_window = Toplevel()
#         self.canvas = Canvas(self.water_mark_window, width=582, height=340)
#         self.canvas.grid(row=0, column=0)
#         self.canvas.create_image(291, 170, image=img)
#         self.opacity_scale = Scale(self.water_mark_window, from_=0, to=100, command=self.change_opacity)
#         self.opacity_scale.grid(row=0, column=1)
#         x= 20
#         y =20
#         a= []
#         for i in range(4):
#             self.x = x
#             self.y = y
#             x += 30
#             y +=50
#             self.create_transparent_text_images()
#             a.append(self.canvas.create_image(150, 150, image=self.transparent_text_images[100], anchor=CENTER))
#         self.water_mark_window.mainloop()
#
#     def change_opacity(self, value):
#         opacity = int(value)
#         self.canvas.itemconfig(self.transparent_text_image, image=self.transparent_text_images[opacity])
#
#     def create_transparent_text_images(self):
#         self.transparent_text_images = {}
#         font = ImageFont.truetype("arial.ttf", 20)
#         for i in range(101):
#             opacity = i / 100
#             image = Image.new("RGBA", (300, 300), (255, 255, 255, 0))
#             draw = ImageDraw.Draw(image)
#             draw.text((self.x, self.y), "Water Mark", font=font, fill=(255, 255, 255, int(255 * opacity)))
#             self.transparent_text_images[i] = ImageTk.PhotoImage(image)
