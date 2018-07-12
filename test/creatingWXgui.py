import os
import wx
import wx.lib.scrolledpanel

output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ''

        wx.Frame.__init__(self, parent, title=title, size=(1000, 400))
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.buttons1 = []
        panel3 = wx.lib.scrolledpanel.ScrolledPanel(self, size=(100, 600), pos=(100, 5), style=wx.SIMPLE_BORDER)
        panel3.SetBackgroundColour('#FFFFFF')
        x = 0
        for i in range(0, len(output_list)):###number of buttons
            self.buttons1.append(wx.Button(panel3, -1, "Remove Row " + str(i), pos=(20, 50 + x), size=(100, 30)))
            self.sizer2.Add(self.buttons1[i], 1, wx.ALL)
            x = x + 30

        # self.button2 = []
        # x = 0
        # for i in range(0, len(output_list)):###number of buttons
        #     self.buttons2.append(wx.Button(self, -1, "Remove Row " + str(i), pos=(20, 100 + x), size=(100, 30)))
        #     self.sizer2.Add(self.buttons2[i], 1, wx.ALL)
        #     x = x + 30
        # user some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Layouts
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        #self.sizer.Fit(self) ###You can user this to auto fit the program
        self.Show()

        text = wx.StaticText(panel3, -1, "Process", pos=(5, 10), size=(10, 10))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)


app = wx.App(False)
frame = MainWindow(None, "Sample editor")  # type: MainWindow
app.MainLoop()
