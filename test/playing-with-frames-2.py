import wx
import wx.grid as grid


class Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Grid", size=(350, 250))
        self.grid = grid.Grid(self)
        self.grid.CreateGrid(20, 20)


class ScrollSync(object):
    def __init__(self, frame1, frame2):
        self.frame1 = frame1
        self.frame2 = frame2
        self.frame1.grid.Bind(wx.EVT_SCROLLWIN, self.onScrollWin1)
        self.frame2.grid.Bind(wx.EVT_SCROLLWIN, self.onScrollWin2)

    def onScrollWin1(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.frame2.grid.Scroll(event.Position, -1)
        else:
            self.frame2.grid.Scroll(-1, event.Position)
        event.Skip()

    def onScrollWin2(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.frame1.grid.Scroll(event.Position, -1)
        else:
            self.frame1.grid.Scroll(-1, event.Position)
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame1 = Frame(None)
    frame1.Show()
    frame2 = Frame(None)
    frame2.Show()
    ScrollSync(frame1, frame2)
    app.MainLoop()