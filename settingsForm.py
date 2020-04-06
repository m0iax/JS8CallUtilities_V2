from tkinter import *

class SettingsDialog:

    def __init__(self, parent):

        top = Toplevel(parent)

        Label(top, text="Value").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        print ("value is", self.e.get())

        self.top.destroy()
