import wx


class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Button Example',
                          size=(300, 300))

        panel = wx.Panel(self, -1)

        self.dateLbl = wx.StaticBox(self, -1, 'Date Range:', size=(240, 140))
        self.dategraphSizer = wx.StaticBoxSizer(self.dateLbl, wx.VERTICAL)
        # self.dategraphSizer.Add(self.dateLbl, 0, wx.ALL|wx.LEFT, 5) NOTE THIS ISN'T NEEDED ANYMORE

        # Date Range Selection
        self.dateSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dateone = wx.TextCtrl(self, -1, style=wx.ALIGN_LEFT)
        self.datetwo = wx.TextCtrl(self, -1, style=wx.ALIGN_LEFT)
        self.date2Lbl = wx.StaticText(self, -1, "TO")
        self.dateSizer.Add(self.dateone, 0, wx.ALL | wx.CENTER, 2)
        self.dateSizer.Add(self.date2Lbl, 0, wx.ALL | wx.CENTER, 2)
        self.dateSizer.Add(self.datetwo, 0, wx.ALL | wx.CENTER, 2)

        # Date Quick Selection Buttons
        self.dategraphSizer.Add(self.dateSizer, 0, wx.ALL | wx.CENTER, 5)
        self.todayButton = wx.Button(self, -1, 'Today Only')
        self.dategraphSizer.Add(self.todayButton, 0, wx.ALL | wx.LEFT, 5)
        self.recentButton = wx.Button(self, -1, 'Most Recent Session')
        self.dategraphSizer.Add(self.recentButton, 0, wx.ALL | wx.LEFT, 5)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()