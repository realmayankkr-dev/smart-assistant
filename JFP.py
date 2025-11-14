import wx

app = wx.App()

frame = wx.Frame(None , title ='To-Do List' , size = (500 , 400))

panel = wx.Panel(frame)
panel.SetBackgroundColour("#FFF8E1")


frame.Show()
app.MainLoop()