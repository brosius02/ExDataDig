import wx


class buttons_buttons_Everywhere(wx.Panel):
    def __init__(self, child):
        wx.Panel.__init__(self, child,)
        # A button
        self.button = wx.Button(self, label="Remove", pos=(20, 200), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.logger = wx.TextCtrl(self, pos=(120, 200), size=(450, 30), style=wx.LB_SINGLE | wx.TE_READONLY)

        # the combobox Control
        self.sampleList = ['Glyphworks', 'CSV', 'gvi', 'asc', 'rdf', 'dtc']
        self.drop_down_box1 = wx.ComboBox(self, pos=(590, 200), size=(80, 35), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.drop_down_box1)

    def OnClick(self, event):
        self.logger.AppendText(" Cleared items %d\n" % event.GetId())

    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())


app = wx.App(False)
frame = wx.Frame(None)
panel = buttons_buttons_Everywhere(frame)
frame.Show()
app.MainLoop()
