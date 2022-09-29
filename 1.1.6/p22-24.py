import turtle as trtl
painter = trtl.Turtle()
# Spider abdomen
painter.pensize(40)
painter.circle(20)
# Configure legs
legs = 6
leg_length = 70
angle = 380 / legs
painter.pensize(5)
rep = 0
# Drawing legs
while (rep < legs):
  painter.goto(0,0)
  painter.setheading(angle*rep)
  painter.forward(leg_length)
  rep = rep + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
