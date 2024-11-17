from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-270,270)
        self.level = 1
        self.update_level()


    def increase_level(self):
        self.level = self.level + 1
        self.update_level()


    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=(FONT))
    


