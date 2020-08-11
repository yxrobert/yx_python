#FLASH小游戏彩色砖块辅助工具
#以下参数需要调整
#窗口大小: 668 * 526
#游戏区大小: 660 * 499
#第一次点击开始:(330, 425)
#第二次点击开始:(320, 280)
#左上角第一个方块相对坐标: (60, 100)
#格子大小: 25 * 25
#格子数量: 23 * 15
#空白格子颜色: 0xF7F7F7 和 0xEDEDED
#实体格子颜色: 
#0x0066cc
#0x00cc00
#0x6666ff
#0xbbbbbb
#0xcccc66
#0x66cccc
#0xcc66cc
#0xff6600
#0xff88ff
#0x0099ff
 
import time
import win32gui
import win32ui
import win32api
import win32con
 
#查找游戏窗口，返回窗口起始坐标
def find_flash_window():
    hwnd = win32gui.FindWindow("ShockwaveFlash", "Adobe Flash Player 28")
    if(hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        return rect[0],rect[1]
    return None
 
#模拟鼠标点击
def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
#点击格子
def click_block(xbase, ybase, x, y):
    x = xbase + x * 25 + 60
    y = ybase + y * 25 + 100
    mouse_click(x, y)
 
 
#颜色转换为方块类型
def convert_color_to_type(color):
    if(color == 0x0066cc):
        return 0x01
    if(color == 0x00cc00):
        return 0x02
    if(color == 0x6666ff):
        return 0x03
    if(color == 0xbbbbbb):
        return 0x04
    if(color == 0xcccc66):
        return 0x05
    if(color == 0x66cccc):
        return 0x06
    if(color == 0xcc66cc):
        return 0x07
    if(color == 0xff6600):
        return 0x08
    if(color == 0xff88ff):
        return 0x09
    if(color == 0x0099ff):
        return 0x0A
    if(color == 0xededed):
        return 0x00
    if(color == 0xf7f7f7):
        return 0x00
    return 0xFF
    
    
#获取方块类型
def load_one_block(hdc, xbase, ybase, x, y):
    x = x * 25 + xbase + 60;
    y = y * 25 + ybase + 100;
    color = win32gui.GetPixel(hdc, x, y)
    return convert_color_to_type(color)
    
#获取所有方块 
def load_all_block(map, xbase, ybase):
    hdc = win32gui.GetWindowDC(0)
    map.clear()
    for y in range(0, 14):
        list = []
        for x in range(0, 22):
            type = load_one_block(hdc, xbase, ybase, x, y)
            list.append(type)
        map.append(list)
    win32gui.ReleaseDC(hdc, 0)
    
#返回指定格子左边的方块
def find_left_block(map, x, y):
    for i in range(0, x):
        if(map[y][x - i] != 0x00):
            return map[y][x - i]
    return 0xFF
    
#返回指定格子右边的方块
def find_right_block(map, x, y):
    for i in range(x, 22):
        if(map[y][i] != 0x00):
            return map[y][i]
    return 0xFF
 
#返回指定格子上边的方块
def find_top_block(map, x, y):
    for i in range(0, y):
        if(map[y - i][x] != 0x00):
            return map[y - i][x]
    return 0xFF
    
#返回指定格子下边的方块
def find_bottom_block(map, x, y):
    for i in range(y, 14):
        if(map[i][x] != 0x00):
            return map[i][x]
    return 0xFF
    
#判断这个格子是否可以点击
def is_block_clickable(map, x, y):
    if(map[y][x] != 0) or (map[y][x] != 0):
        return False
    left = find_left_block(map, x, y)
    right = find_right_block(map, x, y)
    top = find_top_block(map, x, y)
    bottom = find_bottom_block(map, x, y)
    
    if(top == bottom) and (top != 0xFF):
        print("t = b:", top, bottom)
        return True
    if(top == left) and (top != 0xFF):
        print("t = l:", top, left)
        return True
    if(top == right) and (top != 0xFF):
        print("t = r:", top, right)
        return True
    if(left == right) and (left != 0xFF):
        print("l = r:", left, right)
        return True
    if(left == bottom) and (left != 0xFF):
        print("l = b:", left, bottom)
        return True
    if(right == bottom) and (right != 0xFF):
        print("r = b:", right, bottom)
        return True
    return False
    
#查找可以点击的格子
def find_click_block(map):
    for x in range(0, 22):
        for y in range(0, 14):
            if(is_block_clickable(map, x, y)):
                return x,y
    return None
 
def dump_all_block(map):
    for y in range(0, 14):
        for x in range(0, 22):
            print("%02X " % (map[y][x]), end="")
        print()
        
#程序入口
map = []
xbase = 0
ybase = 0
print("正在查找游戏窗口...")
pos = find_flash_window()
if(pos == None):
    print("查找游戏窗口失败!")
    exit()
print("查找游戏窗口成功.")
xbase = pos[0]
ybase = pos[1]
while(True):
    load_all_block(map, xbase, ybase)
    dump_all_block(map)
    print("正在查找可以点击的格子")
    pos = find_click_block(map)
    if(pos == None):
        print("游戏结束!")
        exit()
    print(pos)
    click_block(xbase, ybase, pos[0], pos[1])
    time.sleep(1)
————————————————
版权声明：本文为CSDN博主「星沉地动」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq446252221/article/details/88898433