#author:lls time:2020-10-28

import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk


def scroll1():
    root = tk.Tk()
    monty = ttk.LabelFrame(root, text=" Monty Python ")  # 创建一个容器，其父容器为win
    monty.grid(column=0, row=0, padx=10, pady=10)
    scr = scrolledtext.ScrolledText(monty, width=30, height=5, wrap=tk.WORD)
    scr.grid(column=0, columnspan=3)
    root.mainloop()


def scroll2():
    root = tk.Tk()
    root.grid()
    app = ttk.Frame(root)
    app.grid()
    frame1 = tk.LabelFrame(app, text='1')
    txt1 = tk.Text(frame1)
    sl1 = Scrollbar(frame1)
    sl1['command'] = txt1.yview
    sl1.grid(row=0, column=1, sticky=S + W + E + N)
    txt1.grid(row=0, column=0, sticky=S + W + E + N)
    frame1.grid(row=0, column=0, sticky=S + W + E + N)
    mainloop()
scroll1()
scroll2()