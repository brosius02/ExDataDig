import wx


class NameDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title="Enter Name!"):
        wx.Dialog.__init__(self, parent, id, title, size=(-1, -1))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.label = wx.StaticText(self, label="Enter Name:")
        self.field = wx.TextCtrl(self, value="", size=(300, 20))
        self.okbutton = wx.Button(self, label="OK", id=wx.ID_OK)

        self.mainSizer.Add(self.label, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.field, 0, wx.ALL, 8 )

        self.buttonSizer.Add(self.okbutton, 0, wx.ALL, 8 )

        self.mainSizer.Add(self.buttonSizer, 0, wx.ALL, 0)

        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOK)

        self.SetSizer(self.mainSizer)
        self.result = None

    def onOK(self, event):
        self.result = self.field.GetValue()
        self.Destroy()

    def onCancel(self, event):
        self.result = None
        self.Destroy()


class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.btn = wx.Button(self.panel, -1, "Name-a-matic")
        self.Bind(wx.EVT_BUTTON, self.GetName, self.btn)
        self.txt = wx.TextCtrl(self.panel, -1, size=(140,-1))
        self.txt.SetValue('name goes here')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn)
        sizer.Add(self.txt)

        self.panel.SetSizer(sizer)
        self.Show()

    def GetName(self, e):
        dlg = NameDialog(self)
        dlg.ShowModal()
        self.txt.SetValue(dlg.result)

    def OnCloseWindow(self, e):
        self.Destroy()


app = wx.App()
frame = Frame(None, 'My Nameomatic')
app.MainLoop()