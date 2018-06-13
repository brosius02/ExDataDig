import os
from tkinter import Button

import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title, menu_about=None, menu_exit=None):
        self.dirname = ''

        wx.Frame.__init__(self, parent, title=title, size=(1000, 600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        fileMenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        # Creating the menu bar.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")  # fileMenu to the menu bar
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menu_about)
        self.Bind(wx.EVT_MENU, self.OnExit, menu_exit)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        Button(self,
               text="Add Process",
               command=self.tell_story
               ).grid(row=0, column=0, sticky=W)

        # user some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        self.sizer.Add(self.control, 1, wx.EXPAND)

        # Layouts
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        #self.sizer.Fit(self) ###You can user this to auto fit the program
        self.Show()

    def OnAbout(self, e):
        # Mesage dialoge box with an OK button
        dlg = wx.MessageBox(self, "A sample editor \nin wxPython", "About sample editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

    def onOpen(self, e):
        """"Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            #self.filename = dlg.GetFilename()##doesnt work yet
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname.self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def tell_story(self):
        """ Fill text box with new story based on user input. """


app = wx.App(False)
frame = MainWindow(None, "Sample editor")  # type: MainWindow
app.MainLoop()
