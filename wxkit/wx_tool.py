# -*- coding:utf-8 -*-
import wx
import redis
import socket

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='', size=(300, 588),name='loc_tool',style=541072384)
        icon = wx.Icon(r'C:\Users\PC\Desktop\git-for-windows.ico')
        self.SetIcon(icon)
        self.loc_tool = wx.Panel(self)
        self.Centre()
        self.svr_button = wx.Button(self.loc_tool,size=(90, 30),pos=(15, 10),label='编译服务器',name='编译服务器')
        self.svr_button.Bind(wx.EVT_BUTTON,self.svr_button_hit)
        self.config_button = wx.Button(self.loc_tool,size=(90, 30),pos=(177, 9),label='编译配表',name='编译配表')
        self.config_button.Bind(wx.EVT_BUTTON,self.config_button_hit)
        self.list_box = wx.ListBox(self.loc_tool,size=(254, 473),pos=(16, 68),name='listBox',choices=[],style=32)


    def svr_button_hit(self,event):
        print('svr_button,按钮被单击')
        self.list_box.InsertItems("svr_button_hit", 0)


    def config_button_hit(self,event):
        print('config_button,按钮被单击')


    def OnPaint(self, e):
        print("OnPaint")
        self.list_box.InsertItems("OnPaint", 0)
        # wx.MessageDialog(self, "A small editor in wxPython", "About Sample Editor", wx.OK)

    def OnIdle(self, e):
        print("OnIdle")
        wx.MessageDialog(self, "A small editor in wxPython", "About Sample Editor", wx.OK) 

class myApp(wx.App):
    def  OnInit(self):
        self.iDmfbdvaNk = Frame()
        self.iDmfbdvaNk.Show(True)
        return True

r_table_name = "loc_iptables"
# wx.MessageDialog( self, "A small editor in wxPython", "About Sample Editor", wx.OK)
def main():
    # r = redis.Redis(host='192.168.44.38', port=7001, decode_responses=True)
    # r.hset(r_table_name, socket.gethostbyname(socket.gethostname()), socket.gethostname())
    
    app = myApp()
    app.MainLoop()

if __name__ == '__main__':
    main()
