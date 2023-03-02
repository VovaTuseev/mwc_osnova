import customtkinter as ctk
from PIL.ImageTk import PhotoImage
from customtkinter import *
from customtkinter import CTkImage
from PIL import ImageTk, Image
import start_window
import work_with_config_cam_frame
from Registration_func import registration_function
from work_with_config_cam_frame import set_data_options_cam, load_data_bd
from Autorization_func import check_login_password
import chess
import chess.svg
import chess.svg


class MyConfigFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # self.left_s_f = RegistrationAuthorizationFrame(master)
        # self.left_s_f.place(x=30, y=20)

        # self.right_s_f = ConfigPlaceCam(master)
        # self.right_s_f.place(x=325, y=20)

        self.frame_l = registration_configCam(master)
        self.frame_l.place(x=20, y=20)

        self.way_s_f = ConfigWayRecords(master)
        self.way_s_f.place(x=1273, y=20)
        self.way_s_f.configure(fg_color='#313131')

        img = ctk.CTkImage(dark_image=Image.open("LOGOPNG.png"), size=(700, 175))
        self.label_logo = ctk.CTkLabel(master, text='', image=img)
        self.label_logo.place(x=420, y=470)


# --------------------------------------------------------------------------------------------------------------
# Класс для переключения фреймов авторизации + конфигурации камер
class registration_configCam(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        container = ctk.CTkFrame(self)
        container.pack()

        self.frames = {}

        for F in (RegAutoFalseConfig, RegAutoTrueConfig):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(RegAutoFalseConfig)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class RegAutoFalseConfig(ctk.CTkFrame):
    def __init__(self, master, controller):
        ctk.CTkFrame.__init__(self, master)

        authorization_frame = AuthorizationFrame(self, controller)
        authorization_frame.grid(column=0, row=0)
        authorization_frame.configure(fg_color='#313131')

        config_cam_false = ConfigPlaceCamFalse(self)
        config_cam_false.grid(column=1, row=0, padx=33)
        config_cam_false.configure(fg_color='#313131')

        self.configure(fg_color='transparent')


class RegAutoTrueConfig(ctk.CTkFrame):
    def __init__(self, master, controller):
        ctk.CTkFrame.__init__(self, master)

        authorization_frame = AuthorizationFrameTrue(self, controller)
        authorization_frame.grid(column=0, row=0, sticky='nsew')
        authorization_frame.configure(fg_color='#313131')

        config_cam_false = ConfigPlaceCamTrue(self)
        config_cam_false.grid(column=1, row=0, padx=33)
        config_cam_false.configure(fg_color='#313131')

        self.configure(fg_color='transparent')


# Класс основного фрейма авторизации/регистрации
class AuthorizationFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        CTkFrame.__init__(self, master)
        # Настройка авторизации/регистрации----------------------------------------------------------------------------

        def authorization_function():  # Функция обработки авторизации
            login = str(entry_login.get())
            password = str(entry_password.get())
            print(check_login_password(login, password))
            if check_login_password(login, password) is True:
                start_window.login_acc = login
                start_window.password_acc = password
                controller.show_frame(RegAutoTrueConfig)
                entry_password.delete(0, END)
            else:
                error_window = CTk()
                label_error = ctk.CTkLabel(error_window, text_color='red', text='Данные пользователя неверны')
                label_error.pack()
                error_window.mainloop()

        font_main = ctk.CTkFont(family="helvetica", size=15)

        img = ctk.CTkImage(dark_image=Image.open("ava-transformed.png"), size=(100, 100))

        label_ava = CTkLabel(self, text='', image=img)

        label_login = ctk.CTkLabel(self, text="Введите логин", font=font_main)

        entry_login = ctk.CTkEntry(self, width=150)

        label_password = ctk.CTkLabel(self, text="Введите пароль", font=font_main)

        entry_password = ctk.CTkEntry(self, width=150, show="*")

        btn_login = ctk.CTkButton(self, text="Авторизоваться",
                                  command=authorization_function)  # authorization_function(entry_login, entry_password)

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


# Класс фрейма успешной авторизации
class AuthorizationFrameTrue(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        def exit_funct():
            def func_btn():
                start_window.login_acc = ""
                start_window.password_acc = ""
                controller.show_frame(RegAutoFalseConfig)
                sure.destroy()

            sure = CTk()
            sure.title("Подтвердите выбор")
            sure.geometry("100,100")
            sure.resizable(False, False)
            sure.label = ctk.CTkLabel(sure, text="Вы уверены?")
            sure.label.pack()
            sure.btn = ctk.CTkButton(sure, text="Выйти", command=func_btn)
            sure.btn.pack()
            sure.mainloop()

        font_main = ctk.CTkFont(family="helvetica", size=15)

        img = ctk.CTkImage(dark_image=Image.open("ava-transformed.png"), size=(100, 100))
        label_ava = CTkLabel(self, text='', image=img)
        label_ava.pack(padx=80, pady=10)

        label_login = ctk.CTkLabel(self, text="Логин", font=font_main)
        label_login.pack(anchor=CENTER, pady=5)

        entry_login = ctk.CTkEntry(self, width=150)
        entry_login.insert(0, '********')
        entry_login.configure(state='disabled')
        entry_login.pack()

        label_password = ctk.CTkLabel(self, text="Пароль", font=font_main)
        label_password.pack(pady=5)

        entry_password = ctk.CTkEntry(self, width=150)
        entry_password.insert(0, '********')
        entry_password.configure(state='disabled')
        entry_password.pack()

        btn_login = ctk.CTkButton(self, text="Выйти",
                                  command=exit_funct)  # authorization_function(entry_login, entry_password)
        btn_login.pack(pady=15)

        label_error = ctk.CTkLabel(self, text="", text_color='red')
        label_error.pack()


# Класс фрейма до авторизации
class ConfigPlaceCamFalse(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        # Задание названий "столбцов" таблицы данных камер
        name_cam = ctk.CTkLabel(self, text="Камера")
        address_cam = ctk.CTkLabel(self, text="IP-адрес камеры")
        password_cam = ctk.CTkLabel(self, text="Пароль")
        label_auto = ctk.CTkLabel(self, text_color='red', text='Для редактирования авторизуйтесь')
        label_auto.grid(column=3, row=0, padx=8)
        # Первая строка
        self.name_entry_1 = ctk.CTkEntry(self, justify='center')
        self.name_entry_1.insert(0, "CAM1")
        self.name_entry_1.configure(state=DISABLED)

        self.address_entry_1 = ctk.CTkEntry(self, justify='center')
        self.address_entry_1.configure(state=DISABLED)

        self.password_entry_1 = ctk.CTkEntry(self, justify='center')
        self.password_entry_1.configure(state=DISABLED)

        self.btn_change_1 = ctk.CTkButton(self, text="Сохранить изменения", state='disabled')
        # Вторая строка
        self.name_entry_2 = ctk.CTkEntry(self, justify='center')
        self.name_entry_2.insert(0, "CAM2")
        self.name_entry_2.configure(state=DISABLED)

        self.address_entry_2 = ctk.CTkEntry(self, justify='center')
        self.address_entry_2.configure(state=DISABLED)

        self.password_entry_2 = ctk.CTkEntry(self, justify='center')
        self.password_entry_2.configure(state=DISABLED)
        self.btn_change_2 = ctk.CTkButton(self, text="Сохранить изменения", state='disabled')
        # Третья строка
        self.name_entry_3 = ctk.CTkEntry(self, justify='center')
        self.name_entry_3.insert(0, "CAM3")
        self.name_entry_3.configure(state=DISABLED)

        self.address_entry_3 = ctk.CTkEntry(self, justify='center')
        self.address_entry_3.configure(state=DISABLED)

        self.password_entry_3 = ctk.CTkEntry(self, justify='center')
        self.password_entry_3.configure(state=DISABLED)

        self.btn_change_3 = ctk.CTkButton(self, text="Сохранить изменения", state='disabled')
        # Четвертая строка
        self.name_entry_4 = ctk.CTkEntry(self, justify='center')
        self.name_entry_4.insert(0, "CAM4")
        self.name_entry_4.configure(state=DISABLED)

        self.address_entry_4 = ctk.CTkEntry(self, justify='center')
        self.address_entry_4.configure(state=DISABLED)

        self.password_entry_4 = ctk.CTkEntry(self, justify='center')
        self.password_entry_4.configure(state=DISABLED)

        self.btn_change_4 = ctk.CTkButton(self, text="Сохранить изменения", state='disabled')

        # Кнопка записи сразу всех строк, возможности вносить изменения и загрузка данных из БД
        self.btn_change_all = ctk.CTkButton(self, text="Сохранить все", width=150, state='disabled',
                                            fg_color="#008000")

        self.btn_access = ctk.CTkButton(self, text="Внести изменения", fg_color="#A0522D", state='disabled')

        self.btn_load = ctk.CTkButton(self, text="Загрузить данные", state='disabled')
        self.btn_load = ctk.CTkButton(self, text="Загрузить данные", state='disabled')

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
        self.btn_change_all.grid(column=3, row=5, pady=20, padx=53)


# Класс фрейма после авторизации
class ConfigPlaceCamTrue(ctk.CTkFrame):
    def __init__(self, master):

        def func_for_first_cam():
            set_data_options_cam(self.name_entry_1.get(),
                                 self.address_entry_1.get(),
                                 self.password_entry_1.get())
            make_disable()

        def func_for_second_cam():
            set_data_options_cam(self.name_entry_2.get(),
                                 self.address_entry_2.get(),
                                 self.password_entry_2.get())
            make_disable()

        def func_for_third_cam():
            set_data_options_cam(self.name_entry_3.get(),
                                 self.address_entry_3.get(),
                                 self.password_entry_3.get())
            make_disable()

        def func_for_fourth_cam():
            set_data_options_cam(self.name_entry_4.get(),
                                 self.address_entry_4.get(),
                                 self.password_entry_4.get())
            make_disable()

        def func_for_all_cam():
            func_for_first_cam()
            func_for_second_cam()
            func_for_third_cam()
            func_for_fourth_cam()

        def make_disable():
            self.btn_change_1.configure(state='disabled')
            self.btn_change_2.configure(state='disabled')
            self.btn_change_3.configure(state='disabled')
            self.btn_change_4.configure(state='disabled')
            self.btn_load.configure(state='disabled')
            self.btn_change_all.configure(state='disabled')

        def make_changes():  # Функция кнопки внести изменения
            def func_btn():
                print(entry.get() == start_window.password_acc)
                if entry.get() == start_window.password_acc:
                    self.btn_change_1.configure(state=NORMAL)
                    self.btn_change_2.configure(state=NORMAL)
                    self.btn_change_3.configure(state=NORMAL)
                    self.btn_change_4.configure(state=NORMAL)
                    self.btn_load.configure(state=NORMAL)
                    self.btn_change_all.configure(state=NORMAL)
                    window_changes.destroy()
                else:
                    label_error = ctk.CTkLabel(window_changes, text="Неверный пароль", text_color='red')
                    label_error.pack()

            window_changes = ctk.CTk()
            window_changes.title("Внесение изменений")
            window_changes.geometry("200x200")
            window_changes.resizable(False, False)

            label = ctk.CTkLabel(window_changes, text="Подтвердите пароль")
            label.pack()

            entry = ctk.CTkEntry(window_changes)
            entry.pack()

            btn = ctk.CTkButton(window_changes, text="Подтвердить", command=func_btn)
            btn.pack()

            window_changes.mainloop()

        def load_data():
            work_with_config_cam_frame.load_data_bd("CAM1", self.address_entry_1, self.password_entry_1)
            work_with_config_cam_frame.load_data_bd("CAM2", self.address_entry_2, self.password_entry_2)
            work_with_config_cam_frame.load_data_bd("CAM3", self.address_entry_3, self.password_entry_3)
            work_with_config_cam_frame.load_data_bd("CAM4", self.address_entry_4, self.password_entry_4)
            make_disable()

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
        self.btn_change_1 = ctk.CTkButton(self, text="Сохранить изменения",
                                          command=func_for_first_cam)
        # Вторая строка
        self.name_entry_2 = ctk.CTkEntry(self, justify='center')
        self.name_entry_2.insert(0, "CAM2")
        self.name_entry_2.configure(state=DISABLED)

        self.address_entry_2 = ctk.CTkEntry(self, justify='center')
        self.password_entry_2 = ctk.CTkEntry(self, justify='center')
        self.btn_change_2 = ctk.CTkButton(self, text="Сохранить изменения",
                                          command=func_for_second_cam)
        # Третья строка
        self.name_entry_3 = ctk.CTkEntry(self, justify='center')
        self.name_entry_3.insert(0, "CAM3")
        self.name_entry_3.configure(state=DISABLED)

        self.address_entry_3 = ctk.CTkEntry(self, justify='center')
        self.password_entry_3 = ctk.CTkEntry(self, justify='center')
        self.btn_change_3 = ctk.CTkButton(self, text="Сохранить изменения",
                                          command=func_for_third_cam)
        # Четвертая строка
        self.name_entry_4 = ctk.CTkEntry(self, justify='center')
        self.name_entry_4.insert(0, "CAM4")
        self.name_entry_4.configure(state=DISABLED)

        self.address_entry_4 = ctk.CTkEntry(self, justify='center')
        self.password_entry_4 = ctk.CTkEntry(self, justify='center')
        self.btn_change_4 = ctk.CTkButton(self, text="Сохранить изменения",
                                          command=func_for_fourth_cam)

        # Кнопка записи сразу всех строк, возможности вносить изменения и загрузка данных из БД
        self.btn_change_all = ctk.CTkButton(self, text="Сохранить все", width=150, command=func_for_all_cam,
                                            fg_color="#008000", state='disabled',)

        self.btn_access = ctk.CTkButton(self, text="Внести изменения", fg_color="#A0522D", command=make_changes)

        self.btn_load = ctk.CTkButton(self, text="Загрузить данные", command=load_data)

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
        self.btn_change_all.grid(column=3, row=5, pady=20, padx=53)

        make_disable()


class ConfigWayRecords(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)

        self.frame_btn_entry = ctk.CTkFrame(self, fg_color='transparent')

        img = ctk.CTkImage(dark_image=Image.open('papka-transformed.png'), size=(15, 15))

        label_way = ctk.CTkLabel(self, text='Путь сохранения видеозаписей', padx=20, pady=20)
        entry_way = ctk.CTkEntry(self.frame_btn_entry, width=150)
        btn_way = ctk.CTkButton(self.frame_btn_entry, text='', width=30, image=img)
        btn_open_way = ctk.CTkButton(self, text='Открыть', width=30)

        label_way.pack(anchor=CENTER, padx=5)
        entry_way.grid(row=0, column=0, padx=15)
        btn_way.grid(row=0, column=1)
        self.frame_btn_entry.pack(anchor=W, pady=5)
        btn_open_way.pack(anchor=W, padx=15, pady=10)
