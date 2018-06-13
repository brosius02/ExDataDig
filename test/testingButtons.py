# Mad Lib
# Create a story based on user input
import wx
from tkinter import *

from wx import PySimpleApp


class Application(Frame):
    """ GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create a label for Process
        Label(self, text="Process: ", font=("Helvetica", 15)).grid(row=5, column=0, sticky=W)

        # create a label for Process
        Label(self, text="Processor:", font=("Helvetica", 15)).grid(row=5, column=2, sticky=W)

        # create a label for check boxes
        Label(self, text="Choose Machines:", font=("Helvetica", 12)).grid(row=1, column=4, sticky=W)

        # create check box 1
        self.is_machine1 = BooleanVar()
        Checkbutton(self, text="machine 1", variable=self.is_machine1).grid(row=2, column=4, sticky=W)

        # create check box 2
        self.is_machine2 = BooleanVar()
        Checkbutton(self, text="machine 2", variable=self.is_machine2).grid(row=3, column=4, sticky=W)

        # create check box 3
        self.is_machine3 = BooleanVar()
        Checkbutton(self, text="machine 3", variable=self.is_machine3).grid(row=4, column=4, sticky=W)


        # create variable for single machine
        self.machine_list = StringVar()
        self.machine_list.set(None)

        # create machine lists for check boxes work in progress
        machine_array_list = []
        column = 1
        for part in machine_array_list:
            Radiobutton(self, text=part, variable=self.machine_list, value=part).grid(row=5, column=column, sticky=W)
            column += 1

        # create a submit button
        Button(self, text="Add Process", font=("Helvetica", 12), command=self.process_information).grid(row=2, column=1,
                                                                                                        sticky=W)
        Button(self, text="      Done     ", font=("Helvetica", 12), command=self.complete_process_information())\
            .grid(row=2, column=2, sticky=W)

        self.machine_list_txt = Text(self, width=75, height=25, wrap=WORD)
        self.machine_list_txt.grid(row=10, column=0, columnspan=3)

    def process_information(self):
        """ Fill text box  user input. """

    def complete_process_information(self):
        """ Fill text box with user input. """


class ListBoxFrame(wx.Frame):
    def __init__(self):
        wx.frame__init__(self, None, -1, 'List Box Example', size=(250, 200))
        panel = wx.Panel(self, -1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']

        CheckListBox = wx.CheckListBox(panel, -1, (20, 20), (80, 120), sampleList, wx.LB_SINGLE)
        CheckListBox.SetSelection(3)

    if __name__ == '__main__':
        app = wx.PySimpleApp()  # type: PySimpleApp
        #ListBoxFrame().Show()
        app.MainLoop()


root = Tk()
root.title("GUI App Version .001")
app = Application(root)
root.mainloop()
