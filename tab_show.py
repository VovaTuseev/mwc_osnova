from pathlib import Path
import cv2
import customtkinter as ctk
from customtkinter import *
from tkcalendar import Calendar
import tkinter
import datetime
import os
from tkVideoPlayer import TkinterVideo
import start_window


class MyFrameView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.left_frame = fullFrameShow(master)


class fullFrameShow(ctk.CTkFrame):
    def __init__(self, master, **kwargs):

        global double_click_flag

        # Необходимые функции ------------------------------------------------------------------------------------------
        def set_text(text, e):  # Функция записи в текстовое поле
            e.delete(0, END)
            e.insert(0, text)
            return

        def get_current_info(entry):  # Функция получения позиции курсора в Entry
            return entry.index(INSERT)

        def check_entry():  # Функция корректировки введенных значений в поля дат
            try:
                if len(entry_do.get()) > 0 or len(entry_ot.get()) > 0:
                    list_data_ot = entry_ot.get().split('-')
                    list_data_do = entry_do.get().split('-')
                    a = int(list_data_ot[2]) > int(list_data_do[2])
                    b = int(list_data_ot[1]) > int(list_data_do[1]) and int(list_data_ot[2]) == int(list_data_do[2])
                    c = int(list_data_ot[2]) == int(list_data_do[2]) and int(list_data_ot[1]) == int(list_data_do[1]) \
                        and int(list_data_ot[0]) > int(list_data_do[0])
                    if a or b or c:
                        basket = entry_ot.get()
                        entry_ot.delete(0, END)
                        entry_ot.insert(0, entry_do.get())
                        entry_do.delete(0, END)
                        entry_do.insert(0, basket)
            except Exception:
                print("Исключение при смене дат")

        # --------------------------------------------------------------------------------------------------------------
        # Функции видеоплейера
        def update_duration(event):
            duration = vid_player.video_info()["duration"]
            label_end_vid["text"] = str(datetime.timedelta(seconds=duration))
            slider["to"] = duration

        def update_scale(event):
            progress_value.set(int(vid_player.current_duration()))
            label_start_vid.configure(text=str(datetime.timedelta(seconds=int(vid_player.current_duration()))))

        def play_pause():
            if vid_player.is_paused():
                vid_player.play()
                btn_pause.configure(text="Pause")

            else:
                vid_player.pause()
                btn_pause.configure(text="Play")

        def load_video(event):
            def start_vid():
                file_path = str(start_window.path_video) + chr(92) + str(list_box.selection_get())

                def with_ffprobe(filename):
                    DATA = cv2.VideoCapture(file_path)
                    frames = DATA.get(cv2.CAP_PROP_FRAME_COUNT)
                    fps = DATA.get(cv2.CAP_PROP_FPS)
                    seconds = round(frames / fps)
                    video_time = datetime.timedelta(seconds=seconds)
                    label_end_vid.configure(text=video_time)
                    list_time = str(video_time).split(':')
                    for item in list_time:
                        if item[0] == '0':
                            item.replace(item[0], '')
                    if len(list_time[0]) != 0:
                        start_window.second_video += int(list_time[0]) * 3600
                    if len(list_time[1]) != 0:
                        start_window.second_video += int(list_time[1]) * 60
                    if len(list_time[0]) != 0:
                        start_window.second_video += int(list_time[2])

                with_ffprobe(file_path)

                if file_path:
                    vid_player.load(file_path)
                    slider.configure(from_=0, to=start_window.second_video)
                    btn_pause["text"] = "Play"
                    progress_value.set(0)
                    play_pause()
                    start_window.flag_load_video = True

            if start_window.flag_load_video is False:
                start_window.flag_load_video = True
                start_vid()
            else:
                vid_player.stop()
                start_window.flag_load_video = False

        def seek(value):
            """ used to seek a specific timeframe """
            vid_player.seek(int(value))

        def skip(value: int):
            """ skip seconds """
            vid_player.seek(int(slider.get()) + value)
            progress_value.set(int(slider.get()) + value)

        def video_ended(event):
            """ handle video ended """
            # slider.set(slider["to"])
            btn_pause.configure(text="Play")
            slider.set(0)

        # --------------------------------------------------------------------------------------------------------------
        super().__init__(master, **kwargs)

        font = ctk.CTkFont(family='Arial', size=14)
        font_btn = ctk.CTkFont(size=13)
        now = datetime.datetime.now()

        self.leftSide = ctk.CTkFrame(master)  # Фрейм с выбором необходимого видео
        self.up_cal = ctk.CTkFrame(self.leftSide, fg_color='transparent')  # Фрейм над календарем
        self.btn_frame = ctk.CTkFrame(self.leftSide, fg_color='transparent')  # Фрейм кнопок выбора дат

        label_cam = ctk.CTkLabel(self.leftSide, text="Выбор камеры", font=font)
        label_cam.pack(anchor=CENTER, pady=5)

        def option_menu_callback(choice):  # Функция выбора камеры
            list_box.delete(0, list_box.size())
            start_window.number_cam = choice
            path1 = Path("folder_records", str(start_window.number_cam))
            start_window.path_video = path1
            myList = os.listdir(path=path1)
            for name in myList:
                list_box.insert('end', name)

        combobox = ctk.CTkOptionMenu(self.leftSide, values=['CAM1', 'CAM2', 'CAM3', 'CAM4'],
                                     command=option_menu_callback)
        combobox.pack(anchor=CENTER, pady=5)

        # Настройка выбора даты (label и EntryBox)
        label_period = ctk.CTkLabel(self.leftSide, text="Временной интервал:", font=font)
        label_period.pack(anchor=CENTER, padx=20, pady=5, ipadx=10)

        label_ot = ctk.CTkLabel(self.up_cal, text="От", font=font)
        label_ot.grid(column=0, row=0, padx=0, pady=0)

        label_do = ctk.CTkLabel(self.up_cal, text="До", font=font)
        label_do.grid(column=1, row=0, padx=0, pady=0)

        entry_ot = ctk.CTkEntry(self.up_cal, width=100, justify='center')
        entry_ot.grid(column=0, row=1, padx=20, pady=5)

        entry_do = ctk.CTkEntry(self.up_cal, width=100, justify='center')
        entry_do.grid(column=1, row=1, padx=20, pady=5)

        self.up_cal.pack(anchor=CENTER)
        # Настройка календаря
        cal = Calendar(self.leftSide, selectmode="day", year=now.year, month=now.month, day=now.day,
                       font="helvetica 12", date_pattern='dd-mm-yy')
        cal.pack(anchor=W, padx=29, pady=20)

        # Настройка функций для работы с календарем---------------------------------------------------------------------
        def on_focus(evt):  # Функция для проверки фокуса курсора
            global current_entry
            current_entry = evt.widget

        def grad_date(text_box):  # Функция получения даты
            DaTa = cal.get_date()
            set_text(DaTa, text_box)

        def on_click():  # Функция ввода даты в поля
            if current_entry is not None:
                try:
                    current_entry.insert('insert', grad_date(current_entry))
                except BaseException:
                    print('Ввод данных в поля дат')

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
                check_entry()

        entry_ot.bind('<FocusIn>', on_focus)
        entry_do.bind('<FocusIn>', on_focus)

        entry_ot.bind('<Button-1>', mouse_click_1)
        entry_ot.bind('<Double-1>', double_click)
        entry_do.bind('<Button-1>', mouse_click_2)
        entry_do.bind('<Double-1>', double_click)

        # Настройка кнопок выбора дат ----------------------------------------------------------------------------------
        btn_now = ctk.CTkButton(self.btn_frame, text="Сегодня", width=115, font=font_btn)
        btn_yest = ctk.CTkButton(self.btn_frame, text="Вчера", width=115, font=font_btn)
        btn_week = ctk.CTkButton(self.btn_frame, text="Прошлая неделя", width=115, font=font_btn)
        btn_month = ctk.CTkButton(self.btn_frame, text="Прошлый месяц", width=115, font=font_btn)

        btn_now.grid(column=0, row=0, padx=5, pady=10)
        btn_yest.grid(column=1, row=0, padx=5)
        btn_week.grid(column=0, row=1)
        btn_month.grid(column=1, row=1)
        self.btn_frame.pack(anchor=CENTER)

        # Настройка label list
        self.label_list_frame = ctk.CTkFrame(master)
        label_list = ctk.CTkLabel(self.leftSide, text="Список видеозаписей", font=font)
        label_list.pack(anchor=CENTER, pady=5)

        font1 = CTkFont(size=19)

        list_box = tkinter.Listbox(self.leftSide, font=font1, width=26)
        list_box.bind('<Double-1>', load_video)
        list_box.pack(anchor=CENTER, pady=15)
        self.leftSide.pack(anchor=NW, side=LEFT, padx=30, pady=5)

        # --------------------------------------------------------------------------------------------------------------
        # Настройка видеоплейера
        self.frame_videoplayer = ctk.CTkFrame(master)

        video_frame = ctk.CTkFrame(self.frame_videoplayer, fg_color='transparent')  # Рамка для видео

        vid_player = TkinterVideo(master=video_frame, background='#212121',
                                  scaled=True, consistant_frame_rate=True, keep_aspect=True)  # height=45, width=150
        vid_player.set_size(size=(1320, 743))
        vid_player.pack(expand=True, fill='both', padx=20, pady=20)

        video_frame.configure(width=1800, height=625)

        video_btn = ctk.CTkFrame(self.frame_videoplayer)  # Рамка для кнопок
        slider_frame = ctk.CTkFrame(self.frame_videoplayer)  # Рамка для ползунка

        #  Кнопки работы с видео
        btn_skip_minus_10 = ctk.CTkButton(video_btn, text="-10", width=50, command=lambda: skip(-10))
        btn_skip_plus_10 = ctk.CTkButton(video_btn, text="+10", width=50, command=lambda: skip(10))

        btn_pause = ctk.CTkButton(video_btn, text="Play", width=70, command=play_pause)
        btn_skip_minus_min = ctk.CTkButton(video_btn, text="-60", command=lambda: skip(-60))
        btn_skip_plus_min = ctk.CTkButton(video_btn, text="+60", command=lambda: skip(60))

        # Ползунок
        progress_value = tkinter.IntVar(slider_frame)
        label_start_vid = ctk.CTkLabel(slider_frame, text=str(datetime.timedelta(seconds=0)))
        label_end_vid = ctk.CTkLabel(slider_frame, text=start_window.second_video)
        slider = ctk.CTkSlider(slider_frame, from_=0, to=100, width=400, variable=progress_value, command=seek)

        # vid_player.bind("<<Loaded>>", update_load)
        vid_player.bind("<<Duration>>", update_duration)
        vid_player.bind("<<SecondChanged>>", update_scale)
        vid_player.bind("<<Ended>>", video_ended)

        # Настройка позиционирования кнопок
        btn_skip_minus_min.pack(side=LEFT, padx=5)
        btn_skip_minus_10.pack(side=LEFT, padx=5)
        btn_pause.pack(side=LEFT)
        btn_skip_plus_10.pack(side=LEFT, padx=5)
        btn_skip_plus_min.pack(side=LEFT, padx=5)

        label_start_vid.pack(side=LEFT, padx=10)
        slider.pack(side=LEFT)
        label_end_vid.pack(side=LEFT, padx=10)

        video_frame.pack()
        video_frame.pack_propagate(False)  # (anchor=CENTER, expand=True, fill='both')
        video_btn.pack(anchor=CENTER)
        slider_frame.pack(anchor=CENTER, pady=15)
        self.frame_videoplayer.pack(anchor=NE, side=RIGHT, padx=40, pady=5)
        # self.video_frame.pack(anchor=NE, side=RIGHT, padx=100, pady=5)
        # self.video_frame.place(x=400, y=200)
