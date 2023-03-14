import PIL
import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import *
import cv2
from PIL import ImageTk, Image
import os
import numpy as np


class videoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.video_source = 0

        self.frame = ctk.CTkFrame(master)
        self.cam_1_vid = MyVideoCapture(self.video_source)

        self.canvas_cam1 = tk.Canvas(self.frame, width=764, height=430)
        self.canvas_cam1.grid(row=0, column=0)
        #self.canvas_cam2 = tk.Canvas(self.frame, width=764, height=430, bg='green')
        #elf.canvas_cam2.grid(row=0, column=1)
        #self.canvas_cam3 = tk.Canvas(self.frame, width=764, height=430, bg='green')
        #self.canvas_cam3.grid(row=1, column=0)
        #self.canvas_cam4 = tk.Canvas(self.frame, width=764, height=430, bg='green')
        #self.canvas_cam4.grid(row=1, column=1)

        self.delay = 100
        self.update()

        self.frame.pack(pady=20)

    def update(self):
        # Get a frame from the video source
        ret, frame = self.cam_1_vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame).resize((764, 430)))
            self.canvas_cam1.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.frame.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.height = self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None
        else:
            return ret, None

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

