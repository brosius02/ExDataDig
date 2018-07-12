import wx
output_list = ["", "", ""]


class Page(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Processing Panel Version .6", size=(1100, 400))
        self.cb_list = []
        pannel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonRemove = wx.Button(pannel, id=-1, label="Delete Process")
        self.buttonRemove.Bind(wx.EVT_BUTTON, self.onButtonRemove)
        hbox.Add(self.buttonRemove)

        self.buttonInsert = wx.Button(pannel, id=-1, label="Create Process")
        self.buttonInsert.Bind(wx.EVT_BUTTON, self.onButtonInsert)
        hbox.Add(self.buttonInsert)

        self.buttonDone = wx.Button(pannel, id=-1, label="Done")
        self.buttonDone.Bind(wx.EVT_BUTTON, self.onButtonDone)
        hbox.Add(self.buttonDone)

        vbox.Add(hbox, 0, wx.ALL, 7)

        self.notebook3 = wx.Notebook(pannel)
        vbox.Add(self.notebook3, 1, wx.EXPAND | wx.ALL, 7)

        pannel.SetSizer(vbox)

        self.pageCounter = 0
        self.addPage()

    def addPage(self):
        self.pageCounter += 1
        page = Page(self.notebook3)
        pageTitle = "Process: {0}".format(str(self.pageCounter))
        self.notebook3.AddPage(page, pageTitle)
        y = 0
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        official_list1 = wx.ListBox(page, -1, (30, 10 + y), (500, 30), output_list, wx.LB_SINGLE)
        official_list1
        wx.Choice(page, -1, (550, 10 + y), (90, 40), choices=sampleList)
        for i in range(0, (len(output_list))):
            cb = wx.CheckBox(page, -1, 'Machine ' + str(i), (10 + y, 60))
            cb.SetValue(False)
            self.cb_list.append(cb)
            y = y + 100

        Detailed_Information = wx.ListBox(page, -1, (30, 150), (700, 100), style=wx.TE_MULTILINE | wx.BORDER)
        Detailed_Information

    def onButtonRemove(self, event):
        page_to_delete = self.notebook3.GetSelection()
        self.notebook3.DeletePage(page_to_delete)

    def onButtonInsert(self, event):
        self.addPage()

    def onButtonDone(self, event):
        page = self.notebook3.GetCurrentPage()
        page.textCtrl.AppendText("Yeah this works ")


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()