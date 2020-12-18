# -*- coding:utf-8 -*-
from tkinter import *
import time
import random
import pypinyin

with open('C:\\Users\\THINK\\Desktop\\read.txt', 'r', encoding='utf-8') as fr:
    aList = list(fr.readline())
    print('1', aList)
    # 删除重复的元素
    bList = sorted(set(aList), key=aList.index)
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, bg='black')
        self.pack(expand=YES, fill=BOTH)
        self.window_init()
        self.createWidgets()

    def window_init(self):
        self.master.title('儿童识字')
        self.master.bg = 'black'
        self.master.geometry('1000x600')

    def createWidgets(self):
        # fm1
        self.fm1 = Frame(self, bg='black')
        self.fm1.pack()


        # fm2
        self.fm2 = Frame(self, bg='black')
        self.fm2.pack()

        self.fm3 = Frame(self, bg='black')
        self.fm3.pack()
        self.fm4 = Frame(self, bg='black')
        self.fm4.pack()
        self.predictButton = Button(self.fm1, text='识字', bg='#22C9C9', fg='white',font=('微软雅黑', 18), width='16')#command=self.output_predict_sentence
        self.predictButton.pack(side=LEFT)
        self.lalnul1 = Label(self.fm1, text='', height=1, bg='black', font=('微软雅黑', 48))
        self.lalnul1.pack(side=LEFT)

        self.separator = Frame(height=2, bd=2, relief="sunken")
        self.separator.pack(fill="x", padx=50, pady=50)

        self.lal = Label(self.fm3, text='哈', height=1, bg='black',fg='white',font=('微软雅黑', 200))
        self.lal.pack(side=LEFT)
        self.lalnul3 = Label(self.fm3, text='', height=1, bg='black', font=('微软雅黑', 48))
        self.lalnul3.pack(side=LEFT)
        v = IntVar()
        pyList = self.getWord()
        chkTypeList = [(pyList[0], 1), (pyList[1], 2), (pyList[2], 3), (pyList[3], 4)]
        def show():
            print(v.get())
        for chktype, num in chkTypeList:
            radioB = Radiobutton(self.fm2, text=chktype, variable=v, value=num, command=show, font=('Arial', 36),relief='groove',padx=10)
            radioB.pack(side=LEFT)

        self.lalnul2 = Label(self.fm2, text='', height=1, bg='black', font=('微软雅黑', 56))
        self.lalnul2.pack(side=LEFT)
        self.lalnul4 = Label(self.fm4, text='', height=1, bg='black', font=('微软雅黑', 36))
        self.lalnul4.pack(side=TOP)
        self.truthButton = Button(self.fm4, text='提交', bg='#22C9C9', fg='white',font=('微软雅黑', 18), width='16')
        self.truthButton.pack(side=TOP)


if __name__ == '__main__':
    app = Application()
    # to do
    app.mainloop()
