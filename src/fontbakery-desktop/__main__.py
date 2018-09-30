#!/usr/bin/env python

import os
import wx
from wx.lib.floatcanvas import NavCanvas, FloatCanvas


def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_NORMAL)
    result = wx.BitmapFromImage(image)
    return result


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.CreateStatusBar()
        splitter = wx.SplitterWindow(self,
                                     style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH,
                                     size=(1024, 768))

        # Add the Panel
        panel1 = wx.Panel(splitter)
        panel1.BackgroundColour = 'GREY'
        bitmap = wx.Bitmap(os.path.join(os.path.dirname(__file__),
                           'headline.png'))
        bitmap = scale_bitmap(bitmap, 512, 512)
        sb = wx.StaticBitmap(panel1, bitmap=bitmap, pos=(0, 0))

        # Add the Canvas
        panel2 = NavCanvas.NavCanvas(splitter,
                                     ProjectionFun=None,
                                     Debug=0,
                                     BackgroundColor="LIGHT GREY",
                                     )
        Canvas = panel2.Canvas

        # Put stuff on the Canvas
        Point = (15, 10)
        Canvas.AddScaledTextBox("Markdown output \nwill be shown here.",
                                Point,
                                2,
                                Color="DARK GREY",
                                BackgroundColor=None,
                                LineColor="DARK GREY",
                                LineStyle="Solid",
                                LineWidth=2,
                                Width=None,
                                PadSize=5,
                                Family=wx.SWISS,
                                Style=wx.NORMAL,
                                Weight=wx.NORMAL,
                                Underlined=False,
                                Position='br',
                                Alignment="center",
                                InForeground=False)
        wx.CallAfter(Canvas.ZoomToBB)

        # Set up the Splitter
        sash_Position = 512
        splitter.SplitVertically(panel1, panel2, sash_Position)
        min_Pan_size = 0
        splitter.SetMinimumPaneSize(min_Pan_size)
        self.Fit()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title='FontBakery')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
