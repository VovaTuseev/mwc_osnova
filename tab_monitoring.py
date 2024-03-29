import PIL
import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import *
import cv2
from PIL import ImageTk, Image
import os
import numpy as np
import threading
from threading import Thread
from multiprocessing import Pool


class videoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.video_source1 = 0
        self.video_source2 = 1

        self.frame = ctk.CTkFrame(master)

        self.vid1 = MyVideoCapture(self.video_source1, self.video_source2)

        self.canvas_cam1 = tk.Canvas(self.frame, width=764, height=430)
        self.canvas_cam1.grid(row=0, column=0)

        self.canvas_cam2 = tk.Canvas(self.frame, width=764, height=430)
        self.canvas_cam2.grid(row=0, column=1)

        # self.cam_3_vid = MyVideoCapture(self.video_source3)
        # self.cam_4_vid = MyVideoCapture(self.video_source4)

        self.delay = 100
        t1 = Thread(target=self.update, args=())
        t1.start()
        self.frame.pack(pady=20)

    def update(self):
        # Get a frame from the video source
        ret1, frame1, ret2, frame2 = self.vid1.get_frame()

        if ret1 and ret2:
            self.photo1 = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame1).resize((764, 430)))
            self.photo2 = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame2).resize((764, 430)))
            self.canvas_cam1.create_image(0, 0, image=self.photo1, anchor=tk.NW)
            self.canvas_cam2.create_image(0, 0, image=self.photo2, anchor=tk.NW)

        self.frame.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source1, video_source2):
        # Open the video source
        self.vid1 = cv2.VideoCapture(video_source1, cv2.CAP_DSHOW)
        self.vid2 = cv2.VideoCapture(video_source2, cv2.CAP_DSHOW)
        if not self.vid1.isOpened():
            raise ValueError("Unable to open video source", video_source1)

        # Get video source width and height
        self.width = self.vid1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.height = self.vid1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def get_frame(self):
        if self.vid1.isOpened():
            ret1, frame1 = self.vid1.read()
            ret2, frame2 = self.vid2.read()
            if ret1 and ret2:
                # Return a boolean success flag and the current frame converted to BGR
                return ret1, cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB), ret2, cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
            else:
                return ret1, None, ret2, None
        else:
            return ret1, None, ret2, None

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid1.isOpened():
            self.vid1.release()
        if self.vid2.isOpened():
            self.vid2.release()
