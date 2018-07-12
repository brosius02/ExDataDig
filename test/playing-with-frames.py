import wx
import wx.lib.scrolledpanel as scrolled


class MyFrame(wx.Frame, scrolled.ScrolledPanel):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(1200, 750))

        panel1 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(800, 400), pos=(20, 200), style=wx.SIMPLE_BORDER)
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(300, 400), pos=(840, 200), style=wx.SIMPLE_BORDER)
        panel1.SetBackgroundColour("BLUE")
        panel2.SetBackgroundColour("RED")
        panel1.SetupScrolling()
        panel2.SetupScrolling()
        box = wx.BoxSizer(wx.VERTICAL)

        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()

        output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn = wx.Button(panel1, label="Remove", pos=(20, 11 + x), size=(80, 30))
            official_list1 = wx.ListBox(panel1, -1, (110, 10 + x), (500, 30), output_list, wx.LB_SINGLE)
            wx.Choice(panel1, -1, (650, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            box.Add(remove_btn, 0, wx.ALL, 5)
        official_list1

        y = 0
        for i in range(0, (len(output_list))):
            self.cb1 = wx.CheckBox(panel2, label='', pos=(20, 11 + y))
            y = y + 40


app = wx.PySimpleApp()
frame = MyFrame(None, -1, "Sizer Test")
frame.Show()
app.MainLoop()
