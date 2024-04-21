from turtle import *
tracer(0)
left(90)
down()
screensize(3000, 3000)
k = 30

left(15)
for i in range(7):
    left(30)
    forward(10*k)
    left(60)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(5)
done() #Answer: 98