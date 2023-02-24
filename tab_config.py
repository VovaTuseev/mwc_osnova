import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
import tkinter
import datetime
import os
from db_file import registration_function
from db_file import LOGIN
from db_file import PASSWORD


class MyConfigFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.left_s_f = left_show_frame(master)


class left_show_frame(ctk.CTkFrame):
    def __init__(self, master, login, password):

        self.login = login
        self.password = password

        super().__init__(master)
        self.autoriz = ctk.CTkFrame(master, fg_color='#262626')
        auto = AuthorizationFrame(self.autoriz)
        self.autoriz.place(x=10, y=10)

        # Настройка фрейма со списком камер
        self.list_cam_frame = ctk.CTkFrame(master, fg_color='#262626')

        first = ConfigCAM(self.list_cam_frame, 'CAM1')
        second = ConfigCAM(self.list_cam_frame, 'CAM2')
        third = ConfigCAM(self.list_cam_frame, 'CAM3')
        fourth = ConfigCAM(self.list_cam_frame, 'CAM4')

        self.list_cam_frame.place(x=300, y=10)

        # --------------------------------------------------------------------------------------------------------------


class AuthorizationFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Настройка авторизации/регистрации----------------------------------------------------------------------------
        self.autoreg_frame = ctk.CTkFrame(master, fg_color='#262626')
        font_main = ctk.CTkFont(family="helvetica", size=15)

        photo_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        login_label_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        login_entry_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        pas_label_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        pas_entry_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        btn_login_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        registration_label = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        registration_btn = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')

        img = ctk.CTkImage(dark_image=Image.open("ava-transformed.png"), size=(100, 100))
        label_ava = CTkLabel(photo_frame, text='', image=img)
        label_ava.pack(padx=80, pady=10)

        label_login = ctk.CTkLabel(login_label_frame, text="Введите логин", font=font_main)
        label_login.pack(anchor=CENTER, pady=5)

        entry_login = ctk.CTkEntry(login_entry_frame, width=150)
        entry_login.pack()

        label_password = ctk.CTkLabel(pas_label_frame, text="Введите пароль", font=font_main)
        label_password.pack(pady=5)

        entry_password = ctk.CTkEntry(pas_entry_frame, width=150)
        entry_password.pack()

        btn_login = ctk.CTkButton(btn_login_frame, text="Авторизоваться")
        btn_login.pack(pady=15)

        label_registration = ctk.CTkLabel(registration_label, text="Нет аккаунта?")
        label_registration.pack()

        btn_registration = ctk.CTkButton(registration_btn, text="Регистрирация", command=registration_function)
        btn_registration.pack(pady=10)

        photo_frame.pack(anchor=W)
        login_label_frame.pack(anchor=CENTER)
        login_entry_frame.pack(anchor=CENTER)
        pas_label_frame.pack(anchor=CENTER)
        pas_entry_frame.pack(anchor=CENTER)
        btn_login_frame.pack(anchor=CENTER)
        registration_label.pack(anchor=CENTER)
        registration_btn.pack(anchor=CENTER)

        self.autoreg_frame.pack(padx=5, pady=5)


class ConfigCAM(ctk.CTkFrame):
    def __init__(self, master, name_cam_ent):
        self.name_cam = name_cam_ent
        super().__init__(master)

        def write_name_cam(ent, s):  # Функция записи имени в текстовое поле ткинтер
            ent.insert(0, s)
            ent.configure(state='disabled')
        self.ip_address_cam = ""
        self.password_cam = ""

        # Настройка фрейма для данных камер-----------------------------------------------------------------------------
        self.frame_cam = ctk.CTkFrame(master, fg_color='transparent')

        name_cam = ctk.CTkLabel(self.frame_cam, text="Камера")
        name_cam.grid(column=0, row=0)

        self.name_entry = ctk.CTkEntry(self.frame_cam, justify='center')
        self.name_entry.grid(column=0, row=1, padx=10)

        address_cam = ctk.CTkLabel(self.frame_cam, text="IP-адрес камеры")
        address_cam.grid(column=1, row=0)

        self.address_entry = ctk.CTkEntry(self.frame_cam)
        self.address_entry.grid(column=1, row=1, padx=30)

        password_cam = ctk.CTkLabel(self.frame_cam, text="Пароль")
        password_cam.grid(column=2, row=0)

        self.password_entry = ctk.CTkEntry(self.frame_cam)
        self.password_entry.grid(column=2, row=1, padx=30, pady=10)

        self.btn_change = ctk.CTkButton(self.frame_cam, text="Редактировать")
        self.btn_change.grid(column=3, row=1, padx=10)

        write_name_cam(self.name_entry, name_cam_ent)

        self.frame_cam.pack(padx=60, pady=15)

