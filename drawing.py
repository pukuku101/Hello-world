import turtle as trtl

painter = trtl.Turtle()
painter.color("black")
painter.sety(-500)
painter.begin_fill()
painter.circle(500)
painter.end_fill()
painter.sety(0)
painter.fillcolor("yellow")
#the head
painter.penup()
painter.goto(-45,30)
painter.pendown()
painter.begin_fill()
painter.circle(30)
painter.end_fill()
painter.penup()
painter.goto(0,0)
painter.pendown()
painter.begin_fill()
painter.circle(50)
painter.end_fill()
painter.penup()
painter.goto(45,30)
painter.pendown()
painter.begin_fill()
painter.circle(30,240,16)
painter.end_fill()
#Details
painter.fillcolor("black")
painter.pu()
painter.goto(-10,20)
painter.pd()
painter.begin_fill()
painter.circle(10)
painter.end_fill()
painter.pu()
#Eyes
painter.setx(-25)
painter.sety(70)
painter.pd()
painter.begin_fill()
painter.circle(7)
painter.end_fill()
painter.pu()
painter.setx(-5)
painter.pd()
painter.begin_fill()
painter.circle(7)
painter.end_fill()
painter.pu()
painter.color("blue")
painter.fillcolor("blue")
painter.setx(-22)
painter.sety(68)
painter.pd()
painter.begin_fill()
painter.circle(2)
painter.end_fill()
painter.pu()
painter.setx(-3)
painter.pd()
painter.begin_fill()
painter.circle(2)
painter.end_fill()
#end of program
wn = trtl.Screen()
wn.bgcolor("black")
wn.mainloop()
