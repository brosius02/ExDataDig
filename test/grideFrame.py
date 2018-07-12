import wx
import wx.lib.scrolledpanel as SP

output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]


class App(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(parent=None, title='Scrollbar Example', size=(1000, 600))
        self.panel = SP.ScrolledPanel(self.frame, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)

        p = SP.ScrolledPanel(self.panel, size=(600, 300), pos=(20, 200), style=wx.SUNKEN_BORDER)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        p.SetupScrolling()
        p.SetBackgroundColour('#FFFFFF')
        p.SetSizer(bSizer)
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn1 = wx.Button(p, label="Remove", pos=(20, 20 + x), size=(80, 30))
            official_list1 = wx.ListBox(p, -1, (110, 10 + x), (300, 30), output_list, wx.LB_SINGLE)
            wx.Choice(p, -1, (450, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            bSizer.Add(remove_btn1, 0, wx.ALL, 5)
        official_list1

        p1 = SP.ScrolledPanel(self.panel, size=(250, 300), pos=(620, 200), style=wx.SUNKEN_BORDER)
        p1.SetupScrolling()
        p1.SetBackgroundColour('#FFFFFF')
        p1.SetSizer(bSizer)
        # y = 0
        # y1 = 0
        # for i in range(0, (len(output_list))):
        #     self.checkbox_1 = wx.CheckBox(p1, label='', pos=(23 + y, 10))
        #     bSizer.Add(checkbox_1, 0, wx.ALL, 25)
        #     y = y + 50
        #
        # for i in range(0, (len(output_list))):
        #     self.checkbox_2 = wx.CheckBox(p1, label='', pos=(23, 40 + y1))
        #     bSizer.Add(checkbox_2, 0, wx.ALL, 25)
        #     y1 = y1 + 30

        self.p.Bind(wx.EVT_SCROLLWIN, self.onScrollWin2)
        self.p1.Bind(wx.EVT_SCROLLWIN, self.onScrollWin1)

    def onScrollWin1(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.p.grid.Scroll(event.Position, -1)
        else:
            self.p.grid.Scroll(-1, event.Position)
        event.Skip()

    def onScrollWin2(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.p1.grid.Scroll(event.Position, -1)
        else:
            self.p1.grid.Scroll(-1, event.Position)
        event.Skip()

        self.panel.SetSizer(vbox)
        self.panel.SetupScrolling()
        self.frame.Show()
        ScrollSync(p, p1)
        return True


class ScrollSync(object):
    def __init__(self, frame1, frame2):
        self.frame1 = frame1
        self.frame2 = frame2


if __name__ == '__main__':
    app = App(redirect=False)
    app.MainLoop()
