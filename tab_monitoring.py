import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import *
import cv2
from PIL import ImageTk, Image
import os
import numpy as np


class video_frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

