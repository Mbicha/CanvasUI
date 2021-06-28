# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:00:52 2021

@author: Charles Mbithi
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Simple Designer App')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#variables
_color = 'green'

frame = Frame(root, bg='blue')
frame.pack()

canvas = Canvas(frame, relief=SUNKEN, borderwidth=3)
canvas.pack(fill=BOTH)

control_frame = Frame(frame, relief=RAISED, borderwidth=3, bg='gold')
control_frame.pack(fill=BOTH, ipadx=3, ipady=3)

def drawLine():
    canvasClear()
    canvas.create_line(10,10, 200,40, fill=_color, width=2)
    
def makeArc():
    canvasClear()
    canvas.create_arc(50,20, 300, 200, outline=_color, start=5, extent=90, width=1)
    
def createOval():
    canvasClear()
    canvas.create_oval(10, 20, 100, 40, fill=_color, width=1)
    
def createRectangle():
    canvasClear()
    canvas.create_rectangle(10, 10, 200, 40, outline=_color, width=1) 
    
def createBtn(label, col, row_row, _command):
    createdBtn = Button(control_frame, text=label, width=10, command = _command)
    createdBtn.grid(column=col, row=row_row, padx=5, pady=5)
    return createdBtn

def canvasClear():
    canvas.delete('all')

#Buttons
createBtn('Line', 0, 0, drawLine)
createBtn('Arc', 1, 0, makeArc)
createBtn('Oval', 2, 0, createOval)
createBtn('Rectangle', 3, 0, createRectangle)

root.mainloop()