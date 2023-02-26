import customtkinter
from tkinter import *


def set_text(entry, text):
    entry.delete(0, END)
    entry.insert(0, text)
