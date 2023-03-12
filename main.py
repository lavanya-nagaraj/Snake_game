from turtle import Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(600, 600)
screen.title('Snake Game')
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_highscore()
level = screen.textinput('Select Level', 'Easy or Difficult').lower()
if level == 'easy':
    timing = 0.2
else:
    timing = 0.1

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


is_move = True
while is_move:
    screen.update()
    time.sleep(timing)
    snake.move()
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

        # is_move = False
        # scoreboard.game_over()

    if snake.head.distance(food) < 15:
        scoreboard.increase()
        food.refresh()
        snake.extend()

    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < len(snake.segment):
            scoreboard.reset()
            snake.reset()

            # is_move = False
            # scoreboard.game_over()


screen.exitonclick()
