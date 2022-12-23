from turtle import *

shape("arrow")
screensize(720,630)
setworldcoordinates(0,630,720,0)
speed(5)

up()
goto(520,545)
down()

fillcolor("blue")                   #Shape A
begin_fill()
for i in range(2):
    right(30)
    forward(150)
    right(60)
    forward(300)
    right(90)
end_fill()

up()
goto(500,400)
down()

fillcolor("orange")                #Shape B
begin_fill()
right(90)
forward(170)
left(60)
forward(140)
right(60)
forward(140)
right(120)
forward(290)
right(60)
forward(160)
right(60)
forward(150)
end_fill()

up()
goto(205,545)
setheading(180)
down()

fillcolor("red")                   #Shape A'
begin_fill()
for i in range(2):
    left(30)
    forward(150)
    left(60)
    forward(300)
    left(90)
end_fill()

up()
goto(225,400)
down()

fillcolor("lime")                   #Shape B'
begin_fill()
left(90)
forward(170)
right(60)
forward(140)
left(60)
forward(140)
left(120)
forward(290)
left(60)
forward(160)
left(60)
forward(150)
end_fill()

up()
goto(220,480)
write("MICROSOFT", False, align="left", font=("Arial",34,"normal"))
sety(ycor()+40)
write("Club Pilote Ariana", False, align="left", font=("Arial",26,"normal"))
ht()