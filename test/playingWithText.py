import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(600, 200))
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, -1, style=wx.ALIGN_CENTER)
        txt1 = "Python GUI development"
        lbl.SetLabel(txt1)
        panel.SetSizer(box)

        self.Show()


app = wx.App()
Mywin(None, 'StaticText demo')
app.MainLoop()