import wx
from wx.grid import Grid


class DragGridRowMixin:
    """This mixin allows the use of grid rows as drag sources, you can drag
    rows off of a grid to a text target.  Only row labels are draggable, internal
    cell contents are not.

    You must Initialize this class *after* the wxGrid initialization.
    example
    class MyGrid(Grid, DragGridRowMixin):
        def __init__(self, parent, id):
            Grid.__init__(self, parent, id)
            DragGridRowMixin.__init__(self)
    """
    def __init__(self):
        rowWindow = self.GetGridRowLabelWindow()
        # various flags to indicate whether we should have a select
        # event or a drag event
        self._potentialDrag = False
        self._startRow = None
        self._shift, self._ctrl = None, None

        wx.EVT_LEFT_DOWN(rowWindow, self.OnDragGridLeftDown)
        wx.EVT_LEFT_UP(rowWindow, self.OnDragGridLeftUp)
        wx.EVT_LEFT_UP(self, self.OnDragGridLeftUp)
        wx.EVT_MOTION(rowWindow, self.OnDragGridMotion)
        wx.EVT_KEY_DOWN(self, self.OnDragGridKeyDown)
        wx.EVT_KEY_UP(self, self.OnDragGridKeyUp)

    def OnDragGridKeyDown(self, evt):
        """Set the states of the shift and ctrl keys"""
        self._shift, self._ctrl = (evt.ShiftDown(), evt.ControlDown())

    def OnDragGridKeyUp(self, evt):
        """unset the states of the shift and ctrl keys"""
        self._shift, self._ctrl = None, None

    def OnDragGridLeftDown(self, evt):
        """The left button is down so see if we are selecting rows or not
        and do the appropriate thing.  We need to do this because we
        are blocking the rowlabels so rows won't be selected."""
        x,y = evt.GetX(), evt.GetY()
        row, col = self.DragGridRowXYToCell(x,y, colheight=0)

        if not self._shift and not self._ctrl:
            self._startRow = row
            self.SelectRow(row)
        elif self._shift and not self._ctrl:
            if self._startRow > row:
                start, end = row, self._startRow
            else:
                start, end = self._startRow, row
            for row in range(start, end+1):
                self.SelectRow(row, True)
        elif self._ctrl:
            self.SelectRow(row, True)
        self._potentialDrag = True

    def OnDragGridLeftUp(self, evt):
        """We are not dragging anymore, so unset the potentialDrag flag"""
        self._potentialDrag = False
        evt.Skip()

    def OnDragGridMotion(self, evt):
        """We are moving so see whether this should be a drag event or not"""
        if not self._potentialDrag:
            evt.Skip()
            return

        x,y = evt.GetX(), evt.GetY()
        row, col = self.DragGridRowXYToCell(x,y, colheight=0)
        rows = self.GetSelectedRows()
        if not rows or row not in rows:
            evt.Skip()
            return
        self.StartDrag(rows)

    def DragGridRowXYToCell(self, x, y, colheight=None, rowwidth=None):
        # For virtual grids, XYToCell doesn't work properly
        # For some reason, the width and heights of the labels
        # are not computed properly and thw row and column
        # returned are computed as if the window wasn't
        # scrolled
        # This function replaces XYToCell for Virtual Grids

        if rowwidth is None:
            rowwidth = self.GetGridRowLabelWindow().GetRect().width
        if colheight is None:
            colheight = self.GetGridColLabelWindow().GetRect().height
        yunit, xunit = self.GetScrollPixelsPerUnit()
        xoff =  self.GetScrollPos(wx.HORIZONTAL) * xunit
        yoff = self.GetScrollPos(wx.VERTICAL) * yunit

        # the solution is to offset the x and y values
        # by the width and height of the label windows
        # and then adjust by the scroll position
        # Then just go through the columns and rows
        # incrementing by the current column and row sizes
        # until the offset points lie within the computed
        # bounding boxes.
        x += xoff - rowwidth
        xpos = 0
        for col in range(self.GetNumberCols()):
            nextx = xpos + self.GetColSize(col)
            if xpos <= x <= nextx:
                break
            xpos = nextx

        y += yoff - colheight
        ypos = 0
        for row in range(self.GetNumberRows()):
            nexty = ypos + self.GetRowSize(row)
            if ypos <= y <= nexty:
                break
            ypos = nexty

        return row, col

    def StartDrag(self, selectedrows):
        """This starts the drag event, override this to send different drag
        types."""
        tdo = wx.PyTextDataObject(str(selectedrows))
        # Create a Drop Source Object, which enables the Drag operation
        tds = wx.DropSource(self.GetGridRowLabelWindow())
        # Associate the Data to be dragged with the Drop Source Object
        tds.SetData(tdo)
        # Intiate the Drag Operation
        tds.DoDragDrop(wx.true)


if __name__ == "__main__":
    # -----------------------------------------------------------------------
    # Testing
    class GridTextDropTarget(wx.TextDropTarget):
        def __init__(self, grid):
            wx.TextDropTarget.__init__(self)
            self.grid = grid

        def OnDropText(self, x, y, text):
            # XYToCell doesn't behave quite right, so we'll just
            # grab the DragGridRowXYToCell that we fixed,
            # see the wx.Grid wiki for a better explanation
            # http://wiki.wxpython.org/index.cgi/wxGrid
            row, col = self.grid.DragGridRowXYToCell(x, y)
            if row > -1 and col > -1:
                self.grid.SetCellValue(row, col, text)
                self.grid.Refresh()

    class T(Grid, DragGridRowMixin):
        def __init__(self, parent, id, title):
            Grid.__init__(self, parent, id)
            self.CreateGrid(25,25)
            DragGridRowMixin.__init__(self)
            self.SetDropTarget(GridTextDropTarget(self))

    app = wx.PySimpleApp()
    frame = wx.Frame(None, -1, "hello")
    foo = T(frame, -1, "hello")
    frame.Show()
    app.MainLoop()