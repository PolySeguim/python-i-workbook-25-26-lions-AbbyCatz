import turtle

screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightgreen")

#global variable
abby = turtle.Turtle()


abby.speed(5)
abby.shape("turtle")
abby.color("blue")

def draw_Clock():
    for i in range(12):
        abby.stamp()
        abby.penup()
        abby.forward(100)
        abby.pendown()
        abby.forward(30)
        abby.penup()
        abby.backward(130)
        abby.left(30)
#draw_Clock()



"""
for i in range(number):
    draw_Clock()
    if shape == 1.0:
        distance = distance + 5
screen.mainloop()

    #forwardNumber = float(input("How far forward? "))
    distance = 15
    for i in range(20):
        abby.forward(distance)
        abby.right(90)
        #newForwardNumber = forwardNumber + 20
        #abby.forward(newForwardNumber)
        distance = distance + 5
        




screen.listen()
screen.mainloop()

"""


def draw_Clock(t):
    for i in range(12):
        t.stamp()
        t.penup()
        t.forward(100)
        t.pendown()
        t.forward(30)
        t.penup()
        t.backward(130)
        t.left(30)
    
def draw_multicolor_square(t, sz, colors):
    t.pensize(getThickness())
    for i in colors:
        t.color(i)
        t.forward(sz)
        t.left(90)
        
def getThickness():
    thickness = int(input("Enter the thickness of the turtle"))
    return thickness

def test():
    test_turtle = turtle.Turtle()
    test_turtle.color("pink")
    #draw_Clock(test_turtle)
    color1 = ["red", "purple", "hotpink", "blue"]
    color2 = ["black", "orange", "green", "yellow"]
    color3 = ["purple", "red", "gray", "brown"]
    draw_multicolor_square(test_turtle, 20, color1)
    draw_multicolor_square(test_turtle, 50, color2)
    draw_multicolor_square(test_turtle, 100, color3)

#test()

#screen.listen()
#screen.mainloop()


def myFunction():
    iterations = int(input("How many iterations do you want? "))
    for i in range (5):
        for i in range(4): 
            abby.pendown()
            abby.forward(50)
            abby.left(90)
        abby.left(180)
        abby.penup()
        abby.forward(25)
        abby.right(90)      
#myFunction()
    