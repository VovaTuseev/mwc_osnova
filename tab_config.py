import customtkinter as ctk
from PIL.ImageTk import PhotoImage
from customtkinter import *
from customtkinter import CTkImage
from PIL import ImageTk, Image
import os
from db_file import registration_function
from db_file import authorization_function
from work_with_config_cam_frame import set_data_options_cam, set_text

global switch_flag


class MyConfigFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.left_s_f = RegistrationAuthorizationFrame(master)
        self.left_s_f.place(x=30, y=20)

        self.right_s_f = ConfigPlaceCam(master)
        self.right_s_f.place(x=325, y=20)

        self.way_s_f = ConfigWayRecords(master)
        self.way_s_f.place(x=1255, y=20)


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
        # self.autoreg_frame = ctk.CTkFrame(self, fg_color='#262626')
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
                                  command=lambda: controller.show_frame(
                                      AuthorizationFrameTrue))  # authorization_function(entry_login, entry_password)

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
        # self.autoreg_frame = ctk.CTkFrame(self, fg_color='#262626')
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
                                  command=lambda: controller.show_frame(
                                      AuthorizationFrame))  # authorization_function(entry_login, entry_password)
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

        def func_for_first_cam():
            set_data_options_cam(self.name_entry_1.get(),
                                 self.address_entry_1.get(),
                                 self.password_entry_1.get())

        def func_for_second_cam():
            set_data_options_cam(self.name_entry_2.get(),
                                 self.address_entry_2.get(),
                                 self.password_entry_2.get())

        def func_for_third_cam():
            set_data_options_cam(self.name_entry_3.get(),
                                 self.address_entry_3.get(),
                                 self.password_entry_3.get())

        def func_for_fourth_cam():
            set_data_options_cam(self.name_entry_4.get(),
                                 self.address_entry_4.get(),
                                 self.password_entry_4.get())

        def func_for_all_cam():
            func_for_first_cam()
            func_for_second_cam()
            func_for_third_cam()
            func_for_fourth_cam()

        ctk.CTkFrame.__init__(self, master)
        # Задание названий "столбцов" таблицы данных камер
        name_cam = ctk.CTkLabel(self, text="Камера")
        address_cam = ctk.CTkLabel(self, text="IP-адрес камеры")
        password_cam = ctk.CTkLabel(self, text="Пароль")
        # Первая строка
        self.name_entry_1 = ctk.CTkEntry(self, justify='center')
        self.name_entry_1.insert(0, "CAM1")
        self.name_entry_1.configure(state=DISABLED)

        self.address_entry_1 = ctk.CTkEntry(self, justify='center')
        self.password_entry_1 = ctk.CTkEntry(self, justify='center')
        self.btn_change_1 = ctk.CTkButton(self, text="Сохранить изменения", command=func_for_first_cam)
        # Вторая строка
        self.name_entry_2 = ctk.CTkEntry(self, justify='center')
        self.name_entry_2.insert(0, "CAM2")
        self.name_entry_2.configure(state=DISABLED)

        self.address_entry_2 = ctk.CTkEntry(self, justify='center')
        self.password_entry_2 = ctk.CTkEntry(self, justify='center')
        self.btn_change_2 = ctk.CTkButton(self, text="Сохранить изменения", command=func_for_second_cam)
        # Третья строка
        self.name_entry_3 = ctk.CTkEntry(self, justify='center')
        self.name_entry_3.insert(0, "CAM3")
        self.name_entry_3.configure(state=DISABLED)

        self.address_entry_3 = ctk.CTkEntry(self, justify='center')
        self.password_entry_3 = ctk.CTkEntry(self, justify='center')
        self.btn_change_3 = ctk.CTkButton(self, text="Сохранить изменения", command=func_for_third_cam)
        # Четвертая строка
        self.name_entry_4 = ctk.CTkEntry(self, justify='center')
        self.name_entry_4.insert(0, "CAM4")
        self.name_entry_4.configure(state=DISABLED)

        self.address_entry_4 = ctk.CTkEntry(self, justify='center')
        self.password_entry_4 = ctk.CTkEntry(self, justify='center')
        self.btn_change_4 = ctk.CTkButton(self, text="Сохранить изменения", command=func_for_fourth_cam)

        # Кнопка записи сразу всех строк, возможности вносить изменения и загрузка данных из БД
        self.btn_change_all = ctk.CTkButton(self, text="Сохранить все", width=150, command=func_for_all_cam,
                                            fg_color="#008000")

        self.btn_access = ctk.CTkButton(self, text="Внести изменения", fg_color="#A0522D") #A0522D

        self.btn_load = ctk.CTkButton(self, text="Загрузить данные")

        # Настройка расположения названий столбцов
        name_cam.grid(column=0, row=0, padx=80)
        address_cam.grid(column=1, row=0, padx=80)
        password_cam.grid(column=2, row=0, padx=80)

        # Настройка расположения данных для перовой камеры
        self.name_entry_1.grid(column=0, row=1, padx=10)
        self.address_entry_1.grid(column=1, row=1, padx=30)
        self.password_entry_1.grid(column=2, row=1, padx=30)
        self.btn_change_1.grid(column=3, row=1, padx=40, pady=22)

        # Настройка расположения данных для второй камеры
        self.name_entry_2.grid(column=0, row=2, padx=10)
        self.address_entry_2.grid(column=1, row=2, padx=30)
        self.password_entry_2.grid(column=2, row=2, padx=30)
        self.btn_change_2.grid(column=3, row=2, padx=10, pady=22)

        # Настройка расположения данных для третьей камеры
        self.name_entry_3.grid(column=0, row=3, padx=10)
        self.address_entry_3.grid(column=1, row=3, padx=30)
        self.password_entry_3.grid(column=2, row=3, padx=30)
        self.btn_change_3.grid(column=3, row=3, padx=10, pady=22)

        # Настройка расположения данных для четвертой камеры
        self.name_entry_4.grid(column=0, row=4, padx=10)
        self.address_entry_4.grid(column=1, row=4, padx=30)
        self.password_entry_4.grid(column=2, row=4, padx=30)
        self.btn_change_4.grid(column=3, row=4, padx=10, pady=22)

        # Настройка расположения кнопок с общими функциями
        self.btn_access.grid(column=1, row=5)
        self.btn_load.grid(column=2, row=5)
        self.btn_change_all.grid(column=3, row=5, pady=20)


class ConfigWayRecords(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)

        self.frame_btn_entry = ctk.CTkFrame(self, fg_color='transparent')

        img = ctk.CTkImage(dark_image=Image.open('papka-transformed.png'), size=(15, 15))

        label_way = ctk.CTkLabel(self, text='Путь сохранения видеозаписей', padx=20, pady=20)
        entry_way = ctk.CTkEntry(self.frame_btn_entry, width=150)
        btn_way = ctk.CTkButton(self.frame_btn_entry, text='', width=30, image=img)
        btn_open_way = ctk.CTkButton(self, text='Открыть', width=30)

        label_way.pack(anchor=CENTER)
        entry_way.grid(row=0, column=0, padx=15)
        btn_way.grid(row=0, column=1)
        self.frame_btn_entry.pack(anchor=W, pady=5)
        btn_open_way.pack(anchor=W, padx=15, pady=10)
