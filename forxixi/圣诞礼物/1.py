from tkinter import *
from tkinter import messagebox


#导入所依赖的库
from turtle import *
from datetime import*
import random
import time


t = 0

def Merry():
    colormode(255)
    color(125,125,50)
    penup()
    back(50)
    goto(0,-100)
    pendown()
    write(("Merry Christmas"),align="center",font=("Courier", 24, "bold")) 
    penup()
    #Merry Christmas

def howday():
    past = datetime.strptime('2018-8-26 13:14:00','%Y-%m-%d %H:%M:%S')#过去时间
    now = datetime.now()#当前时间
    delta = now - past#求时间差
    colormode(255)
    color(125,125,50)
    penup()
    back(50)
    goto(0,-220)
    pendown()
    write(("爱我宝贝的第"+str(delta.days)+"天"),align="center",font=("Courier", 14, "bold")) 
    penup()

def tree():
    n = 80.0

    goto(0,0)
    pendown()
    #设置速度快

    speed(0)
    delay(10)

    pensize(20)

    #背景颜色 海贝壳色，偏粉色

    screensize(bg='seashell')

    left(90)

    forward(3*n)

    color("orange", "yellow")

    begin_fill()

    left(126)

    

    for i in range(5):

        forward(n/5)

        right(144)

        forward(n/5)

        left(72)

    end_fill()

    right(126)

    

    color("dark green")

    backward(n*4.8)

    def tree(d, s):

        global t
        
        t = t + 1
        
        delay(13-t/100)
        #delay(0)

        if d <= 0: return

        forward(s)

        tree(d-1, s*.8)

        right(120)

        tree(d-3, s*.5)

        right(120)

        tree(d-3, s*.5)

        right(120)

        backward(s)

    tree(12, n)

    backward(n/2)

    
    pensize(2)

    for i in range(90):

        a = 200 - 400 * random.random()

        b = 10 - 20 * random.random()

        up()

        forward(b)

        left(90)

        forward(a)

        down()

        if random.randint(0, 1) == 0:

                color('tomato')

        else:

            color('wheat')

        circle(2)

        up()

        backward(a)

        right(90)

        backward(b)


def window():
    window = Tk()
    window.title("爱我吗")
    window.geometry("300x200")
    window.configure(bg = "seashell")
    lbl = Label(window, text="你爱我吗", font=("华文行楷", 30),padx=10,pady=10)
    #lbl.grid(column=0, row=0)
    lbl.place(x=60,y = 10)
    global mm,click2
    click2 = 0
    mm = 0
    def clicked1():
        global click2
        click2 += 1 
        if click2==1:
            messagebox.showinfo("不可以", " 当然不可以")
        elif click2==2:
            messagebox.showinfo("不可以", " 再给你个考虑的机会")
        elif click2==3:
            messagebox.showinfo("不可以", " 还不改是吧")
        elif click2==4:
            messagebox.showinfo("不可以", " 再这样我就生气了啊")
        else:
            messagebox.showinfo("不可以", " 甚重考虑啊")


    def clicked2():
        def yclose():
            mback = messagebox.askquestion("??","还敢关掉？")
            if mback:
                return
            else:
                m_messagebox.showinfo("爱你呦", " 我就说嘛")

        global mm
        mm = 1
        m_messagebox = messagebox
        m_messagebox.showinfo("爱你呦", " 那就对了")
        messagebox.showinfo("爱你呦", " 我也爱你")
        window.destroy()
        tree()
        howday()
        Merry()
    def closeWindow():
        global mm
        if mm == 0:
            messagebox.showinfo("不可以", " 以为关掉就可以不爱我了？")
        else:
            window.destroy()
      
    btn1 = Button(window, text="不爱", command=clicked1,height=2,width=15, bg="pink", fg="red")
    #btn1.grid(column=0, row=2)
    btn1.place(x = 50,y=100)
    btn2 = Button(window, text=" 爱 ", command=clicked2,height=2,width=15, bg="pink", fg="red" )
    btn2.place(x = 150,y=100)
    #btn2.grid(column=1, row=2)

    def mexit(event):
        if messagebox.askokcancel('Exit','Confirm to exit?'):
            window.destroy()
        #window.destroy()
    window.protocol('WM_DELETE_WINDOW', closeWindow)
    #window.bind("<Escape>", mexit)
    window.bind("<Alt-z>", mexit)
    window.mainloop()


def main():
    window()


if __name__ == "__main__":
    main()
    

