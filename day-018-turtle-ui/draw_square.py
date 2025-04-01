from turtle import Turtle, Screen

def move_right(turtle:Turtle) -> None:
    turtle.setheading(0)
    turtle.forward(25)


def move_up(turtle:Turtle) -> None:
    turtle.setheading(90)
    turtle.forward(25)


def move_left(turtle:Turtle) -> None:
    turtle.setheading(180)
    turtle.forward(25)


def move_down(turtle:Turtle) -> None:
    turtle.setheading(270)
    turtle.forward(25)

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
    
