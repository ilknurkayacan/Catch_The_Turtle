import turtle
import time
from random import random, randint


window=turtle.Screen()
tur_ins=turtle.Turtle()
score=0
timer_t=turtle.Turtle()
timer_t.hideturtle()
window.bgcolor("light blue")
window.title("Catch The Turtle")
tur_ins.shape('turtle')
tur_ins.color("green")
tur_ins.penup()

list=["red","purple","blue","green","orange","yellow"]

def calis(x,y):
    tur_ins.penup()
    if tur_ins.xcor() > 200 or tur_ins.xcor() < -200:
        tur_ins.home()
    if tur_ins.ycor() > 200 or tur_ins.ycor() < -200:
        tur_ins.home()
    def catchturtle(x,y):
        global score
        score += 1
        print(score)

    k=randint(0,5)
    tur_ins.color(list[k])
    i=randint(0,6)

    if i==0:
        tur_ins.forward(100)
    elif i==1:
        tur_ins.backward(100)
    elif i==2:
        tur_ins.left(45)
        tur_ins.forward(100)
    elif i==3:
        tur_ins.left(45)
        tur_ins.backward(100)
    elif i == 4:
        tur_ins.right(45)
        tur_ins.forward(100)
    elif i == 5:
        tur_ins.right(45)
        tur_ins.backward(100)

    tur_ins.onclick(catchturtle)


time_off=5


style=("courier",20,"italic")
x_coordinates = [-10, 0, 10]
y_coordinates = [10, 0, -10]


while True:
    timer_t.clear()
    timer_t.hideturtle()
    timer_t.penup()
    timer_t.setposition(0, 240)

    timer_t.write(f"Time: {time_off}", font=style, align='center')

    for x in x_coordinates:
        for y in y_coordinates:
            calis(x, y)

    time_off -= 1
    if time_off==0:
        timer_t.clear()
        timer_t.write(f"Time: {time_off}", font=style, align='center')
        break

timer_t.hideturtle()
tex=turtle.Turtle()
tex.hideturtle()
tex.penup()
tex.setposition(0,-240)
tex.write(f"Time Finished\nScore: {score}",font=style,align='center')



print(window.window_width())

window.mainloop()