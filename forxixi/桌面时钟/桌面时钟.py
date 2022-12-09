from turtle import*
from datetime import*
import time

def D(n,r,d=1):
    for i in range(n):
         left(d)
         circle(r,abs(d))#玫瑰
def rose():
    reset()
    s = 0.2 #size
    setup(450*5*s,750*5*s)
    pencolor("black")
    fillcolor("red")
    speed(100)
    penup()
    goto(0,900*s)
    pendown()
#花朵
    begin_fill()
    circle(200*s,30)
    D(60,50*s)
    circle(200*s,30)
    D(4,100*s)
    circle(200*s,50)
    D(50,50*s)
    circle(350*s,65)
    D(40,70*s)
    circle(150*s,50)
    D(20,50*s,-1)
    circle(400*s,60)
    D(18,50*s)
    fd(250*s)
    right(150)
    circle(-500*s,12)
    left(140)
    circle(550*s,110)
    left(27)
    circle(650*s,100)
    left(130)
    circle(-300*s,20)
    right(123)
    circle(220*s,57)
    end_fill()
#
    left(120)
    fd(280*s)
    left(115)
    circle(300*s,33)
    left(180)
    circle(-300*s,33)
    D(70,225*s,-1)
    circle(350*s,104)
    left(90)
    circle(200*s,105)
    circle(-500*s,63)
    penup()
    goto(170*s,-30*s)
    pendown()
    left(160)
    D(20,2500*s)
    D(220,250*s,-1)
#
    fillcolor("green")
    penup()
    goto(670*s,-180*s)
    pendown()
    right(140)
    begin_fill()
    circle(300*s,120)
    left(60)
    circle(300*s,120)
    end_fill()
    penup()
    goto(180*s,-550*s)
    pendown()
    right(85)
    circle(600*s,40)
#
    penup()
    goto(-145*s,-910*s)
    pendown()
    seth(45)
    begin_fill()
    right(120)
    circle(300*s,120)
    seth(105)
    circle(300*s,120)
    end_fill()
    penup()
    goto(430*s,-1070*s)
    pendown()
    right(50)
    circle(-600*s,35)
    fd(50)
    write("2019-2-14", align="center", font=("Courier", 17, "bold"))
   



def koch(size,n):
    if n ==0:
        fd(size)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            koch(size/3,n-1)
def Kmain():
    setup(600,600)
    speed(100)
    penup()
    goto(-200,100)
    pendown()
    pensize(2)
    level=3
    for i in range(3):
        koch(400,level)
        right(120)
    first()
    hideturtle()
def first():
    penup()
    goto(0,0)
    pendown()
    write("2018-8-26", align="center", font=("Courier", 17, "bold"))
    penup()
    fd(20)
    pendown()
    write("我们相遇", align="center", font=("Courier", 17, "bold"))

# 移动距离，但是不绘制
def Skip(step):
    penup()
    forward(step)
    pendown()


# 画表盘
def DrawClock(radius):
    reset()  # 将乌龟返回初始位置
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i%5 == 0:
            forward(20)
            Skip(-radius - 20)
        else:
            dot(5)  # 绘制圆点turtle.dot(直径)
            Skip(-radius)
        right(6)


def mkHand(name, length):
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    '''''
    begin_poly -- 开始记录，end_poly -- 结束记录,get_poly -- 绘画记录点
    '''
    register_shape(name, handForm)  # 给handForm形状起名


def Init():
    global secHand, minHand, hurHand, printer  # 定义这三个是全局变量
    mode("logo")
    '''''
    三种模式：standard，logo,world。
                turtle方向    默认运动方向
    standard:    向右（朝东）  逆时针
    logo    :    向上（朝北）  顺时针
    world -- 自定义
    '''
    mkHand("secHand", 125)
    mkHand("minHand", 130)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")  # 对于该turtle变量赋值形状
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)  # 调整三根指针的粗细
        hand.speed(0)
    printer = Turtle()
    printer.hideturtle()  # 隐藏箭头
    printer.penup()


def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)

def howday(t):
    past = datetime.strptime('2018-8-26 13:14:00','%Y-%m-%d %H:%M:%S')#过去时间
    now = datetime.now()#当前时间
    delta = now - past#求时间差
    printer.write(("爱我宝贝的第"+str(delta.days)+"天"),align="center",font=("Courier", 14, "bold"))
# 钟表更新
def Tick():
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)  # 重新设置朝向，设置指针的方向角度
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    tracer(False)
    printer.forward(65)  # 前进65写星期
    printer.write(Week(t), align="center", font=("Courier", 14, "bold"))
    printer.back(130)   # 退后130写时间
    printer.write(Date(t), align="center", font=("Courier", 14, "bold"))
    # write函数中可以把指定的内容进行书写
    printer.forward(300)
    howday(t)
    printer.back(800)
    printer.write("爱你如一",align="center",font=("Courier", 14, "bold"))

    printer.home()
    tracer(True)
    ontimer(Tick, 100)  # 计时函数用来控制刷新时间。单位-毫秒


def main():
    tracer(False)  # 关闭绘画追踪，可以用于加速绘画复杂图形
    Init()
    DrawClock(160)
    tracer(True)
    Tick()
    mainloop()  # mainloop则是主窗口的成员函数，
    # 开始接收鼠标的和键盘的操作。你现在就能够通过鼠标缩放以及关闭这个窗口了。

Kmain()
time.sleep(0.5)
rose()
time.sleep(1.5)
reset()
if __name__ == "__main__":
    main()
