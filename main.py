import ttkbootstrap as ttk
from tkinter.messagebox import  showerror
import googletrans
from googletrans import Translator
import pyttsx3
import pyperclip


class LanguageTranslator:
    def __init__(self, master):
        self.master = master
        self.widow_setup()

    def widow_setup(self):
        self.master.title("Translator")
        self.master.resizable(width=False, height=False)
        self.master.geometry("600x430+300+150")
        icon = ttk.PhotoImage(file="translate-icon.png")
        self.master.iconphoto(False, icon)



window = ttk.Window(themename='cosmo')
application = LanguageTranslator(window)
window.mainloop()