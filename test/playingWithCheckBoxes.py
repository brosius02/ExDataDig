from typing import Set

import wx


class TestPanel(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Processing Layout Version .002', size=(1000, 600))
        panel = wx.Panel(self, -1)
        ##########Labels
        text_process=wx.StaticText(panel, -1, "Process", (60, 170), (260, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_process.SetFont(font)
        text_processor = wx.StaticText(panel, -1, "Processor", (400, 170), (260, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font)
        the_machines = ("machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                        "machine 8", "machine 9", "machine 10", "machine 2", "machine 3", "machine 4", "machine 5",
                        "machine 6", "machine 7", "machine 8", "machine 9", "machine 10")

        theList = wx.CheckListBox(panel, -1, (780, 80), (200, 200), the_machines, wx.LB_SORT)
        theList.SetSelection(0)  # this selects the first number of the check box

        # self.machines = []
        # for i in range(0, 18):  ###number of boxes
        #     self.machines.append(wx.CheckListBox(self, -1, "machine &" + str(i)))
        #     self.sizer2.Add(self.machines[i], 1, wx.EXPAND)

        ###The following is for the text box at the bottom
        output_list = ["machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                       "machine 8", "machine 9", "machine 10", "machine 2", "machine 3", "machine 4", "machine 5",
                       "machine 6", "machine 7", "machine 8", "machine 9", "machine 10"]

        official_list = wx.ListBox(panel, -1, (50, 200), (700, 400), output_list, wx.LB_MULTIPLE)
        official_list.SetSelection(0)

        exit_button = wx.Button(panel, label="Exit", pos=(880, 520), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.close_button, exit_button)
        self.Bind(wx.EVT_CLOSE, self.close_window)

        process_button = wx.Button(panel, label="Process", pos=(225, 80), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.close_button, process_button)

        done_button = wx.Button(panel, label="Done", pos=(400, 80), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.close_button, done_button)

    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()

    def process_button(self, event):
        """#something awesome happens here"""

    def done_button(self, event: object) -> object:
        """pretty much self evident, what do you think it means?"""


if __name__ == '__main__':
    app = wx.PySimpleApp()
    TestPanel().Show()
    app.MainLoop()
