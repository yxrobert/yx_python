# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:45:42 2019

@author: Martin
"""


import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText

import tkinter.filedialog
from tkinter import *
import tkinter.messagebox


recivier_list = {
    'yX_Robert_91@kindle.cn'
    , 'yX_Robert_6db7bc@kindle.cn'
    , 'yX_Robert@163.com'
}

def send():
    msg = email.mime.multipart.MIMEMultipart()
    msgFrom = 'yX_Robert@163.com' #SMTP的邮箱
    # msgTo = 'yX_Robert_6db7bc@kindle.cn' #亚马逊的邮箱
    msgTo = 'yX_Robert_91@kindle.cn' #亚马逊的邮箱
    # msgTo = 'yX_Robert@163.com' #亚马逊的邮箱
    smtpSever='smtp.163.com'  #SMTP的服务器
    smtpPort = '25'  #端口号
    sqm='1234qwer' #邮箱密码

    msg['from'] = msgFrom
    msg['to'] = msgTo
    msg['subject'] = '[Kindle]Martin'

    content = '''
    Dear Martin,
         
        Please check this book.
         
    Auto send program
    '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    #附件
    #path=file_path
    #file_name=path+name+'.xlsx'
    att = MIMEText(open(file_path, 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename='+file_path
    msg.attach(att)
    #
    smtp = smtplib
    smtp = smtplib.SMTP()

    try:
        smtp.connect(smtpSever, smtpPort)
        print("connect success!")
        smtp.login(msgFrom, sqm)
        print("login success!")

        for i in recivier_list:    
            smtp.sendmail(msgFrom, i, str(msg))
            print("%s邮件发送成功", i)
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



def callback1():
    global file_path
    file_path = tkinter.filedialog.askopenfilename(initialdir ="C:/Users/Martin/Downloads",filetypes=( ("亚马逊电子书格式", "mobi"), ("all", "*.*"), ("文本", "*.txt*"),("Excel 97-2003 工作簿", "*.xls")))
    t.insert('insert',file_path)

def t_k():
    root = Tk()
    root.title('发送文件至 Paper White 3')
    tkinter.Label(root, text='发送文件至kindle',bg='Gainsboro', font=('微软雅黑', 15,'bold'), width=400, height=2).pack()
    tkinter.Label(root,
        text="软件使用说明：1,先选择文件，2,然后点击发送。\n --by Martin",
        bg='Gainsboro', font=('微软雅黑', 11), width=400, height=3).pack()
    fm=Frame(root)
    Button(fm, text="选择文件", font = ('微软雅黑',10),fg="DodgerBlue",bd=2,width=20,command=callback1, relief=GROOVE).pack(side=LEFT, anchor=W, fill=X, expand=YES)
    fm.pack(side=TOP)
    global t
    t = Text(root,height=1,font =('微软雅黑', 10), fg="Black",bg='White')
    t.pack()

    Button(fm, text="发送", font = ('微软雅黑',10), fg="DarkRed",bd=2,width=20,command=send, relief=GROOVE).pack(side=LEFT, anchor=W, fill=X, expand=YES)

    sw = root.winfo_screenwidth()#得到屏幕宽度
    sh = root.winfo_screenheight()#得到屏幕高度
    ww = 700
    wh = 350#窗口宽高为100
    x = (sw-ww) / 2
    y = (sh-wh) / 2
    root.geometry("%dx%d+%d+%d" %(ww,wh,x,y)) #窗口居中

    root.mainloop()
if __name__=='__main__':
    t_k()