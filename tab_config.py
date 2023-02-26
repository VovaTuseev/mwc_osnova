import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
import tkinter
import datetime
import os
from db_file import registration_function
from db_file import authorization_function

global switch_flag


class MyConfigFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.left_s_f = RegistrationAuthorizationFrame(master)
        self.left_s_f.place(x=30, y=20)

        self.right_s_f = ConfigPlaceCam(master)
        self.right_s_f.place(x=320, y=20)

        self.way_s_f = ConfigWayRecords(master)
        self.way_s_f.place(x=1250, y=20)


# --------------------------------------------------------------------------------------------------------------


class RegistrationAuthorizationFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        container = ctk.CTkFrame(self)
        container.pack()

        self.frames = {}

        for F in (AuthorizationFrame, AuthorizationFrameTrue):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(AuthorizationFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    # def __init__(self, master):
    #     super().__init__(master)
    #     self._frame = None
    #     self.switch_frame(StartPage)

    # def switch_frame(self, frame_class):
    #     new_frame = frame_class(self)
    #     if self._frame is not None:
    #         self._frame.destroy()
    #     self._frame = new_frame
    #     self._frame.pack()


class AuthorizationFrame(ctk.CTkFrame):  # Класс основного фрейма авторизации/регистрации
    def __init__(self, master, controller):
        CTkFrame.__init__(self, master)
        # Настройка авторизации/регистрации----------------------------------------------------------------------------
        self.autoreg_frame = ctk.CTkFrame(self, fg_color='#262626')
        font_main = ctk.CTkFont(family="helvetica", size=15)

        # photo_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # login_label_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # login_entry_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # pas_label_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # pas_entry_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # btn_login_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # registration_label = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # registration_btn = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')

        img = ctk.CTkImage(dark_image=Image.open("ava-transformed.png"), size=(100, 100))
        label_ava = CTkLabel(self, text='', image=img)

        label_login = ctk.CTkLabel(self, text="Введите логин", font=font_main)

        entry_login = ctk.CTkEntry(self, width=150)

        label_password = ctk.CTkLabel(self, text="Введите пароль", font=font_main)

        entry_password = ctk.CTkEntry(self, width=150)

        btn_login = ctk.CTkButton(self, text="Авторизоваться",
                                  command=lambda: controller.show_frame(AuthorizationFrameTrue))  # authorization_function(entry_login, entry_password)

        label_registration = ctk.CTkLabel(self, text="Нет аккаунта?")

        btn_registration = ctk.CTkButton(self, text="Регистрирация",
                                         command=registration_function)

        label_ava.pack(padx=80, pady=10)
        label_login.pack(anchor=CENTER, pady=5)
        entry_login.pack()
        label_password.pack(pady=5)
        entry_password.pack()
        btn_login.pack(pady=15)
        label_registration.pack()
        btn_registration.pack(pady=10)

        # photo_frame.pack(anchor=W)
        # login_label_frame.pack(anchor=CENTER)
        # login_entry_frame.pack(anchor=CENTER)
        # pas_label_frame.pack(anchor=CENTER)
        # pas_entry_frame.pack(anchor=CENTER)
        # btn_login_frame.pack(anchor=CENTER)
        # registration_label.pack(anchor=CENTER)
        # registration_btn.pack(anchor=CENTER)

        # self.autoreg_frame.pack(padx=5, pady=5)


class AuthorizationFrameTrue(ctk.CTkFrame):  # Класс фрейма успешной авторизации
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        # Настройка авторизации/регистрации----------------------------------------------------------------------------
        self.autoreg_frame = ctk.CTkFrame(self, fg_color='#262626')
        font_main = ctk.CTkFont(family="helvetica", size=15)

        # photo_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # login_label_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # login_entry_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # pas_label_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # pas_entry_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # btn_exit_frame = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # load_label = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')
        # load_label_btn = ctk.CTkFrame(self.autoreg_frame, fg_color='#262626')

        img = ctk.CTkImage(dark_image=Image.open("ava-transformed.png"), size=(100, 100))
        label_ava = CTkLabel(self, text='', image=img)
        label_ava.pack(padx=80, pady=10)

        label_login = ctk.CTkLabel(self, text="Логин", font=font_main)
        label_login.pack(anchor=CENTER, pady=5)

        entry_login = ctk.CTkEntry(self, width=150)
        entry_login.pack()

        label_password = ctk.CTkLabel(self, text="Пароль", font=font_main)
        label_password.pack(pady=5)

        entry_password = ctk.CTkEntry(self, width=150)
        entry_password.pack()

        btn_login = ctk.CTkButton(self, text="Выйти",
                                  command=lambda: controller.show_frame(AuthorizationFrame))  # authorization_function(entry_login, entry_password)
        btn_login.pack(pady=15)

        # photo_frame.pack(anchor=W)
        # login_label_frame.pack(anchor=CENTER)
        # login_entry_frame.pack(anchor=CENTER)
        # pas_label_frame.pack(anchor=CENTER)
        # pas_entry_frame.pack(anchor=CENTER)
        # btn_exit_frame.pack(anchor=CENTER)
        # load_label.pack(anchor=CENTER)
        # load_label_btn.pack(anchor=CENTER)

        # self.autoreg_frame.pack(padx=5, pady=5)


class ConfigPlaceCam(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        # Задание названий "столбцов" таблицы данных камер
        name_cam = ctk.CTkLabel(self, text="Камера")
        address_cam = ctk.CTkLabel(self, text="IP-адрес камеры")
        password_cam = ctk.CTkLabel(self, text="Пароль")
        # Первая строка
        self.name_entry_1 = ctk.CTkEntry(self, justify='center')
        self.address_entry_1 = ctk.CTkEntry(self, justify='center')
        self.password_entry_1 = ctk.CTkEntry(self, justify='center')
        self.btn_change_1 = ctk.CTkButton(self, text="Сохранить изменения")
        # Вторая строка
        self.name_entry_2 = ctk.CTkEntry(self, justify='center')
        self.address_entry_2 = ctk.CTkEntry(self, justify='center')
        self.password_entry_2 = ctk.CTkEntry(self, justify='center')
        self.btn_change_2 = ctk.CTkButton(self, text="Сохранить изменения")
        # Третья строка
        self.name_entry_3 = ctk.CTkEntry(self, justify='center')
        self.address_entry_3 = ctk.CTkEntry(self, justify='center')
        self.password_entry_3 = ctk.CTkEntry(self, justify='center')
        self.btn_change_3 = ctk.CTkButton(self, text="Сохранить изменения")
        # Четвертая строка
        self.name_entry_4 = ctk.CTkEntry(self, justify='center')
        self.address_entry_4 = ctk.CTkEntry(self, justify='center')
        self.password_entry_4 = ctk.CTkEntry(self, justify='center')
        self.btn_change_4 = ctk.CTkButton(self, text="Сохранить изменения")

        # Настройка расположения названий столбцов
        name_cam.grid(column=0, row=0, padx=80)
        address_cam.grid(column=1, row=0, padx=80)
        password_cam.grid(column=2, row=0, padx=80)
        # Настройка расположения данных для перовй камеры
        self.name_entry_1.grid(column=0, row=1, padx=10)
        self.address_entry_1.grid(column=1, row=1, padx=30)
        self.password_entry_1.grid(column=2, row=1, padx=30)
        self.btn_change_1.grid(column=3, row=1, padx=40, pady=20)
        # Настройка расположения данных для второй камеры
        self.name_entry_2.grid(column=0, row=2, padx=10)
        self.address_entry_2.grid(column=1, row=2, padx=30)
        self.password_entry_2.grid(column=2, row=2, padx=30)
        self.btn_change_2.grid(column=3, row=2, padx=10, pady=34)
        # Настройка расположения данных для третьей камеры
        self.name_entry_3.grid(column=0, row=3, padx=10)
        self.address_entry_3.grid(column=1, row=3, padx=30)
        self.password_entry_3.grid(column=2, row=3, padx=30)
        self.btn_change_3.grid(column=3, row=3, padx=10, pady=34)
        # Настройка расположения данных для четвертой камеры
        self.name_entry_4.grid(column=0, row=4, padx=10)
        self.address_entry_4.grid(column=1, row=4, padx=30)
        self.password_entry_4.grid(column=2, row=4, padx=30)
        self.btn_change_4.grid(column=3, row=4, padx=10, pady=35)


class ConfigWayRecords(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)

        label_way = ctk.CTkLabel(self, text='Путь сохранения видеозаписей', padx=20, pady=10)
        entry_way = ctk.CTkEntry(self, width=100)
        btn_way = ctk.CTkButton(self, text='', width=30)
        btn_open_way = ctk.CTkButton(self, text='Открыть', width=30)

        label_way.pack(anchor=CENTER)
        entry_way.pack(anchor=CENTER)
        btn_way.pack(anchor=CENTER)
        btn_open_way.pack(anchor=CENTER)
