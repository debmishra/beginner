import turtle
import time

my_turtle = turtle.Turtle()

def square() :

    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
#    my_turtle.right(90)
#    my_turtle.forward(100)

#square()
#my_turtle.forward(100)
#square()

#if 1 > 2:
#   square()
#else:
#   my_turtle.forward(100)


# While true:
#  ## do something

for i in range(4):
    square()

time.sleep(5)