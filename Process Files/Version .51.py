import wx
import wx.lib.scrolledpanel


class GUI(wx.Frame):

    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title, size=(1200, 700), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        mainPanel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, style=wx.SIMPLE_BORDER)
        panel1 = wx.lib.scrolledpanel.ScrolledPanel(self, size=(800, 150), pos=(20, 50),
                                                    style=wx.SUNKEN_BORDER)
        panel1.SetBackgroundColour('#FFFFFF')

        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(800, 400), pos=(20, 200),
                                                    style=wx.BORDER_SUNKEN)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        bSizer = wx.BoxSizer(wx.VERTICAL)
        panel2.SetSizer(bSizer)

        panel3 = wx.lib.scrolledpanel.ScrolledPanel(self, size=(250, 400), pos=(840, 200), style=wx.SUNKEN_BORDER)
        panel3.SetBackgroundColour('#FFFFFF')
        panel3.SetupScrolling()
        panel3.SetSizer(bSizer)

        output_list = ["", "", ""]
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn1 = wx.Button(panel2, label="Remove", pos=(20, 20 + x), size=(80, 30))
            official_list1 = wx.ListBox(panel2, -1, (110, 10 + x), (500, 30), output_list, wx.LB_SINGLE)
            wx.Choice(panel2, -1, (650, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            bSizer.Add(remove_btn1, 0, wx.ALL, 5)
        official_list1

        y = 0
        y1 = 0
        self.cb_list = []
        for x in range(0, (len(output_list))):
            for i in range(0, (len(output_list))):
                cb = wx.CheckBox(panel3, -1, '', (10 + y1, 10 + y))
                cb.SetValue(False)
                self.cb_list.append(cb)
                y = y + 40
            y = 0
            y1 = y1 + 40

        process_button = wx.Button(panel1, label="Process", pos=(125, 50), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.process_button, process_button)

        done_button = wx.Button(panel1, label="Done", pos=(450, 50), size=(150, 40))
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
