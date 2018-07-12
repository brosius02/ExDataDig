#!/usr/bin/env python
import wx
import wx.lib.scrolledpanel


class GUI(wx.Frame):

    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, None, id, title, size=(1200, 700))
        panelsSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        mainPanel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(1200, 700), style=wx.SIMPLE_BORDER)

        panel1 = wx.lib.scrolledpanel.ScrolledPanel(mainPanel, -1, size=(1150, 400), pos=(20, 200), style=wx.BORDER_SUNKEN)

        panel1.SetupScrolling(scroll_x=False)
        panel1.SetBackgroundColour('#FFFFFF')
        # panel2.SetBackgroundColour('#FFFFFF')
        panelsSizer.Add(panel1, 1, wx.ALL)
        # panelsSizer.Add(panel2, 2, wx.ALL)

        output_list = ["", "", "", "", "", "", "", ""]
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn1 = wx.Button(panel1, label="Remove", pos=(20, 10 + x), size=(80, 30))
            official_list1 = wx.ListBox(panel1, -1, (110, 10 + x), (500, 30), output_list, wx.LB_SINGLE)
            wx.Choice(panel1, -1, (650, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            sizer1.Add(remove_btn1, 0, wx.ALL, 5)
        official_list1

        y = 0
        y1 = 0
        self.cb_list = []
        for x in range(0, (len(output_list))):
            for i in range(0, (len(output_list))):
                cb = wx.CheckBox(panel1, -1, '', (760 + y1, 10 + y))
                cb.SetValue(False)
                self.cb_list.append(cb)
                y = y + 40
            y = 0
            y1 = y1 + 40
        sizer1.Add(cb, 0, wx.ALL, 5)
        panel1.SetSizer(sizer1)


if __name__ == '__main__':
    app = wx.App()
    frame = GUI(parent=None, id=-1, title="Test")
    frame.Show()
    app.MainLoop()
