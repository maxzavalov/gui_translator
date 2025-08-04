from ensurepip import bootstrap

import ttkbootstrap as ttk
from tkinter.messagebox import showerror
import googletrans
from googletrans import Translator
import pyttsx3
import pyperclip


translator = Translator()
engine = pyttsx3.init()


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
        self.canvas.create_window(170, 170, window=self.from_lang)
        # loading the arrow icon
        self.arrows_icon = ttk.PhotoImage(file="arrows.png").subsample(15, 15)
        self.arrows_label = ttk.Label(self.master, image=self.arrows_icon)
        self.canvas.create_window(350, 170, window=self.arrows_label)
        # the second combobox for the destination language
        self.to_lang = ttk.Combobox(self.canvas, width=36, values=languages)
        self.to_lang.current(21)
        self.canvas.create_window(530, 170, window=self.to_lang)
        # scrollable text for entering input
        self.from_text_field = ttk.ScrolledText(self.master, font=("Helvetica", 10), width=30, height=10)
        self.canvas.create_window(170, 310, window=self.from_text_field)
        # scrollable text for output
        self.to_text_field = ttk.ScrolledText(self.master, font=("Helvetica", 10), width=30, height=10)
        self.canvas.create_window(530, 310, window=self.to_text_field)
        # loading icons
        self.speaker_icon = ttk.PhotoImage(file='speaker.png').subsample(5, 4)
        self.copy_icon = ttk.PhotoImage(file='copy.png').subsample(5, 4)
        self.speak_button = ttk.Button(self.master, image=self.speaker_icon, bootstyle='secondary', state=ttk.DISABLED)
        self.canvas.create_window(400, 435, window=self.speak_button)
        self.copy_button = ttk.Button(self.master, image=self.copy_icon, bootstyle='secondary', state=ttk.DISABLED)
        self.canvas.create_window(450, 435, window=self.copy_button)
        self.translate_button = ttk.Button(self.master, text="TRANSLATE", width=20, bootstyle='primary')
        self.canvas.create_window(330, 480, window=self.translate_button)

    def widow_setup(self):
        self.master.title("Translator")
        self.master.resizable(width=False, height=False)
        self.master.geometry("700x500+300+150")

    def widgets(self):
        # the canvas for containing the other widgets
        self.canvas = ttk.Canvas(self.master, bg="white", width=700, height=500)
        self.canvas.pack()




window = ttk.Window(themename='cosmo')
application = LanguageTranslator(window)
window.mainloop()
