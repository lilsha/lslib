#author:lls time:2020-10-26
import os,time,re
import tkinter as tk
from tkinter import *
from tkinter import ttk

"""
l = tk.Label(window, 
    text='OMG! this is TK!',    # 标签的文字
    bg='green',                 # 背景颜色
    font=('Arial', 12),         # 字体和字体大小
    width=15, height=2          # 标签长宽)
l.pack()    # 固
"""

class MainWindow():
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("恒领生产检测")
        self.root.geometry('1000x800')
        #框架
        self.frame = Frame(self.root)
        self.frame.pack()
        # 第一行：检测项标签
        self.lab1 = Label(self.frame,text='检测项目:')
        self.lab1.pack( side=LEFT )
        # 第一行：文件选择框功能
        def go(*args):  # 处理事件，*args表示可变参数
            print(self.comboxlist.get())  # 打印选中的值
            return self.comboxlist.get()

        self.comvalue = StringVar()# 窗体自带的文本，新建一个值
        self.comboxlist = ttk.Combobox(self.frame, textvariable=self.comvalue ,width=50)  # 初始化
        self.comboxlist["values"] = os.listdir('e:/')
        self.comboxlist.current(0)  # 选择第一个
        self.comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
        self.comboxlist.pack(side=LEFT)


        # 第一行：留空
        self.lab_NULL2 = Label( self.frame, text='  ' )
        self.lab_NULL2.pack(side=LEFT)
        # 第一行：检测工序标签
        self.lab2 = Label( self.frame, text='检测工序:' )
        self.lab2.pack(side=LEFT)
        # 第一行：工序配置项功能
        v = IntVar()
        chkTypeList = [('主板', 1),
                       ('整机', 2),
                       ('应用', 3),
                       ('质检', 4)]

        def show():
            print(v.get())
            return v.get()
        for chktype, num in chkTypeList:
            self.radioB = Radiobutton(self.frame, text=chktype, variable=v, value=num, command=show, relief='groove')
            self.radioB.pack(side=LEFT)

        #第一行：留空
        self.lab_NULL1 = Label( self.frame, text='     ' )
        self.lab_NULL1.pack(side=LEFT)
        #第一行：按钮，检测前选项配置功能

        def bt1Function():
            chk_type = v.get()  # 获取检测项装填
            chk_file = self.comboxlist.get()  # 获取文件选项
            if chk_type=="" or chk_type =="":
                print("请从新选择")#实际要做弹框提示
                pass
            else:
                if self.bt1[ 'text'] == '检测项确认':
                    self.lab1['text'] ='检测项目为：  e:/{}/{}'.format(chk_file,chkTypeList[chk_type-1][0])
                    print(chk_type,chk_file)
                    self.process.insert('insert',self.lab1['text'])
                    self.bt1[ 'text']='检测可执行'
                    self.bt1[ 'bg' ]='red'
                    self.bt2['state'] = 'normal'
                    self.bt2['bg'] = 'green'

                elif self.bt1[ 'text' ] == '检测可执行':
                    self.bt1['bg'] = 'green'
                    self.bt1['text'] = '检测项确认'
                    self.bt2['state'] = 'disable'
                    self.bt2['bg'] = 'red'
        def getCommand():
            fileList = os.listdir( "%s"%(self.lab1['text']).replace("检测项目为：  ",""))
            print(fileList)
            if len(fileList) == 2:
                print(fileList)
                for file in fileList:
                    if file.endswith(".txt"):
                        caseName = file
                    elif file.endswith('.py'):
                        varName = file
                if caseName != "" and varName != "":
                    Command = 'sudo pybot -P /home/pi/hlrfw/keywords/ -V /home/pi/CHK/{} /home/pi/CHK/{} '.format(varName,caseName)
                    print(Command)
                    return Command
                    #startCommand = os.system( Commnad )
                else:
                    print('文件缺失')
                    Command = ""
                    return Command
        self.bt1 = Button(self.frame, text='检测项确认', command=bt1Function)
        self.bt1.pack(side=RIGHT)

        #第二行：检测项目信息
        self.lab1 = Label(self.root,text='11111',width=1000,padx=10,pady=10)  # justify=LEFT
        self.lab1.pack(side=TOP)
        #第三行:隔开行横线
        self.separator = tk.Frame(height=2, bd=2, relief="sunken")
        self.separator.pack(fill="x", padx=10, pady=10)
        #第四行：启动检测按钮功能


        def pp():

            print(self.lab1['text'])
            self.log.insert('insert',getCommand())
            for i in range(100):
                aa.log.insert('insert', '1111111111111111')
                time.sleep(1)

        self.bt2 = Button(self.root, text='启动检测',width=10,height=3,font=('Times', 16),bg='green',state='disable',command=pp)
        self.bt2.pack(side=TOP)
        #第五行：留空
        self.separator1 = tk.Frame(height=2, bd=2, relief="sunken")
        self.separator1.pack(padx=10, pady=10)
        #创建框架给日志打印和什么打印
        self.frm_txt = Frame(self.root)
        self.frm_txt.pack()
        #第6行：说明标签
        self.labm = Label(self.frm_txt,width=120,text='                   检测过程                                                        日志打印                      ')
        self.labm.pack()
        #创建两个TXT

        self.process = Text(self.frm_txt,width=50,height=40,pady=5,relief='raised')# "sunken"，"raised"，"groove" 或 "ridge"
        self.process.pack(side=LEFT)
        self.log = Text(self.frm_txt,width=70,height=40,pady=5,relief='raised')
        self.log.pack(side=LEFT)
        def ppp():
            self.log.delete( 0.0, tk.END )
            self.process.delete( 0.0,tk.END )
        self.bt3 = Button(self.frm_txt, text='关机',width=10,height=3,font=('Times', 16),command=ppp)
        self.bt3.pack(side=BOTTOM)
        self.frame.mainloop()
    def ww(self):
        while True:
            print('1111')
            self.process.insert('insert','1111')
            time.sleep(1)
if __name__ =='__main__':
    MainWindow()

