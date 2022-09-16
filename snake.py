from turtle import Turtle

START = [(0 , 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for item in START:
            self.add_turtle(item)

    def move(self):
        for turtle in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle - 1].xcor()
            new_y = self.turtle_list[turtle - 1].ycor()
            self.turtle_list[turtle].goto(new_x, new_y)

        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def add_turtle(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.color("white")
        turtle.shape("square")
        turtle.goto(position)
        self.turtle_list.append(turtle)

    def grow(self):
        self.add_turtle(self.turtle_list[-1].position())