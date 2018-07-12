import wx
import wx.grid


class TestFrame(wx.Frame):
    rowLabels = ["1", "2", "3", "4", "5"]

    columnLabels = ["machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
                    "machine 8", "machine 9", "machine 10"]

    def __init__(self):
        wx.Frame.__init__(self, None, title="Grid Headers", size=(500, 200))
        grid = wx.grid.Grid(self)
        grid.CreateGrid(5, 5)
        for row in range(5):
            grid.setRowLabelValue(row, self.rowLabels[row])
            grid.setColLabelValue(row, self.columnLabels[row])
            for col in range(5):
                grid.SetCellValue(row, col,
                                  '(%s, %s)' % (self.rowLabels[row], self.columnLabels[col]))


if __name__ == '__main__':
    app = wx.PySimpleApp()
    TestFrame().Show()
    app.MainLoop()
