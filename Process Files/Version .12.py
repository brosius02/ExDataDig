import wx
import wx.lib.scrolledpanel
import wx.grid as grd


class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Processing Layout Version .1', size=(1200, 600))
        panel = wx.Panel(self, -1)
        self.SetBackgroundColour('light grey')  ###Background color of form.
        grid = RightSideGrid(panel)
        grid.SetFocus()
        self.CentreOnScreen()

        ##########Labels
        text_process = wx.StaticText(panel, -1, "Process", (60, 170), (260, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_process.SetFont(font)
        text_processor = wx.StaticText(panel, -1, "Processor", (570, 170), (240, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        ##The following is for the text box at the bottom
        output_list = ["", "", "", "", "", "", "", ""]
        # x = 0
        # for i in range(0, (len(output_list))):
        #     ###official_list is a generic term used to call the list box at the bottom of the screen and location
        #     official_list1 = wx.ListBox(panel, -1, (110, 200 + x), (500, 30), output_list, wx.LB_SINGLE)
        #     remove_btn1 = wx.Button(panel, label="Remove", pos=(20, 200 + x), size=(80, 30))
        #     self.Bind(wx.EVT_BUTTON, self.close_button, remove_btn1)
        #     ###Drop Down menu
        #     # the combobox Control
        #     sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        #     wx.Choice(panel, -1, (650, 200 + x), (90, 40), choices=sampleList)  # pos , then size
        #     x = x + 40
        #
        # official_list1
        #############################################
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(200, 400), pos=(10, 200),
                                                    style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        panel2.SetSizer(bSizer)
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn1 = wx.Button(panel2, label="Remove", pos=(20, 25 + x), size=(80, 30))
            official_list1 = wx.ListBox(panel2, -1, (110, 5 + x), (500, 30), output_list, wx.LB_SINGLE)
            wx.Choice(panel2, -1, (650, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            bSizer.Add(remove_btn1, 0, wx.ALL, 5)
        official_list1
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

    def __init__(self, Parent):
        grd.Grid.__init__(self, Parent, -1, pos=(860, 140), size=(250, 380))
        rowLabels = {"machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                     "machine 8"}
        colLabels = {"machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                     "machine 8"}
        # myGrid = grd.Grid()
        self.CreateGrid(len(colLabels), len(rowLabels))
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
