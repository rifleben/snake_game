import time
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

turtle_list = []

game_on = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food, wall, and self:

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for turtle in snake.turtle_list[1:]:
        if snake.head.distance(turtle) < 10:
            game_on = False
            score.game_over()



screen.exitonclick()
