from turtle import *
tracer(0)
k = 20
screensize(2000, 2000)
left(90)
up()

for i in range (9):
    forward(15*k)
    right(90)
    forward(25*k)
    right(90)
up()
back(10*k); right(90)
down()
for i in range(8):
    forward(15*k)
    left(90)
    forward(25*k)
    left(90)
up()
forward(6*k); left(90)
down()
for i in range (7):
    forward(15*k)
    right(90)
    forward(25*k)
    right(90)
up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(4)
done()