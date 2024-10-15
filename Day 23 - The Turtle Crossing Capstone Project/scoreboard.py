from turtle import Turtle

FONT = ("Courier", 24, "normal")
BOLD_FONT = ("Courier", 28, "bold")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.penup()
        self.level_scoreboard()
        

    def level_scoreboard(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.level += 1
        self.level_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", False, "center", BOLD_FONT)
        self.goto(0, -30)
        self.color("blue")
        self.write(f"Your Final Score is: {self.level}", False, "center", BOLD_FONT)

