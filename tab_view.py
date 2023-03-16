import customtkinter
from customtkinter import *
import customtkinter as ctk
from customtkinter import *
from tkcalendar import Calendar
import tkinter
import datetime
import os
import threading
from threading import Thread
from tab_show import *
from tab_config import *
from tab_monitoring import *
from threading import Thread
from multiprocessing import *


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.add("Наблюдение")
        self.add("Просмотр записей")
        self.add("Конфигурация")


        def create_view():
            self.left_view_frame = MyFrameView(self.tab("Просмотр записей"))
        t1 = Thread(target=create_view, args=())

        def create_show():
            self.left_config_frame = MyConfigFrame(self.tab("Конфигурация"))
        t2 = Thread(target=create_show, args=())

        def create_config():
            self.frame_vid = videoFrame(self.tab("Наблюдение"))
        t3 = Thread(target=create_config, args=())

        t1.start()
        t2.start()
        t3.start()

