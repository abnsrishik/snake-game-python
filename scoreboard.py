from turtle import Turtle
COORDINATES = (0,270)
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(COORDINATES)
        self.update_score()


    def update_score(self):
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg= "GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 15, "normal"))

