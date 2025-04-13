from turtle import Turtle, Screen

def draw_polygon(edge:int, n_sides:int=3):
    
    if n_sides < 3:
        n_sides = 3

    turtle = Turtle()

    heading = 0
    heading_increment = 180 - ((n_sides - 2) * 180 / n_sides)

    while n_sides > 0:
        turtle.setheading(heading)
        turtle.forward(edge)
        n_sides -= 1
        heading += heading_increment

if __name__ == "__main__":
    draw_polygon(50, 3)
    draw_polygon(50, 4)
    draw_polygon(50, 5)
    draw_polygon(50, 6)

    screen = Screen()
    screen.screensize(300, 300)
    screen.listen()
    screen.exitonclick()

    