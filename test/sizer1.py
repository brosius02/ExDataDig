import wx


class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Button Example',
                          size=(300, 300))
        panel = wx.Panel(self, -1)
        self.radio = wx.RadioButton(panel, -1, "Accept user agreement", pos=(50, 10))
        self.button = wx.Button(panel, -1, "Run", pos=(50, 30))
        self.Bind(wx.EVT_BUTTON, self.OnRun, self.button)
        self.button.SetDefault()
        self.btn2 = wx.Button(panel, -1, "Walk", pos=(150, 30))
        self.Bind(wx.EVT_BUTTON, self.OnWalk, self.btn2)

    def OnRun(self, event):
        if not self.CheckRadio():
            return
        self.button.SetLabel("Running")

    def OnWalk(self, event):
        if not self.CheckRadio():
            return
        self.btn2.SetLabel("Walking")

    def CheckRadio(self):
        accepted = self.radio.GetValue()
        if not accepted:
            dlg = wx.MessageDialog(None, 'First accept the user agreement', 'MessageDialog', wx.OK | wx.ICON_QUESTION)
            result = dlg.ShowModal() # result not used in this demo
            dlg.Destroy()
            return False
        else:
            return True


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()