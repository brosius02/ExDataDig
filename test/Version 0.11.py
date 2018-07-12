import wx
import wx.grid as grd


class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Processing Layout Version .1', size=(1100, 600))
        panel = wx.Panel(self, -1)
        self.SetBackgroundColour('light grey')  ###Background color of form.
        grid = RightSideGrid(panel)
        grid.SetFocus()
        self.CentreOnScreen()

        ##########Labels
        text_process = wx.StaticText(panel, -1, "Process", (60, 170), (260, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_process.SetFont(font)
        text_processor = wx.StaticText(panel, -1, "Processor", (400, 170), (260, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font)

        ##The following is for the text box at the bottom
        output_list = [""]
        ###official_list is a generic term used to call the list box at the bottom of the screen and location
        official_list1 = wx.ListBox(panel, -1, (110, 200), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list2 = wx.ListBox(panel, -1, (110, 240), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list3 = wx.ListBox(panel, -1, (110, 280), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list4 = wx.ListBox(panel, -1, (110, 320), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list5 = wx.ListBox(panel, -1, (110, 360), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list6 = wx.ListBox(panel, -1, (110, 400), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list7 = wx.ListBox(panel, -1, (110, 440), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list8 = wx.ListBox(panel, -1, (110, 480), (500, 30), output_list, wx.LB_MULTIPLE)
        official_list1, official_list2, official_list3, official_list4, official_list5, official_list6, official_list7, official_list8.SetSelection(
            0)

        remove_btn1 = wx.Button(panel, label="Remove", pos=(20, 200), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn1)
        remove_btn2 = wx.Button(panel, label="Remove", pos=(20, 240), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn2)
        remove_btn3 = wx.Button(panel, label="Remove", pos=(20, 280), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn3)
        remove_btn4 = wx.Button(panel, label="Remove", pos=(20, 320), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn4)
        remove_btn5 = wx.Button(panel, label="Remove", pos=(20, 360), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn5)
        remove_btn6 = wx.Button(panel, label="Remove", pos=(20, 400), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn6)
        remove_btn7 = wx.Button(panel, label="Remove", pos=(20, 440), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn7)
        remove_btn8 = wx.Button(panel, label="Remove", pos=(20, 480), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn8)
        ###Drop Down menu
        # the combobox Control
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        wx.Choice(panel, -1, (650, 200), (90, 40), choices=sampleList)  # pos , then size
        wx.Choice(panel, -1, (650, 240), (90, 40), choices=sampleList)  # pos , then size
        wx.Choice(panel, -1, (650, 280), (90, 40), choices=sampleList)  # pos , then size
        wx.Choice(panel, -1, (650, 320), (90, 40), choices=sampleList)  # pos , then size
        wx.Choice(panel, -1, (650, 360), (90, 40), choices=sampleList)  # pos , then size
        wx.Choice(panel, -1, (650, 400), (90, 40), choices=sampleList)  # pos , then size
        wx.Choice(panel, -1, (650, 440), (90, 40), choices=sampleList)  # pos , then size
        wx.Choice(panel, -1, (650, 480), (90, 40), choices=sampleList)  # pos , then size
        ###Exit button location and determination

        process_button = wx.Button(panel, label="Process", pos=(225, 80), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.process_button, process_button)

        done_button = wx.Button(panel, label="Done", pos=(400, 80), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.done_button, done_button)

    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()

    def process_button(self, event):
        """#something awesome happens here"""

    def done_button(self, event: object) -> object:
        """pretty much self evident, what do you think it means?"""


class RightSideGrid(grd.Grid):  ###This grid is the display on the right side of the screen

    def __init__(self, parent):
        grd.Grid.__init__(self, parent, -1, pos=(810, 140), size=(250, 380))

        colLabels = {"machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                     "machine 8"}
        # myGrid = grd.Grid()
        self.CreateGrid(8, len(colLabels))
        self.RowLabelSize = 0
        self.ColLabelSize = 60
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self, 1, wx.EXPAND)
        # GetColLabelTextOrientation()

        attr = grd.GridCellAttr()
        attr.SetEditor(grd.GridCellBoolEditor())
        attr.SetRenderer(grd.GridCellBoolRenderer())

        for i in range(0, (len(colLabels))):  ###uses the number of grids depending on amount of items in colLabels
            self.SetColAttr(i, attr)
            self.SetColSize(i, 80)  ###sets column 0 size
            self.SetRowSize(i, 40)
            self.SetColLabelValue(i, "Machine " + str(i))

    def toggleCheckBox(self):
        self.cb.Value = not self.cb.Value
        self.afterCheckBox(self.cb.Value)


class MyApp(wx.App):
    def OnInit(self):
        frame = Main(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    app = wx.PySimpleApp()
    Main().Show()
    app.MainLoop()
