#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import time
import win32gui
# import win32ui
# import win32api
# import win32con

app_name = u"UnityWndClass"
title = u"炉石传说"


#模拟鼠标点击
def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)



#send key
# win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F9, 0)#发送F9键
# win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F9, 0)


def main():
	hwnd = win32gui.FindWindow(app_name, title)
	if not hwnd:
		print("ERROR hwnd")
		return

	hdc = win32gui.GetWindowDC(hwnd)
	if not hdc:
		print("ERROR hdc")
		return

	color = win32gui.GetPixel(hdc, 1322, 770)
	# print(0x00ff0000 & color)
	print(color)
	print(hex(color))






if __name__ == "__main__":
    main()