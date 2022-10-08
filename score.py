from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.num = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score:{self.num}", align='center', font=('Arial', 10, 'normal'))

    def increase_score(self):
        self.num += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Arial', 10, 'normal'))
