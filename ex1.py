import turtle

def draw_square(t,sz):
    #Make a turtle t draw a square of size sz
    for _ in range(4):
        t.forward(sz)
        t.left(90)


#Create screen object
wn=turtle.Screen()

#Create turtle object
t=turtle.Turtle()

#Set background color and pen color
wn.bgcolor("lightgreen")
t.color("hotpink")
t.width(3)

#For loop to draw all the squares

for i in range(20,120,20):
    draw_square(t,i)
    t.up()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.down()


wn.mainloop()