import customtkinter
from customtkinter import *
import customtkinter as ctk
from customtkinter import *
from tkcalendar import Calendar
import tkinter
import datetime
import os
from tab_show import *
from tab_config import *


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.add("Наблюдение")
        self.add("Просмотр записей")
        self.add("Конфигурация")

        self.left_view_frame = MyFrameView(self.tab("Просмотр записей"))

        self.left_config_frame = MyConfigFrame(self.tab("Конфигурация"))

