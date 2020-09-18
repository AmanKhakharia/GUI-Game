from tkinter import*
from tkinter import messagebox,Label,Button
import random
import time

colours=['blue','red','yellow','green','red','pink','red','black','green','cyan']
global i
i=0
global redcount
redcount=0
global greencount
greencount=0
global canvas


def startclick():
    
    global i
    global canvas
    global redcount
    global greencount
    
    for i in range(1,26):
        m=random.randint(0,10)
        if m==1 or m==4 or m==6:
            redcount=redcount+1
        if m==3 or m==8:
            greencount=greencount+1
        try:
            a=random.randint(50,250)
            b=random.randint(50,300)
            canvas.create_oval(a, b, a+50, b+50, outline="white", fill=colours[m],width=2)
            canvas.update()
        except:
            print()
    return(1)

def startclick1():
    
    global i
    global canvas
    global redcount
    global greencount
    
    for i in range(1,38):
        m=random.randint(0,10)
        if m==1 or m==4 or m==6:
            redcount=redcount+1
        if m==3 or m==8:
            greencount=greencount+1
        try:
            a=random.randint(50,250)
            b=random.randint(50,300)
            canvas.create_oval(a, b, a+50, b+50, outline="white", fill=colours[m],width=2)
            canvas.update()
        except:
            print()
    return(2)

def startclick2():
    
    global i
    global canvas
    global redcount
    global greencount
    
    for i in range(1,50):
        m=random.randint(0,10)
        if m==1 or m==4 or m==6:
            redcount=redcount+1
        if m==3 or m==8:
            greencount=greencount+1
        try:
            a=random.randint(50,250)
            b=random.randint(50,300)
            canvas.create_oval(a, b, a+50, b+50, outline="white", fill=colours[m],width=2)
            canvas.update()
        except:
            print()
    return(3)
    
    
def startgame():
    global canvas
    x=startclick()
    if x==1:
        time.sleep(10)
    messagebox.showinfo("ANSWER","number of red balls="+str(redcount)+"and green balls are="+str(greencount))
    canvas.delete("all")


def startgame1():
    global canvas
    y=startclick1()
    if y==2:
        time.sleep(10)
    messagebox.showinfo("ANSWER","number of red balls="+str(redcount)+"and green balls are="+str(greencount))
    canvas.delete("all")

def startgame2():
    global canvas
    z=startclick2()
    if z==3:
        time.sleep(10)
    messagebox.showinfo("ANSWER","number of red balls="+str(redcount)+"and green balls are="+str(greencount))
    canvas.delete("all")




root=Tk()
root.title("GUI GAME")
root.geometry("800x700+50+50")
canvas=Canvas(width=500,height=500,bg='blue')
canvas.place(x=20,y=20)
w=Label(root,text="Can you count number of green and red balls",bg= "black",fg="yellow")
w.place(x=20,y=500)
y = Label(root, text="you have 10 seconds to answer ..press the start button to play!!",bg = "white",fg="blue")
y.place(x=20,y=550)
b= Button(root, text="Level 1", bg="#e79700", width=20, height=1, font=("OpenSans", 13, 'bold'), fg='white',command=startgame) 
b.place(x=550,y=50)

b= Button(root, text="Level 2", bg="#e79700", width=20, height=1, font=("OpenSans", 13, 'bold'), fg='white',command=startgame1) 
b.place(x=550,y=100)

b= Button(root, text="Level 3", bg="#e79700", width=20, height=1, font=("OpenSans", 13, 'bold'), fg='white',command=startgame2) 
b.place(x=550,y=150)

root.mainloop()


