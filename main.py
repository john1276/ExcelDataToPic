import wx
from GUI import MyFrame2
if __name__ == '__main__':
    app = wx.App()
    frame=MyFrame2(wx.Frame(None, -1, 'win.py'))
    # set the size of the  
    frame.SetDimensions(0,0,640,480) 
    # put the frame in the center of the screen
    frame.Center() 
    # show the frame
    frame.Show()
    #start to listen users' actions
    app.MainLoop()
