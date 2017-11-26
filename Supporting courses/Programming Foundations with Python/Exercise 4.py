import turtle

#draw squere
def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")
    #create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(3)
    draw_square(brad)
    #create turtle angie
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

draw_art()