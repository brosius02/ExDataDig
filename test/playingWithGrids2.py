import wx
import wx.grid as grd


class MyForm(wx.Frame):

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, -1, 'Processing Layout Version .1', size=(270, 350))
        # grd.Grid.__init__(self, parent, -1, pos=(770, 80), size=(270, 350))
        panel = wx.Panel(self)

        colLabels = {"machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                     "machine 8", "machine 9", "machine 10", "machine 11"}
        myGrid = grd.Grid(panel)
        myGrid.CreateGrid(12, len(colLabels))
        myGrid.RowLabelSize = 0
        myGrid.ColLabelSize = 40

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        attr = grd.GridCellAttr()
        attr.SetEditor(grd.GridCellBoolEditor())
        attr.SetRenderer(grd.GridCellBoolRenderer())

        for i in range(0, (len(colLabels))):  ###uses the number of grids depending on amount of items in colLabels
            myGrid.SetColAttr(i, attr)
            myGrid.SetColSize(i, 40)  ###sets column 0 size
            myGrid.SetColLabelValue(i, "Machine " + str(i))


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
