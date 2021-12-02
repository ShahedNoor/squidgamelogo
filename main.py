import turtle as t

#Pen Position Start From Here.
t.penup()
t.goto(-400, -100)
t.pendown()
#Position End.

#Triangle Start From Here.
t.pen(pencolor="red", fillcolor="red", pensize=7)
t.begin_fill()
t.fd(200)
t.lt(120)
t.fd(200)
t.lt(120)
t.fd(200)
t.lt(120)
t.end_fill()
#Triangle End.

#Pen Position Start From Here.
t.penup()
t.goto(0, -100)
t.pendown()
#Position End.

#Circle Star From Here.
t.pen(pencolor="green", pensize=7, fillcolor="green", speed=10)
t.begin_fill()
t.circle(90)
t.end_fill()
#Circle End.

#Pen Position Start From Here.
t.penup()
t.goto(235, -100)
t.pendown()
#Positon End.

#Squre Start From Here.
t.pen(pencolor="red", fillcolor="red")
t.begin_fill()
t.fd(160)
t.lt(90)
t.fd(160)
t.lt(90)
t.fd(160)
t.lt(90)
t.fd(160)
t.lt(90)
t.end_fill()
#Squre End.
