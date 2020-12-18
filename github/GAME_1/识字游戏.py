
#encoding=utf-8
import tkinter as tk
from tkinter import *
import re
import random
import pypinyin
import winsound


with open('C:\\Users\\THINK\\Desktop\\read.txt','r',encoding='utf-8') as fr:
    a=fr.readline()

wordsList=list(a)
wordsList=sorted(set(wordsList), key=wordsList.index)
print(wordsList)
numList=[]
for i in range(len(wordsList)):
    numList.append(i)
ww =random.shuffle(numList)
nowList = wordsList
#nowList = random.shuffle(wordsList)
print(nowList)
a = len(a)
b = []
window = tk.Tk()
window.title('识字游戏')
window.geometry('1000x500')
frm1 = Frame(window).pack()




def getWord():
    #print( len( nowList ) )
    random.shuffle( nowList )
    if len(nowList)>0:
        known[ 'text' ] = nowList[0]
        knownPinyin[ 'foreground' ] = 'green'
        knownPinyin['text'] = pypinyin.pinyin( nowList[0] )[0][0]
        del nowList[0]

        for i in range(3):
            pyList[i]=pypinyin.pinyin( nowList[i] )[0][0]
        return pyList
        #winsound.PlaySound(r'C:\\Users\\THINK\\Desktop\\gxnddl.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        print(float(a), float( len(b) ))
        known['text'] = '*** 汉字识别结束 ***'
        known['font'] = ('Arial', 28)
        knownPinyin['font'] = ('Arial', 28)
        knownPinyin['foreground'] = 'red'
        Vword =round( ( 1 - len(b)/a )*100 ,1)
        knownPinyin['text'] = '恭喜 童荣祥 小朋友 ， 你今天获得的成绩为： {:1} 继续加油！！！'.format(Vword)
        with open('C:\\Users\\THINK\\Desktop\\unknow.txt','w') as f:
            f.write(str(b))
def getColor():
    knownPinyin['foreground'] = 'black'
    b.append(known['text'])
BT1_chk = tk.Button(window, text='识字',font=('Arial', 28),command=getWord )
BT1_chk.pack()
BT1_ts = tk.Button(window, text='提示',font=('Arial', 28),command=getColor )
BT1_ts.pack()

v = IntVar()
pyList=['','','']
chkTypeList = [(pyList[0], 1), (pyList[1], 2), (pyList[2], 3)]

# def show():
#     print(v.get())
# for chktype, num in chkTypeList:
#     radioB = tk.Radiobutton(window, text=chktype, variable=v, value=num, command=show,font=('Arial', 28), relief='groove')
#     radioB.pack()

knownPinyin = tk.Label( window, text='',bg='green',width=60, height=1,font=('Arial', 200))
knownPinyin.pack()
known = tk.Label( window, text='',bg='green',width=60, height=2,font=('楷体', 250))
known.pack()


window.mainloop()
