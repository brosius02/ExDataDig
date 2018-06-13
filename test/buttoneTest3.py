import wx


class creating_buttons(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button', size=(1000, 600))
        panel = wx.Panel(self)
        button = wx.Button(panel, label="exit", pos=(130, 10), size=(60, 60))
        self.Bind(wx.EVT_BUTTON, self.close_button, button)
        self.Bind(wx.EVT_CLOSE, self.close_window)

    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()


if __name__ == 'main':
    app = wx.PySimpleApp()
    frame = creating_buttons(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
