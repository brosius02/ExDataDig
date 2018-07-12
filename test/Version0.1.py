import wx
import wx.grid as grd
from wx.grid import GridCellAttr


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

        ###The following is for the text box at the bottom
        output_list = ["machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                       "machine 8", "machine 9", "machine 10", "machine 2", "machine 3", "machine 4", "machine 5",
                       "machine 6", "machine 7", "machine 8", "machine 9", "machine 10"]
        ###official_list is a generic term used to call the list box at the bottom of the screen and location
        official_list = wx.ListBox(panel, -1, (50, 200), (700, 400), output_list, wx.LB_MULTIPLE)
        official_list.SetSelection(0)
        ###Exit button location and determination
        exit_button = wx.Button(panel, label="Exit", pos=(880, 520), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.close_button, exit_button)
        self.Bind(wx.EVT_CLOSE, self.close_window)

        save_button = wx.Button(panel, label="Save", pos=(780, 520), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.save_button, save_button)

        process_button = wx.Button(panel, label="Process", pos=(225, 80), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.process_button, process_button)

        done_button = wx.Button(panel, label="Done", pos=(400, 80), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.done_button, done_button)

    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()

    def save_button(self, event):
        """Saves the information into a text document, that has not been created yet. Will Be called SavedData.txt"""

    def process_button(self, event):
        """#something awesome happens here"""

    def done_button(self, event: object) -> object:
        """pretty much self evident, what do you think it means?"""


class RightSideGrid(grd.Grid):  ###This grid is the display on the right side of the screen

    def __init__(self, parent):
        grd.Grid.__init__(self, parent, -1, pos=(770, 80), size=(270, 350))
        panel = wx.Panel(self)
        colLabels = {"machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                     "machine 8", "machine 9", "machine 10", "machine 11"}

        self.CreateGrid(10, len(colLabels))
        self.RowLabelSize = 0
        self.ColLabelSize = 40

        attr = grd.GridCellAttr()  # type: GridCellAttr
        attr.SetEditor(grd.GridCellBoolEditor())
        attr.SetRenderer(grd.GridCellBoolRenderer())

        for i in range(0, (len(colLabels))):  ###uses the number of grids depending on amount of items in colLabels
            self.SetColAttr(i, attr)
            self.SetColSize(i, 40)  ###sets column 0 size
            #grd.SetColLabelValue(i, "Machine " + str(i))

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
