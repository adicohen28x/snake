from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.num = 0
        with open("data.txt") as highscore:
            self.high_score = int(highscore.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear() 
        self.write(f"score:{self.num}    High Score:{self.high_score}", align='center', font=('Arial', 10, 'normal'))

    def increase_score(self):
        self.num += 1
        self.update_score()

    def reset(self):
        if self.num > self.high_score:
            with open("data.txt", mode="w") as highscore:
                highscore.write(f"{self.num}")
        self.num = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align='center', font=('Arial', 10, 'normal'))
