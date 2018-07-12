import wx


########################################################################
class MyPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.btns = 1

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.main_sizer)

        add_btn = wx.Button(self, label="Process", pos=(225, 600), size=(150, 40))
        add_btn.Bind(wx.EVT_BUTTON, self.add_button)

        done_button = wx.Button(self, label="Done", pos=(400, 600), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.done_button, done_button)
    # ----------------------------------------------------------------------

    def add_button(self, event):
        """"""
        new_btn = wx.Button(self, label="Remove %s" % self.btns, pos=(20, 20), size=(80, 30))
        new_btn.Bind(wx.EVT_BUTTON, self.remove_button)
        self.btns += 1
        self.main_sizer.Add(new_btn, 0, 0, wx.ALL, 5)
        # new_list_box = wx.ListBox(self, label="")
        self.main_sizer.Layout()

    # ----------------------------------------------------------------------


    def process_button(self, event):
        """#something awesome happens here"""

    def done_button(self, event):
        """pretty much self evident, what do you think it means?"""


########################################################################
class MyFrame(wx.Frame):
    """"""
    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Buttons", size=(1200, 700))
        panel = MyPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
