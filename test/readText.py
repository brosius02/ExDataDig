import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.state = 'Yes'
        self.panel = wx.Panel(self)
        self.status = wx.StaticText(self.panel, label=self.state, pos=(95, 5), size=(50, 20))
        self.button = wx.Button(self.panel, label='Change', pos=(115, 45), size=(50, 20))
        self.Bind(wx.EVT_BUTTON, self.changed, self.button)

    def changed(self, event):
        self.state = 'Yes' if self.state == 'No' else 'No'
        self.status.SetLabel(self.state)


app = wx.App(False)
frame = MyFrame(None, "Hello")
frame.Show()
app.MainLoop()
