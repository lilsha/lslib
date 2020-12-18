# #author:lls time:2020-10-23
import os
import sys
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *

"""
relief
1. 指定边框样式
2. 默认值是 FLAT
3. 另外你还可以设置 SUNKEN，RAISED，GROOVE 或 RIDGE
4. 注意，如果你要设置边框样式，记得设置 borderwidth 或 bd 选项不为 0，才能看到边框
"""
class MainWindow(object):
    def __init__(self):
        root = tk.Tk()
        root.title("生产检测")
        # root.resizable(100,100)
        root.geometry('1000x800')

        frametop = Frame(root)
        frametop.pack()


        # 型号及车型文件列表
        def go(*args):  # 处理事件，*args表示可变参数
            print(comboxlist.get())  # 打印选中的值
            return comboxlist.get()
        lab = Label( frametop , text=" 检测路径选择：" ) #justify=LEFT
        lab.pack(  side=LEFT )
        comvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist = ttk.Combobox(frametop, textvariable=comvalue )  # 初始化
        comboxlist["values"] = os.listdir('e:/')
        comboxlist.current(0)  # 选择第一个
        comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
        comboxlist.pack( side=LEFT )

       #选择类型
        lab = Label( frametop , text="   检测工位选择：" ) #justify=LEFT
        lab.pack(  side=LEFT )
        v = tk.IntVar()
        chkTypeList = [ ( '主板', 1) ,
                        ( '整机', 2) ,
                        ( '应用', 3) ,
                        ( '质检', 4)  ]
        def show():
            print(v.get())
            return v.get()
        for chktype, num in chkTypeList:
            #rb1 = tk.Radiobutton(root, text=chkType, variable=v, value=num, command=show)
            b = tk.Radiobutton(frametop, text=chktype, variable=v, value=num, command=show,relief='groove'  )
            b.pack( side=LEFT)

        lab1 = Label(root,text='11111',width=1000,padx=10,pady=10)  # justify=LEFT
        lab1.pack(side=TOP)
        def comBT2():
            print("任务启动执行")
            t1.insert(1.0,'任务执行中\r\n')

        BT2 = tk.Button(root, text="检测开始", command=comBT2 ,state='disable',padx=5,pady=5 )
        #BT2.grid(row=5,column=1)
        BT2.pack( side=TOP)
        #点击按钮下拉框和路径 禁止选择
        def helloCallBack():
            print( BT1['state'] )
            if BT1[ 'text'] == '检测项确认':
                a= v.get()
                b= comboxlist.get()
                lab1['text'] = b
                print(a,b)
                t.insert('insert',b+"\r\n")
                BT1[ 'text']='检测可执行'
                BT2['state'] = 'normal'
            elif BT1[ 'text' ] == '检测可执行':
                BT2['state'] = 'disable'
                BT1['text'] = '检测项确认'


        lab = Label( frametop , text="     " ) #justify=LEFT
        lab.pack(  side=LEFT )

        BT1 = tk.Button(frametop, text="检测项确认", command=helloCallBack ,justify='left' ) #state=DISABLED状态是否可点
        BT1.pack( side=LEFT)
        f1=Frame(root)
        f1.pack()
        lab11 = Label( f1, text=" 检测过程                                                        检测日志                                           ",padx=10,pady=10)  # justify=LEFT
        lab11.pack(side=TOP)
        t = tk.Text(f1,width=30,height=40,pady=5)
        t.pack(side=LEFT)

        t1 = tk.Text(f1,width=70,height=40,pady=5)
        t1.pack(side=LEFT)

        root.mainloop()

if __name__ == '__main__':
    MainWindow()