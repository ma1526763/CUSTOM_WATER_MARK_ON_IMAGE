from tkinter import *
from upload_image import UploadImage
BACKGROUND_THEME = "#051b35"

class FrontScreen:
    def __init__(self):
        self.window = Tk()
        self.set_front_screen()
        self.window.mainloop()

    def set_front_screen(self):
        self.window.title("Watermark")
        self.window.geometry("800x600+150+100")
        self.window.resizable(False, False)
        self.window.config(pady=50, padx=50, bg=BACKGROUND_THEME)
        make_label = Label(text="Make", font=("Arial", 54, "bold"), bg=BACKGROUND_THEME, fg="white")
        make_label.place(x=100, y=50)
        watermark_label = Label(text="Watermark", font=("Arial", 54, "bold"), bg=BACKGROUND_THEME, fg="white")
        watermark_label.place(x=100, y=125)
        quickly_label = Label(text="Quickly", font=("Arial", 54, "bold"), bg=BACKGROUND_THEME, fg="white")
        quickly_label.place(x=100, y=200)
        quickly_label = Label(text="Edit & add watermark to images quickly.", font=("Arial", 16), bg=BACKGROUND_THEME, fg="white")
        quickly_label.place(x=100, y=290)
    #     create_water_mark = Button(text="Create Watermark", font=("Arial", 28, "bold"), fg=BACKGROUND_THEME, command=self.upload_photo)
    #     create_water_mark.place(x=100, y=340)
    #
    # def upload_photo(self):
    #     self.window.destroy()
    #     UploadImage()
