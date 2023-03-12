from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.display()
        self.hideturtle()

    def display(self):
        self.clear()
        self.write(f'Score: {self.score}  Highscore: {self.highscore}', align='center', font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.display()

    '''def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=("Arial", 24, "normal"))'''

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.display()

    def update_highscore(self):
        with open("data.txt", mode='r') as file:
            self.highscore = file.read()
            self.display()
