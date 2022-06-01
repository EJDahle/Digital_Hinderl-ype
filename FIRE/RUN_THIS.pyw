from random import choice, randint
from tkinter import *
from tkinter import ttk
import thEtext as te
from utils import checkChange,splitIfTooLong

root = Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Click The Button")

labelPoints = IntVar(root,0)
pointLabel = Label(root,textvariable=labelPoints)
pointLabel.pack()

def youClickedTheButton():
    global stopTaunt
    stopTaunt = True
    root.bind("<Motion>", lambda i:None)
    pointLabel.pack_forget()
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    pressButton.place_forget()
    pressButton.grid(row=0,column=0,sticky="NEWS")
    pressButton.configure(text=te.get_text("DHX GMfnL nayB ÆKMÆqBC GB sXL LnaLE IHL LnB eaå LH fBL LnB KBLLBø"),command=None)

pressButton = ttk.Button(root,name="ok",command=youClickedTheButton)
pressButton.place(x=randint(0,root.winfo_width()),y=randint(0,root.winfo_height()))

data = open("nums.txt","r").readlines()
taunts = [i.strip("\n") for i in open("taunts.txt","r").readlines()]
currentTaunt = None
usedTaunts = []
misses = 0
stopTaunt = False

def changePos():
    unknownData = eval(choice(data))
    startTaunt()
    setPos(unknownData[0],unknownData[1])


def startTaunt():
    global currentTaunt,usedTaunts,stopTaunt

    if stopTaunt:
        return

    while True:
        taunt = choice(taunts)
        if taunt not in usedTaunts:
            usedTaunts.append(taunt)
            if len(usedTaunts)>10:
                del usedTaunts[0]
            break

    currentTaunt = taunt

    if "|" in taunt:
        lines = taunt.split("|")
        pressButton.configure(text=lines[0])
        currentIndex = IntVar(root,1)

        def comment():
            if currentTaunt != taunt:
                return
            if stopTaunt:
                return
            index = currentIndex.get()

            if len(lines) <= index:
                return

            line = splitIfTooLong(lines[index])
            time = index*1000+(len(line)*10)

            pressButton.configure(text=line)
            currentIndex.set(index + 1)

            root.after(time,comment)

        root.after(1000+(len(lines[0])*10),comment)
    else:
        pressButton.configure(text=splitIfTooLong(taunt))

def setPos(x:int,y:int):
    pressButton.place_forget()
    pressButton.place(x=x,y=y)

def move(event:Event):
    global misses,stopTaunt
    if event.widget == pressButton:
        changePos()
        misses += 1
        labelPoints.set(misses)
        result = checkChange(root,pressButton,misses)
        for key,val in result.items():
            exec(f"global {key}\n{key}={val}")
        result.clear()
   
root.bind("<Motion>", move)
root.mainloop()