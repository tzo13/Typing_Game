from tkinter import *
import random

t = Tk()
list = ['The purple kangaroo wore sunglasses and danced to jazz music—what a sight!','I tried to teach my cat how to moonwalk, but she preferred napping... typical.','A potato wearing a top hat just asked for directions to the nearest pizza place—bizarre!','Every Tuesday, a group of flamingos hosts a badminton tournament on the beach... they’re champions!','The jellybean factory accidentally made a rainbow-colored giraffe that only eats marshmallows—oops!','A squirrel with a monocle gave me financial advice on how to save for a rocket ship. Wise little creature!','My sneakers started a rock band called "The Rolling Soles"—they’re on tour next month','The pancake I made for breakfast has mysteriously grown a tiny mustache. Should I be concerned?','The clouds were so fluffy, I thought I saw a unicorn jumping between them—seriously, it was magical!','If I could talk to trees, I’d probably ask them for tips on how to grow taller... and how to be more patient!']
score = 0
time = 120
t.configure(background="#43a370")



def anakata(event):
    global score
    a = e.get()
    random.shuffle(list)
    lbl.configure(text =list[0])
    if a == list[0]:
        score += 1
        scor.configure(text ="Score: " + str(score))
        anakata()
        e.delete(0, END)


def countdown():
    global time
    if time > 0 :
        time -= 1
        xrono.configure(text = "Time: "+ str(time))
        xrono.after(1000,countdown)

def mpla(event):
    t.bind('<Return>',anakata)
    if time == 120:
        countdown()



o1 = Label(t,text = "Pata to 0 mia fora na ksekinsei t paixnidi kai meta enter ",  bg = "#43a370")
o2 = Label(t,text = "Kathe fora p exeis mia apantish pata to enter",bg = "#43a370")
o3 = Label (t,text = "Exeis dyo lepta epdh imaste large",bg = "#43a370")
lbl = Label(t,text = "START",font = '#7fff00,40',bg = "#43a370")
e = Entry (t)
scor = Label(t,text = "score",bg = "#43a370")
xrono = Label(t,text ="time",bg = "#43a370")
t.bind('<0>', mpla)


o1.grid(row =0 , column=0)
o2.grid(row = 1, column =0)
o3.grid(row = 2, column = 0)
lbl.grid(row =5 , column = 0)
e.grid(row =6 , column = 0 )
scor.grid(row = 4, column = 0 )
xrono.grid(row = 3,column = 0)


t.mainloop()    