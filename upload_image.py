from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from create_water_mark import CreateWaterMark
# from practice import WaterMark

BACKGOUND = "#222222"

class UploadImage:
    def __init__(self):
        self.upload_window = Tk()
        self.img = PhotoImage(file="upload.png")
        self.canvas = Canvas(self.upload_window, width=204, height=152, highlightthickness=0)
        self.window_settings()
        self.upload_window.mainloop()

    def window_settings(self):
        self.upload_window.config(padx=50, pady=50, bg=BACKGOUND)
        self.upload_window.title("Upload Files")
        self.upload_window.geometry("800x600+200+100")
        self.upload_window.resizable(False, False)
        self.canvas.create_image(102, 76, image=self.img)
        self.canvas.place(x=300, y=80)
        add_water_mark_label = Label(self.upload_window, text="Add watermark", font=("Arial", 20), foreground="white",
                                     background=BACKGOUND)
        add_water_mark_label.place(x=270, y=240)
        upload_photo_button = Button(self.upload_window, text="Upload Photo", font=("Arial", 20, "bold"),
                                     background="#df5966",
                                     activebackground="#ce6e88", activeforeground="white", foreground="white",
                                     command=self.load_photo_from_computer)
        upload_photo_button.place(x=260, y=300)

    def load_photo_from_computer(self):
        f_types = [("jpeg", ".jpg .jpeg"), ("png", ".png"), ("gif", ".gif")]
        file_path = filedialog.askopenfilename(filetypes=f_types)
        if file_path:
            img = Image.open(file_path)
            image_width, image_height = img.width, img.height
            while image_width > 650 or image_height > 550:
                image_width = image_width - int(image_width * 0.05)
                image_height = image_height - int(image_height * 0.05)
            print(image_width, image_height)
            while image_width < 550:
                image_width = image_width + int(image_width * 0.05)
                image_height = image_height + int(image_height * 0.01)
            if image_height > 600:
                image_height = image_height - int(image_height*0.35)
            print(image_height)

            img_resized = img.resize((image_width, image_height))  # new width & height
            img = ImageTk.PhotoImage(img_resized)
            self.upload_window.iconify()
            CreateWaterMark(img, image_width, image_height, file_path)
            # WaterMark(img)
