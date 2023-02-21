import customtkinter
from customtkinter import *
import customtkinter as ctk
from customtkinter import *
from tkcalendar import Calendar
import tkinter
import datetime
import os


class MyFrameView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.left_frame = Left_f(master)


class Left_f(ctk.CTkFrame):
    def __init__(self, master, **kwargs):

        global double_click_flag

        # Необходимые функции ------------------------------------------------------------------------------------------
        def set_text(text, e):  # Функция записи в текстовое поле
            e.delete(0, END)
            e.insert(0, text)
            return

        def get_current_info(entry):  # Функция получения позиции курсора в Entry
            return entry.index(INSERT)

        # ---------------------------------------------------------------------------------------------------------------
        super().__init__(master, **kwargs)
        self.now = datetime.datetime.now()

        self.combobox_frame = ctk.CTkFrame(master)
        self.period_frame = ctk.CTkFrame(master)
        self.ot_do_label = ctk.CTkFrame(master)
        self.ot_do_box = ctk.CTkFrame(master)
        self.cal_frame = ctk.CTkFrame(master)
        self.button_frame = ctk.CTkFrame(master)

        # Настройка скролллиста для выбора камеры !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Доделать после конфигурации
        combobox = ctk.CTkOptionMenu(self.combobox_frame)
        combobox.pack()

        # Настройка выбора даты (label и EntryBox)
        label_period = ctk.CTkLabel(self.period_frame, text="Временной интервал:")
        label_period.pack(anchor=W, padx=20, pady=10, ipadx=10, ipady=0)

        label_ot = ctk.CTkLabel(self.ot_do_label, text="От")
        label_ot.grid(column=0, row=0, padx=35, pady=0)

        label_do = ctk.CTkLabel(self.ot_do_label, text="До")
        label_do.grid(column=1, row=0, ipadx=105, pady=0)

        entry_ot = ctk.CTkEntry(self.ot_do_box, width=80)
        entry_ot.grid(column=0, row=0, padx=30, pady=5)

        entry_do = ctk.CTkEntry(self.ot_do_box, width=80)
        entry_do.grid(column=1, row=0, padx=45, pady=5)

        # Настройка календаря
        cal = Calendar(self.cal_frame, selectmode="day", year=self.now.year, month=self.now.month, day=self.now.day,
                       font="helvetica 12")
        cal.pack(anchor=W, padx=29, pady=20)

        # Настройка функций для работы с календарем---------------------------------------------------------------------
        def on_focus(evt):  # Функция для проверки фокуса курсора
            global current_entry
            current_entry = evt.widget

        entry_ot.bind('<FocusIn>', on_focus)
        entry_do.bind('<FocusIn>', on_focus)

        def grad_date(text_box):  # Функция получения даты
            DaTa = cal.get_date()
            set_text(DaTa, text_box)

        def on_click():  # Функция ввода даты в поля
            if current_entry is not None:
                try:
                    current_entry.insert('insert', grad_date(current_entry))
                except BaseException:
                    print('Norm')

        def mouse_click_1(event):  # Функция одиночного нажатия
            entry_ot.after(300, mouse_action, event)

        def mouse_click_2(event):
            entry_ot.after(300, mouse_action, event)

        def double_click(event):  # Функция обработки двойного нажатия
            global double_click_flag
            double_click_flag = True

        def mouse_action(event):  # Функция вызова других функций при нажатии
            global double_click_flag
            if double_click_flag:
                on_click()
                double_click_flag = False

        entry_ot.bind('<Button-1>', mouse_click_1)
        entry_ot.bind('<Double-1>', double_click)
        entry_do.bind('<Button-1>', mouse_click_2)
        entry_do.bind('<Double-1>', double_click)

        # Настройка кнопок выбора дат ----------------------------------------------------------------------------------
        btn_now = ctk.CTkButton(self.button_frame, text="Сегодня", width=115)
        btn_yest = ctk.CTkButton(self.button_frame, text="Вчера", width=115)
        btn_week = ctk.CTkButton(self.button_frame, text="Прошлая неделя", width=115)
        btn_month = ctk.CTkButton(self.button_frame, text="Прошлый месяц", width=115)

        btn_now.grid(column=0, row=0, padx=20, pady=5)
        btn_yest.grid(column=1, row=0, padx=5, pady=5)
        btn_week.grid(column=0, row=1, padx=5, pady=5)
        btn_month.grid(column=1, row=1, padx=5, pady=5)

        # Настройка label list
        self.label_list_frame = ctk.CTkFrame(master)
        label_list = ctk.CTkLabel(self.label_list_frame, text="Список видеозаписей")
        label_list.pack(anchor=W, padx=20, pady=5)

        self.period_frame.pack(anchor=W)
        self.ot_do_label.pack(anchor=W)
        self.ot_do_box.pack(anchor=W)
        self.cal_frame.pack(anchor=W)
        self.button_frame.pack(anchor=W)
        self.label_list_frame.pack(anchor=W)
