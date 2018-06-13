from tkinter import *

class Applicatoin(Frame):
    def _inti_(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text="Enter password for the secrete of learning to use Python")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.pw_lbl = Label(self, text = "Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)

        self.pw_ent = Entry(self)
