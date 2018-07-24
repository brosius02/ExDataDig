import wx

output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


class Page(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Processing Version .6", size=(950, 500))
        self.cb_list = []
        pannel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        ico = wx.Icon('john_deere.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

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
        space_between_boxes1 = 0
        space_between_boxes2 = 0
        space_between_boxes3 = 0
        space_between_boxes4 = 0
        process_hieght_location = 65 ###This controls the height of all of the attributes within the program.

        first_line = process_hieght_location
        second_line = 25 + process_hieght_location
        third_line = 50 + process_hieght_location
        fourth_line = 75 + process_hieght_location

        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]

        browse_button = wx.Button(page, label="Browse Button", pos=(10, process_hieght_location), size=(95, 30))
        self.Bind(wx.EVT_BUTTON, self.save_notes_button, browse_button)

        official_list1 = wx.ListBox(page, -1, (110, process_hieght_location), (500, 30),
                                    style=wx.TE_MULTILINE | wx.BORDER)

        wx.StaticBox(page, label='Available Machines', pos=(5, process_hieght_location + 40), size=(880, 125))
        wx.Choice(page, -1, (630, process_hieght_location), (90, 40), choices=sampleList)
        for i in range(0, (len(output_list))):
            if i < 10:
                cb = wx.CheckBox(page, -1, 'Machine ' + str(i + 1), (10 + space_between_boxes1, 60 + first_line))
                cb.SetValue(False)
                self.cb_list.append(cb)
                space_between_boxes1 += 85
            elif 10 <= i < 20:
                cb = wx.CheckBox(page, -1, 'Machine ' + str(i + 1), (10 + space_between_boxes2, 60 + second_line))
                cb.SetValue(False)
                self.cb_list.append(cb)
                space_between_boxes2 += 85
            elif 20 <= i < 30:
                cb = wx.CheckBox(page, -1, 'Machine ' + str(i + 1), (10 + space_between_boxes3, 60 + third_line))
                cb.SetValue(False)
                self.cb_list.append(cb)
                space_between_boxes3 += 85
            elif 30 <= i < 40:
                cb = wx.CheckBox(page, -1, 'Machine ' + str(i+ 1), (10 + space_between_boxes4, 60 + fourth_line))
                cb.SetValue(False)
                self.cb_list.append(cb)
                space_between_boxes4 += 85

        notes_process = wx.StaticText(page, -1, "Notes About This Process", pos=(30, process_hieght_location + 180),
                                      size=(100, 0))
        font = wx.Font(9, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        notes_process.SetFont(font)

        text_processor = wx.StaticText(page, -1, "Processor", pos=(635, process_hieght_location - 25),
                                       size=(100, 0))
        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font)

        process_text = wx.StaticText(page, -1, "Process", pos=(110, process_hieght_location - 25),
                                       size=(100, 0))
        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        process_text.SetFont(font)

        Detailed_Information = wx.ListBox(page, -1, (30, process_hieght_location + 195), (700, 100),
                                          style=wx.TE_MULTILINE | wx.BORDER)


    def onButtonRemove(self, event):
        page_to_delete = self.notebook3.GetSelection()
        self.notebook3.DeletePage(page_to_delete)

    def onButtonInsert(self, event):
        self.addPage()

    def onButtonDone(self, event):
        page = self.notebook3.GetCurrentPage()
        page.textCtrl.AppendText("Yeah this works ")

    def save_notes_button(self, event: object) -> object:
        """pretty much self evident, what do you think it means?"""


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
