import wx
import wx.lib.scrolledpanel


class GUI(wx.Frame):

    def __init__(self, parent, id, title):
        # Create a frame
        wx.Frame.__init__(self, parent, id, title, size=(1200, 650))
        output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        machine_number = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
############################################
        # checkboxpanel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(250, 400), pos=(840, 200),
        #                                                    style=wx.SIMPLE_BORDER)
        # checkboxpanel.SetupScrolling()
        # checkboxpanel.SetBackgroundColour('#FFFFFF')
        # bSizer3 = wx.BoxSizer(wx.VERTICAL)
        # checkboxpanel.SetSizer(bSizer3)
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(1100, 400), pos=(20, 200),
                                                    style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        bSizer = wx.BoxSizer(wx.VERTICAL)
        panel2.SetSizer(bSizer)
        y = 0
        y1 = 0
        for i in range(0, (len(output_list))):
            self.cb1 = wx.CheckBox(panel2, label='', pos=(840, 11 + y))
            y = y + 40
            for z in range(0, (len(machine_number))):
                self.cb1 = wx.CheckBox(panel2, label='', pos=(840 + y, 11))
            y1 = y1 + 40
#############################################

        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn1 = wx.Button(panel2, label="Remove", pos=(20, 20 + x), size=(80, 30))
            official_list1 = wx.ListBox(panel2, -1, (110, 10 + x), (500, 30), output_list, wx.LB_SINGLE)
            wx.Choice(panel2, -1, (650, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            bSizer.Add(remove_btn1, 0, wx.ALL, 5)
        official_list1
#############################################
        panel1 = wx.lib.scrolledpanel.ScrolledPanel(self, size=(800, 150), pos=(20, 50),
                                                    style=wx.SIMPLE_BORDER)
        panel1.SetBackgroundColour('#FFFFFF')
        process_button = wx.Button(panel1, label="Process", pos=(225, 30), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.process_button, process_button)

        done_button = wx.Button(panel1, label="Done", pos=(400, 30), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.done_button, done_button)
        text_process = wx.StaticText(panel1, -1, "Process", pos=(50, 100), size=(260, -1))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_process.SetFont(font)
        text_processor = wx.StaticText(panel1, -1, "Processor", pos=(600, 100), size=(240, -1))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font)

    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()

    def process_button(self, event):
        """#something awesome happens here"""

    def done_button(self, event: object) -> object:
        """pretty much self evident, what do you think it means?"""


if __name__ == '__main__':
    app = wx.App()
    frame = GUI(parent=None, id=-1, title="Test")
    frame.Show()
    app.MainLoop()
