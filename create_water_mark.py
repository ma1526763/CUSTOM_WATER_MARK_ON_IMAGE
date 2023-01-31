from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

BACKGROUND_THEME = "#222222"
primary_color = "#a44726"


class CreateWaterMark:
    def __init__(self, img, img_width, img_height, file_path):
        self.make_copy = False
        self.image = img
        self.file_path = file_path
        self.image_width = img_width
        self.image_height = img_height
        self.water_mark_window = Toplevel()
        self.canvas = Canvas(self.water_mark_window, width=self.image_width, height=self.image_height, borderwidth=0,
                             highlightthickness=0)
        self.canvas.grid(row=0, column=0, rowspan=8, columnspan=5)
        self.canvas.create_image(self.image_width // 2, self.image_height // 2, image=self.image)

        self.water_mark_text = self.canvas.create_text(self.image_width // 2, self.image_height // 2 + 10,
                                                       text="@Ali Riax", width=img_width - 20,
                                                       font=("Arial", 20, "bold"), fill="white", )

        self.user_text_entry = Entry(self.water_mark_window, width=25, font=("Arial", 12))
        self.user_text_entry.bind("<KeyRelease>", self.update_canvas_text)
        self.font_size_entry = Entry(self.water_mark_window, width=25, font=("Arial", 12))
        self.font_size_entry.bind("<KeyRelease>", self.update_font_size)
        self.font_box = None
        self.list_of_multiples = []
        self.create_multiple_copies()
        self.color_button = Button(self.water_mark_window, text="Choose Color", width=25, font=("Arial", 12,),
                                   command=self.change_water_mark_color, anchor=W)
        self.copy_button = Button(self.water_mark_window, text="Multiple Watermark", width=25, font=("Arial", 12,),
                                  command=self.copy_button_water_mark, anchor=W)
        self.reset_button = Button(self.water_mark_window, text="Reset Watermark", width=25, font=("Arial", 12,),
                                   command=self.reset_button_water_mark, anchor=W)

        self.angle_scale = Scale(self.water_mark_window, from_=-180, to=180, sliderrelief='flat', orient="horizontal",
                                 background=BACKGROUND_THEME, fg="#df5966", highlightthickness=0,
                                 troughcolor=primary_color, activebackground='black', showvalue=True, length=230,
                                 width=20,
                                 command=self.change_angle, )
        self.opacity_scale = Scale(self.water_mark_window, from_=0, to=100, sliderrelief='flat', orient="horizontal",
                                   background=BACKGROUND_THEME, fg="#df5966", highlightthickness=0,
                                   troughcolor=primary_color, activebackground='black', showvalue=True, length=230,
                                   width=20,
                                   command=self.change_opacity, )
        self.save_button = Button(self.water_mark_window, text="Save Image", background=primary_color,
                                  foreground="white",
                                  width=10, height=2, font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0,
                                  activebackground="#a44002", activeforeground="white", command=self.save_image)
        self.window_settings()
        self.water_mark_window.mainloop()

    def window_settings(self):
        self.water_mark_window.title("Water mark")
        self.water_mark_window.config(background=BACKGROUND_THEME)
        self.water_mark_window.geometry(f"{self.image_width + 370}x{self.image_height + 200}+200+100")
        self.water_mark_window.resizable(False, False)
        self.canvas.create_text(self.image_width - 35, self.image_height - 10,
                                text=f"{self.image_width} x {self.image_height}", font=("Arial", 10), fill="#E2DFD2")

        water_mark_options = Label(self.water_mark_window, text="Water Mark Options", padx=15, background=primary_color,
                                   foreground="white", font=("Arial", 14), )
        water_mark_options.grid(row=1, column=7, sticky="N")

        self.create_label("Text: ", r=2)
        self.create_label("Size: ", r=3)
        self.create_label("Font: ", r=4)
        self.create_label("Rotate", r=5)
        self.create_label("Opacity", r=6)
        self.create_label("Color:", r=8)
        self.create_label("Copy:", r=10)
        self.create_label("Reset:", r=11)
        self.create_label("● Add custom water mark, size, opacity, angle, and font etc.", r=9, c=1, color="#E2DFD2",
                          size="normal", sticky="WS")
        self.create_label("● Offer various output formats, such as JPG, PNG, or GIF.", r=10, c=1, color="#E2DFD2",
                          size="normal", sticky="WS")
        self.create_label("● Created by @Ali Riax. Design is simple and flexible!!", r=11, c=1, color="#E2DFD2",
                          size="normal", sticky="WS")
        self.create_label("● Save it to your computer without any charges. Its Free!!.", r=12, c=1, color="#E2DFD2",
                          size="normal", sticky="WN")

        self.user_text_entry.grid(row=2, column=7, sticky="W", ipady=3, columnspan=2)
        self.user_text_entry.insert(0, "@Ali Riax")
        self.font_size_entry.grid(row=3, column=7, sticky="W", ipady=3, columnspan=2)
        self.font_size_entry.insert(0, "20")

        with open("fonts.txt") as file:
            font_list = [font.strip() for font in file.readlines()]
            self.font_box = ttk.Combobox(self.water_mark_window, values=font_list, width=23, font=("", 12))
            self.font_box.set("Arial")
            self.font_box.grid(row=4, column=7, sticky="W", ipady=3, columnspan=2)
            self.font_box.bind("<<ComboboxSelected>>", self.get_selected_font)
        self.angle_scale.grid(row=5, column=7, sticky="W", columnspan=1)
        self.opacity_scale.grid(row=6, column=7, sticky="W", columnspan=1)
        self.color_button.grid(row=8, column=7, sticky="W", columnspan=2)
        self.copy_button.grid(row=10, column=7, sticky="W", columnspan=2)
        self.reset_button.grid(row=11, column=7, sticky="W", columnspan=2)
        self.save_button.grid(row=12, column=7, sticky="EN", pady=15)

    def update_canvas_text(self, event):
        user_text = self.user_text_entry.get()
        if len(user_text) <= 15:
            self.canvas.itemconfig(self.water_mark_text, text=user_text)
            self.check_copy()

    def update_font_size(self, event):
        try:
            font_size = int(self.font_size_entry.get())
        except ValueError:
            return
        else:
            if 0 <= font_size <= 200:
                font = self.canvas.itemconfig(self.water_mark_text, "font")[-1].split()[0]
                self.canvas.itemconfig(self.water_mark_text, font=(font, font_size, "bold"))
                self.check_copy()

    def get_selected_font(self, event):
        font = self.font_box.get()
        try:
            font_size = int(self.font_size_entry.get())
        except ValueError:
            font_size = 0
        if not font_size:
            font_size = 0
        self.canvas.itemconfig(self.water_mark_text, font=(font, font_size, "bold"))
        self.check_copy()

    def change_water_mark_color(self):
        color = askcolor(title="Water mark Color Chooser")[1]
        self.color_button.config(background=color)
        self.canvas.itemconfig(self.water_mark_text, fill=color)
        self.check_copy()

    def create_label(self, text, r, c=6, color=primary_color, p_y=0, size="bold", sticky="W"):

        label = Label(self.water_mark_window, text=text, padx=6, pady=p_y, background=BACKGROUND_THEME,
                      foreground=color, font=("Arial", 14, size))
        label.grid(row=r, column=c, sticky=sticky)

    def create_multiple_copies(self):
        img_width = self.image_width
        img_height = self.image_height
        for i in [[70, 30], [img_width // 2, 30], [img_width - 70, 30], [img_width // 3, img_height // 3],
                  [img_width // 1.5, img_height // 3], [70, img_height // 2], [img_width - 70, img_height // 2],
                  [img_width // 3, img_height // 1.4], [img_width // 1.4, img_height // 1.4, ], [70, img_height - 30],
                  [img_width // 2, img_height - 30], [img_width - 70, img_height - 30]]:
            new_text = self.canvas.create_text(i[0], i[1])
            self.list_of_multiples.append(new_text)

    def reset_button_water_mark(self):
        self.make_copy = False
        for canvas_text in self.list_of_multiples:
            self.canvas.itemconfig(canvas_text, text="")

    def copy_button_water_mark(self):
        self.make_copy = True
        text = self.canvas.itemconfig(self.water_mark_text, "text")[-1]
        color = self.canvas.itemconfig(self.water_mark_text, "fill")[-1]
        font = self.canvas.itemconfig(self.water_mark_text, "font")[-1].split()
        angle = self.canvas.itemconfig(self.water_mark_text, "angle")[-1]
        for canvas_text in self.list_of_multiples:
            self.canvas.itemconfig(canvas_text, text=text, width=self.image_width - 20,
                                   font=(font[0], int(font[1]), font[2]), fill=color, angle=int(float(angle)))

    def check_copy(self):
        if self.make_copy:
            self.copy_button_water_mark()

    def change_angle(self, value):
        self.canvas.itemconfig(self.water_mark_text, angle=int(value))
        self.check_copy()

    def change_opacity(self, value):
        x = self.canvas
        self.check_copy()
        print(int(value))

    def save_image(self):
        print(self.image)
