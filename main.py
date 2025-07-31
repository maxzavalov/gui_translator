from ensurepip import bootstrap

import ttkbootstrap as ttk
from tkinter.messagebox import showerror
import googletrans
from googletrans import Translator
import pyttsx3
import pyperclip


class LanguageTranslator:
    def __init__(self, master):
        self.master = master
        self.widow_setup()
        self.widgets()
        self.logo = ttk.PhotoImage(file="translate-icon.png").subsample(7, 7)  # load image
        self.canvas.create_image(85, 80, image=self.logo)  # add image to canvas
        lang_data = googletrans.LANGUAGES  # getting all the languages
        lang_values = lang_data.values()  # getting all the language values using the values() function
        languages = list(lang_values)
        # first combobox for the source language
        self.from_lang = ttk.Combobox(self.canvas, width=36, bootstyle="primary", values=languages)
        self.from_lang.current(0)
        self.canvas.create_window(170,180, window=self.from_lang)
        # loading the arrow icon
        self.arrows_icon = ttk.PhotoImage(file="arrows.png").subsample(15, 15)
        self.arrows_label = ttk.Label(self.master, image=self.arrows_icon)
        self.canvas.create_window(350, 180, window=self.arrows_label)
        # the second combobox for the destination language
        self.to_lang = ttk.Combobox(self.canvas, width=36, values=languages)
        self.to_lang.current(21)
        self.canvas.create_window(530, 180, window=self.to_lang)


    def widow_setup(self):
        self.master.title("Translator")
        self.master.resizable(width=False, height=False)
        self.master.geometry("700x430+300+150")

    def widgets(self):
        # the canvas for containing the other widgets
        self.canvas = ttk.Canvas(self.master, bg="white", width=700, height=400)
        self.canvas.pack()


window = ttk.Window(themename='cosmo')
application = LanguageTranslator(window)
window.mainloop()
