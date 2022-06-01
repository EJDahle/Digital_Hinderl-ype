from random import randint
from tkinter import *
from tkinter import ttk

timeLeft = 160*1000
colorOffset = [randint(-1,1) for i in range(6)]
hexLetters = "0123456789ABCDEF" 
returnThings = {}

def getFullRandomHexCode():
    global colorOffset
    for index, val in enumerate(colorOffset):
        upOrDownVal = randint(-1,1)+val
        if upOrDownVal > 15:
            colorOffset[index] -= 16
            continue
        if upOrDownVal < -16:
            colorOffset[index] += 17
            continue
        colorOffset[index] = upOrDownVal

    return "".join([hexLetters[(colorOffset[i])] for i in range(6)])

def checkChange(root:Tk,button:ttk.Button,amount:int):
    global returnThings
    match amount:
        case 12:
            button.configure(text="The insults are not gonna stop")
        case 69:
            button.configure(text="Nice")
        case 100:
            button.configure(text="Now thats some commitment")

        case 420:
            def colorChange():
                global timeLeft
                if timeLeft < 0:
                    root.configure(background="SystemButtonFace")
                    [child.configure(background="SystemButtonFace") for child in root.winfo_children() if type(child) == Label]
                    returnThings["stopTaunt"] = False
                    return
                timeLeft -= 1000
                hexCode = "#"+getFullRandomHexCode()
                root.configure(background=hexCode)
                [child.configure(background=hexCode) for child in root.winfo_children() if type(child) == Label]
                button.configure(text="WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED")
                root.after(100,colorChange)
            colorChange()
            returnThings["stopTaunt"] = True

        case 9001:
            button.configure(text="ITS OVER 9000!!!!!!!!!!!!!!!")

    return returnThings

def splitIfTooLong(text:str):
    if not len(text) > 50:
        return text
    splitSpace = round(len(text)/2)
    left = splitIfTooLong(text[:splitSpace])
    right = splitIfTooLong(text[splitSpace:])
    return "".join((left,"-\n",right))
# print(splitIfTooLong("how is you day going|mine is doing extremly great|now that i get to see you fail"))