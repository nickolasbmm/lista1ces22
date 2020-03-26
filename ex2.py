import turtle

def draw_poly(t,n,sz):
    #Make a turtle t draw a n-sided polygon of side-length sz
    for _ in range(n):
        t.forward(sz)
        t.left(360/n)


#Create screen object
wn=turtle.Screen()

#Create turtle object
t=turtle.Turtle()

#Set background color and pen color
wn.bgcolor("lightgreen")
t.color("hotpink")
t.width(3)

#Draw polygon of n=8 and sz=50
draw_poly(t,8,50)


wn.mainloop()