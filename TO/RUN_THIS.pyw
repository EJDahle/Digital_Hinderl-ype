import tkinter as tk
import random as rn


y0 = -10_000


class MakeBox:
    all_boxes = []

    
    def __init__(self, canvas, x_min, y_min, x_max, y_max, speed):
        self.x_min, self.y_min = x_min, y_min
        self.x_max, self.y_max = x_max, y_max
        self.speed = speed
        self.name = canvas.create_rectangle(x_min, y_min, x_max, y_max, fill = 'gray', outline = "gray")
        MakeBox.all_boxes.append(self)

        
    def reposition(self, canvas):
        self.y_min += self.speed
        self.y_max += self.speed
        canvas.move(self.name, 0,self.speed)


class MakePlayer:
    def __init__(self, start_x, start_y, width, height):
        self.x_min = start_x - int(width/2)
        self.x_max = self.x_min + width
        self.width = width
        self.height = height
        self.y_min = start_y - int(height/2)
        self.y_max = self.y_min + height
        self.name = canvas.create_rectangle(self.x_min, self.y_min, self.x_max, self.y_max, fill = 'blue', outline = "blue")


    def move_player(self, canvas, displ):
        if self.x_min - displ < 40 and displ < 0:
            displ = 0
        if self.x_max + displ > 600 and displ > 0:
            displ = 0
        self.x_min += displ
        self.x_max += displ
        canvas.move(self.name, displ, 0)


def m():
    for i in b.all_boxes:
        i.reposition(canvas)
        if player.x_min + int(player.width/2)  in range(i.x_min - int(player.width/2), i.x_max + int(player.width/2)):
            if player.y_min in range(i.y_min, i.y_max):
                is_alive.set(False)
                root.unbind('<Left>')
                root.unbind('<Right>')
                canvas.create_text(300,300, anchor = 'center', text = 'LOOSER!', fill = "red", font = 'Arial 50')
                root.after(500, kill)
    if is_alive.get():
        canvas.itemconfigure(canvas.text, text = points.get())
        points.set(points.get() + 1)
        root.after(5,m)


def make_boxes():
    if is_alive.get():
        x0 = rn.randint(0,550)
        x_w = rn.randint(10,50)
        y_h = rn.randint(10,50)
        next_box = rn.randint(speed_inc.get(),speed_inc.get() + 100)
        if speed_inc.get() > 300:
            speed_inc.set(speed_inc.get() + 2)
        speed = rn.randint(1,speed_ran.get())
        if speed_ran.get() < 10:
            speed_ran.set(speed_ran.get() + 1)
        b = MakeBox(canvas, x0, 0-y_h, x0 + x_w, y_h, speed)
        root.after(next_box, make_boxes)


def kill():
    root.destroy()

    
def move_left(event):
    player.move_player(canvas, -20)
def move_right(event):
    player.move_player(canvas, 20)


root = tk.Tk()
points = tk.IntVar()
points.set(0)
speed_inc = tk.IntVar()
speed_inc.set(1_000)
speed_ran = tk.IntVar()
speed_ran.set(1)
is_alive = tk.BooleanVar()
is_alive.set(True)

canvas = tk.Canvas(root, width = 600, height = 600, bg = 'white')
canvas.pack()

b = MakeBox(canvas, 275, y0, 325, y0 + 50, 1)
b = MakeBox(canvas, 225, y0 + 50, 275, y0 + 100, 1)
b = MakeBox(canvas, 325, y0 + 50, 375, y0 + 100, 1)
b = MakeBox(canvas, 175, y0 + 100, 225, y0 + 150, 1)
b = MakeBox(canvas, 375, y0 + 100, 425, y0 + 150, 1)
b = MakeBox(canvas, 175, y0 + 150, 225, y0 + 200, 1)
b = MakeBox(canvas, 375, y0 + 150, 425, y0 + 200, 1)
b = MakeBox(canvas, 175, y0 + 200, 225, y0 + 250, 1)
b = MakeBox(canvas, 375, y0 + 200, 425, y0 + 250, 1)
b = MakeBox(canvas, 225, y0 + 200, 275, y0 + 250, 1)
b = MakeBox(canvas, 325, y0 + 200, 375, y0 + 250, 1)
b = MakeBox(canvas, 275, y0 + 200, 325, y0 + 250, 1)
b = MakeBox(canvas, 175, y0 + 250, 225, y0 + 300, 1)
b = MakeBox(canvas, 375, y0 + 250, 425, y0 + 300, 1)
b = MakeBox(canvas, 175, y0 + 300, 225, y0 + 350, 1)
b = MakeBox(canvas, 375, y0 + 300, 425, y0 + 350, 1)
b = MakeBox(canvas, 0, y0 + 360, 600, y0 + 370, 1)

canvas.text = canvas.create_text(300,50, anchor = 'center', text = '', fill = "red", font = 'Arial 10')
player = MakePlayer(300, 550, 50, 50)

make_boxes()
m()

root.bind('<Left>', move_left)
root.bind('<Right>', move_right)
root.mainloop()

