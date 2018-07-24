"""Instructions of layout
    1) panel1: Is the panel that runs the remove, dropdown window
    2) panel2: Is the panel that runs the Process, buttons and labels
    3) panel 4: Is the panel that has the grid layout on the right"""

import wx
import wx.lib.scrolledpanel
import wx.grid as grd

######################These are place holders for the for loops.
output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
colLabels = {"machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
             "machine 8", "machine 9", "machine 10", "machine 11", "machine 12", "machine 13", "machine 14"}
######################


class MyGrid(grd.Grid):#############Grid Class for the right side of the screen
    def __init__(self, Child):
        grd.Grid.__init__(self, Child, -1, size=(250, 460))
        self.EnableGridLines(enable=False)
        self.CreateGrid(len(output_list), len(colLabels))
        self.RowLabelSize = 0
        self.ColLabelSize = 60

        attr = grd.GridCellAttr()  # type: GridCellAttr
        attr.SetEditor(grd.GridCellBoolEditor())
        attr.SetRenderer(grd.GridCellBoolRenderer())

        # digital

        for i in range(0, (len(colLabels))):  ###uses the number of grids depending on amount of items in colLabels
            self.SetColAttr(i, attr)
            self.SetRowSize(i, 40)
            self.SetColSize(i, 80)  ###sets column 0 size
            self.SetColLabelValue(i, "Machine " + str(i))

        self.Bind(grd.EVT_GRID_CELL_LEFT_CLICK, self.onMouse)
        self.Bind(grd.EVT_GRID_SELECT_CELL, self.onCellSelected)
        self.Bind(grd.EVT_GRID_EDITOR_CREATED, self.onEditorCreated)

    def onMouse(self, evt):
        if evt.Col == 0:
            wx.CallLater(100, self.toggleCheckBox)
        evt.Skip()

    def toggleCheckBox(self):
        self.cb.Value = not self.cb.Value
        self.afterCheckBox(self.cb.Value)

    def onCellSelected(self, evt):
        if evt.Col == 1:
            wx.CallAfter(self.EnableCellEditControl)
        evt.Skip()

    def onEditorCreated(self, evt):
        if evt.Col == 1:
            self.cb = evt.Control
            self.cb.WindowStyle |= wx.WANTS_CHARS
            self.cb.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
            self.cb.Bind(wx.EVT_CHECKBOX, self.onCheckBox)
        evt.Skip()

    def onCheckBox(self, evt):
        self.afterCheckBox(evt.IsChecked())

    def afterCheckBox(self, isChecked):
        print('afterCheckBox', self.GridCursorRow, isChecked)


class GUI(wx.Frame):

    def __init__(self, parent, id, title):
        # Create a frame
        wx.Frame.__init__(self, parent, id, size=(1200, 650))

############################################ Grid on the right side of the frame
        panel4 = wx.Panel(self, -1, size=(250, 460), pos=(840, 140), style=wx.SIMPLE_BORDER)
        grid = MyGrid(panel4)
        grid.SetFocus()
        # self.CentreOnScreen()
############################################# Main Panel that has buttons and drop downs
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(800, 400), pos=(20, 200),
                                                    style=wx.SIMPLE_BORDER)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        panel2.SetSizer(bSizer)
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn1 = wx.Button(panel2, label="Remove", pos=(20, 20 + x), size=(80, 30))
            official_list1 = wx.ListBox(panel2, -1, (110, 10 + x), (500, 30), output_list, wx.LB_SINGLE)
            wx.Choice(panel2, -1, (650, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            bSizer.Add(remove_btn1, 0, wx.ALL, 5)
        official_list1
############################################# Process and done button panel
        panel1 = wx.lib.scrolledpanel.ScrolledPanel(self, size=(800, 150), pos=(20, 50),
                                                    style=wx.SIMPLE_BORDER)
        panel1.SetBackgroundColour('#FFFFFF')
        process_button = wx.Button(panel1, label="Process", pos=(225, 30), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.process_button, process_button)

        done_button = wx.Button(panel1, label="Done", pos=(400, 30), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.done_button, done_button)

        text_process = wx.StaticText(panel1, -1, "Process", pos=(50, 100), size=(260, -1))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_process.SetFont(font)
        text_processor = wx.StaticText(panel1, -1, "Processor", pos=(600, 100), size=(240, -1))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font)

    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()

    def process_button(self, event):
        """#something awesome happens here"""

    def done_button(self, event: object) -> object:
        """pretty much self evident, what do you think it means?"""


if __name__ == '__main__':
    app = wx.App()
    frame = GUI(parent=None, id=-1, title="Test")
    frame.Show()
    app.MainLoop()