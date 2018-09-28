#!/usr/bin/env python

import wx
from wx.lib.floatcanvas import NavCanvas, FloatCanvas


class MyFrame(wx.Frame):
  def __init__(self, *args, **kwargs):
    wx.Frame.__init__(self, *args, **kwargs)
    # Add SplitterWindow
    splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE|wx.SP_3D, size = (768,512))
    # Add left Panel
    panel1 = wx.Panel(splitter)
    panel1.SetBackgroundColour(wx.LIGHT_GREY)
    # Add Canvas
    panel2 = NavCanvas.NavCanvas(splitter,
                                 ProjectionFun = None,
                                 Debug = 0,
                                 BackgroundColor = "Grey",
                                )
    Canvas = panel2.Canvas
    # put something on the Canvas
    Point = (15,10)
    Canvas.AddScaledTextBox("A Two Line\nString",
                            Point,
                            2,
                            Color = "Black",
                            BackgroundColor = None,
                            LineColor = "Red",
                            LineStyle = "Solid",
                            LineWidth = 6,
                            Width = None,
                            PadSize = 5,
                            Family = wx.ROMAN,
                            Style = wx.NORMAL,
                            Weight = wx.NORMAL,
                            Underlined = True,
                            Position = 'br',
                            Alignment = "left",
                            InForeground = True)
    wx.CallAfter(Canvas.ZoomToBB)
    # set up the Splitter
    sash_Position = 300
    splitter.SplitVertically(panel1, panel2, sash_Position)
    min_Pan_size = 40
    splitter.SetMinimumPaneSize(min_Pan_size)
    self.Fit()


class MyApp(wx.App):
  def OnInit(self):
    frame = MyFrame(None, title='FontBakery')
    frame.Show(True)
    self.SetTopWindow(frame)
    return True

app = MyApp(0)
app.MainLoop()
