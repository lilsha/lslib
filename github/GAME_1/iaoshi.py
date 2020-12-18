import time
import os,shutil
from tkinter import *

for i in range(10000):
    b=open('e:\\lisha\\11.txt', 'a+')
    b.write('{}_11111111111111111 \r'.format(i))
b.close()
def onGo():
    a = open('e:\\lisha\\11.txt', 'r')
    def counter(i):
        if i > 0:
            data = a.readline()
            if data!='':
                #t.insert(END, 'a_' + str(i)+'\r\n')
                t.insert(END, 'a_' + data + '\r\n')
                t.after(10, counter, i+1 )
                t.see(END)
            else:
                pass
        else:
            goBtn.config(state=NORMAL)

    counter(50)
    #------------------------------



root = Tk()
t = Text(root)
t.pack()
goBtn = Button(text="Go!", command=onGo)
goBtn.pack()
root.mainloop()






# pp = os.path.exists('e:\\lisha\\11aab.txt')
# print(pp)
# if pp==False:
#     with open('e:\\lisha\\11aab.txt','a') as ff:
#         ff.close()
#     print( os.path.exists('e:\\lisha\\11aab.txt') )

