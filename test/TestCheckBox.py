import wx


class MyCheckBox(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, 'Checking Options', size=(470, 400))
        panel = wx.Panel(self, -1)

        self.cb_list = []
        for pos in [(120,75), (200,75), (278,75), (356,75), (120,105), (200,105), (278,105), (356,105)]:
            cb = wx.CheckBox(panel, -1, '', pos)
            cb.SetValue(False)
            self.cb_list.append(cb)

        # wx.StaticText(panel, -1, "Send output to File", (70, 255))
        # self.cb = wx.CheckBox(panel, -1, '', (50, 255))
        # self.cb.SetValue(True)

        # wx.EVT_CHECKBOX(self, self.cb.GetId(), self.ShowTitle)

        # self.btnSelect = wx.Button(panel, label="Select All", pos=(45, 295))
        # self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id = self.btnSelect.GetId())
        #
        # self.btnUnSelectAll = wx.Button(panel, label="Unselect All*", pos=(173, 295))
        # self.Bind(wx.EVT_BUTTON, self.OnUnSelectAll, id = self.btnUnSelectAll.GetId())
        #
        # self.btnApply = wx.Button(panel, label="Apply/Close", pos=(305, 295))
        # self.Bind(wx.EVT_BUTTON, self.OnApply, id = self.btnApply.GetId())
        #
        # wx.StaticText(panel, -1, "* Note: 'Unselect All' button will not unselect storms that" '\n'
        #           "   have already determined", (20, 350))

        self.Show()
        # self.Centre()

    # def ShowTitle(self, event):
    #     if self.cb.GetValue():
    #         self.SetTitle('checkbox.py')
    #     else:
    #         self.SetTitle('')

    # def OnSelectAll(self, event):
    #     for cb in self.cb_list:
    #         cb.SetValue(True)

    # def OnUnSelectAll(self, event):
    #     for cb in self.cb_list:
    #         cb.SetValue(False)

    # def OnApply(self, event):
    #     selection = self.cb.GetValue()
    #     for i, cb in enumerate(self.cb_list):
    #         if cb.GetValue():
    #             print('{} selected'.format(i))


app = wx.App(0)
MyCheckBox(None, -1, 'checkbox.py')
app.MainLoop()