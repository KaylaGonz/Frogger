from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1;
        self.penup()
        self.goto(-250, 270)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", True, align="center", font=FONT)

    def level_increase(self):
        self.level += 1
        self.clear()
        self.goto(-250, 270)
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=FONT)