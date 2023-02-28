import customtkinter
from customtkinter import *
from PIL import *
import cv2

import start_window
from tab_view import *
from tab_config import *
from db_file import *
from start_window import take_pass_postgresql


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("MuLCAM")
        self.attributes('-fullscreen', False)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(True, True)

        self.tab_view = MyTabView(master=self)
        self.tab_view.pack()

        self.fr = MyFrameView(master=self, height=self.winfo_screenheight(), width=self.winfo_screenwidth())


# take_pass_postgresql()
start_window.password_postgres = "tuiiutVT29072001"
app = App()
app.mainloop()

# j = ctk.CTk()
# fr = ConfigPlaceCam(j)
# fr.pack()
# j.mainloop()

