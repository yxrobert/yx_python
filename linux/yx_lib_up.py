#-*- coding:utf-8 -*-

import os

import re

def update():

    pipList = os.popen('pip3 list --outdate').readlines() #这里就相当于我们在cmd里面输入pip3 list 展示 pip3 安装的所有包

    #print(pipList)

    p = re.compile(r'\(.*?\)')#由于pipList里面存储的数据都是pefile (2017.11.5) 这种样子的，但是我们只需要pefile而不要()里面的东西，所以要利用正则表达式将()以及里面的内容去掉

    try:

        for i in pipList:

            content = p.sub('',i) #利用正则表达式去掉无用的信息

            print(content)

            os.system('pip3 install --upgrade' + ' '+content) #开始更新内容

    except:

        pass






if __name__=='__main__':

    update()