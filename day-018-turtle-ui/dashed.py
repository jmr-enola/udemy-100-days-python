from turtle import Turtle, Screen

def move_right(turtle:Turtle) -> None:
    turtle.setheading(0)
    dashed_forward(turtle, 25, 5)

def move_up(turtle:Turtle) -> None:
    turtle.setheading(90)
    dashed_forward(turtle, 25, 5)

def move_left(turtle:Turtle) -> None:
    turtle.setheading(180)
    dashed_forward(turtle, 25, 5)

def move_down(turtle:Turtle) -> None:
    turtle.setheading(270)
    dashed_forward(turtle, 25, 5)

def dashed_forward(turtle:Turtle, steps:int, gap:int) -> None:
    distance = steps
    is_pen_down = True
    while (distance > 0):
        if is_pen_down:
            turtle.pendown()
        else:
            turtle.penup()

        turtle.forward(gap)
        distance -= gap
        is_pen_down = not is_pen_down

if __name__ == "__main__":
    slow_poke = Turtle()
    move_down(slow_poke)
    move_left(slow_poke)
    move_up(slow_poke)
    move_right(slow_poke)

    screen = Screen()
    screen.screensize(300, 300)
    screen.listen()
    screen.exitonclick()
    
