from turtle import *
tracer(0)
left(90)
down()
screensize(3000, 3000)
k = 30

for i in range(4):
    forward(3*k)
    left(270)
    forward(5*k)
    right(90)
left(270)
for i in range(3):
    forward(5*k)
    right(90)
    forward(3*k)
    left(270)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(5)
done() #Answer: 42