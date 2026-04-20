from turtle import *


class Face:

    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
  
    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
      
        pensize(5)

    def goHome(self):
        penup()
        goto(self.coord)
        
        setheading(0)
        
    def drawOutline(self):
        penup()
        # move turtle pen in forward direction 
        forward(self.size)
        left(90)
        # draw a circle of given radius
        pendown()
        circle(self.size)
        # return back to centre
        self.goHome()

    def drawEye(self, turn):
        penup()
        # turn turtle pen to given angle
        left(turn)
        # move turtle pen in forward direction
        forward(self.size / 2)
        pendown()
        # draw a cirle of given radius
        dot(self.size/10)
        # return back to centre
        self.goHome()
        
    def drawMouth(self):
        penup()
        # turn turtle pen to given angle
        right(135)
        # move turtle pen in forward direction
        forward(self.size/1.7)
        left(90)
        pendown()
        # draw a circle of given radius
        # but till given extent only 
        circle(self.size/1.7,90)
       

 

#  start of drawing code
#  ---------------------
  
f1 = Face(0, 0)
f1.draw()

showturtle()
done()

