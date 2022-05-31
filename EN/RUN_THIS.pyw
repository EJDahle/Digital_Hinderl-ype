import tkinter as tk
import thEtext as te

visible_color = "#99ccff"
invisible_color = "#99cccc"




def show_msg():
    msg1 = ['RBM', 'mBKqHGGBI LMK lfMK EMI CMfMLaKB nMICBøKFåPBu',
           'Y xMKBIB xMIIBø CX sHqELayBøu NMEEB sKMø BI qøåPLBøMIfEIFqqBKu',
           'vFqqBKBI søXqBE LMK r KBEB BI xMKu NX Gr HfEr xMIIB xMKBIu',
           'SDddl oYS!', 'X']
    msg = []
    for i in msg1:
        msg2 = te.get_text(i)
        msg3 = msg2.split(" ")
        if len(msg3) > 5:
            msg4 = msg3[:5] + ["\n"] + msg3[5:]
        else:
            msg4 = msg3
        text = ""
        for n, m in enumerate(msg4):
            if n > 0:
                text +=  " " + m
            else:
                text += m
                
        msg.append(text)
    if len(msg[msgNum.get()]) > inString.get() and len(msg) > msgNum.get():
        inString.set(inString.get() + 1)
        label1.config(text = msg[msgNum.get()][0:inString.get()])
        root.after(100, show_msg)
    else:
        msgNum.set(msgNum.get() + 1)
        inString.set(0)
        if len(msg) > msgNum.get():
            root.after(1000, show_msg)
        else:
            root.after(1000, kill)
    
    
def kill():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen',True)
root.config(bg = invisible_color)
root.attributes('-transparentcolor', invisible_color)

inString = tk.IntVar()
inString.set(0)
msgNum = tk.IntVar()
msgNum.set(0)

label1 = tk.Label(root, text = "", font = ('Times 100'), bg = invisible_color, fg = visible_color)
label1.pack(fill='both', expand=True)

show_msg()
root.mainloop()
