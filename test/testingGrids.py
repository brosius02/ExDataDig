import wx
import wx.grid as gridlib

########################################################################
class MyForm(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, -1, 'Processing Layout Version .1', size=(800, 800))
        panel = wx.Panel(self)

        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(12, 8)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        languages = ['C', 'C++', 'Python', 'Java', 'Perl']
        # self.combo = wx.ComboBox(panel, choices=languages)
        # sizer.Add(self.combo, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        choice_editor = wx.grid.GridCellChoiceEditor(languages, True)
        myGrid.SetCellEditor(5, 3, choice_editor)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()