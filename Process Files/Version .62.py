import wx

output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", ""]  ##controls the amount of check boxes for available machines

dictionary = {}


class Page(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)


class MainFrame(wx.Frame):
    def __init__(self):
        #Controls the size of the frame
        wx.Frame.__init__(self, None, title="Processing Version .62", size=(950, 500))
        self.cb_list = []
        pannel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        ico = wx.Icon('john_deere.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        #The start of the buttons on the main panel
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
        #creates the page
        self.pageCounter += 1
        page = Page(self.notebook3)
        pageTitle = "Process: {0}".format(str(self.pageCounter))
        self.notebook3.AddPage(page, pageTitle)

        # Control the height of the objects within the GUI
        space_between_boxes1 = 0
        space_between_boxes2 = 0
        space_between_boxes3 = 0
        space_between_boxes4 = 0
        process_height_location = 45  ###This controls the height of all of the attributes within the program.
        static_box_width = 860
        first_line = process_height_location
        second_line = 25 + process_height_location
        third_line = 50 + process_height_location
        fourth_line = 75 + process_height_location

        # Process buttons and drop downs
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        browse_button = wx.Button(page, label="Browse Button", pos=(10, process_height_location), size=(95, 30))
        self.Bind(wx.EVT_BUTTON, self.onBrowse_button, browse_button)
        wx.ListBox(page, self.pageCounter, (110, process_height_location), (500, 30), style=wx.TE_MULTILINE | wx.BORDER)
        wx.Choice(page, self.pageCounter, (630, process_height_location), (90, 40), choices=sampleList)

        # Check Box locations and for loop
        if len(output_list) < 6:
            wx.StaticBox(page, label='Available Machines', pos=(5, process_height_location + 40),
                         size=(static_box_width / 2, 50), style=wx.BORDER_DEFAULT)
        elif 6 <= len(output_list) < 11:
            wx.StaticBox(page, label='Available Machines', pos=(5, process_height_location + 40),
                         size=(static_box_width, 50), style=wx.BORDER_DEFAULT)
        elif 11 <= len(output_list) < 21:
            wx.StaticBox(page, label='Available Machines', pos=(5, process_height_location + 40),
                         size=(static_box_width, 75), style=wx.BORDER_DEFAULT)
        elif 21 <= len(output_list) < 31:
            wx.StaticBox(page, label='Available Machines', pos=(5, process_height_location + 40),
                         size=(static_box_width, 100), style=wx.BORDER_DEFAULT)
        elif 31 <= len(output_list) < 41:
            wx.StaticBox(page, label='Available Machines', pos=(5, process_height_location + 40),
                         size=(static_box_width, 125), style=wx.BORDER_DEFAULT)
        #This sets the spacing and area for the first row of checkboxes
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
                cb = wx.CheckBox(page, -1, 'Machine ' + str(i + 1), (10 + space_between_boxes4, 60 + fourth_line))
                cb.SetValue(False)
                self.cb_list.append(cb)
                space_between_boxes4 += 85

        # Bottom part of the form. Notes
        notes_process = wx.StaticText(page, self.pageCounter, "Notes About This Process",
                                      pos=(15, process_height_location + 195), size=(100, 0))
        font_notes = wx.Font(9, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        notes_process.SetFont(font_notes)
        # Notes text box
        box = wx.TextCtrl(page, 1, pos=(5, process_height_location + 210), size=(860, 100),
                          style=wx.TE_MULTILINE | wx.BORDER_SIMPLE)
        # Text at the top of the notepad
        text_processor = wx.StaticText(page, -1, "Processor", pos=(635, process_height_location - 25), size=(100, 0))
        font_top_text = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font_top_text)

        process_text = wx.StaticText(page, -1, "Process", pos=(110, process_height_location - 25), size=(100, 0))
        process_text.SetFont(font_top_text)

    def onButtonRemove(self, event):
        page_to_delete = self.notebook3.GetSelection()
        self.notebook3.DeletePage(page_to_delete)

    def onButtonInsert(self, event):
        self.addPage()

    def onBrowse_button(self, event: object):
        """pretty much self evident, what do you think it means?"""

    def onButtonDone(self, event):
        """This represents the event for the done button."""


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()