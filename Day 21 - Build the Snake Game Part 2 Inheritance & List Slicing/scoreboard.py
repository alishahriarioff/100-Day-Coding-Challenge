from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, "center", ("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", False, "center", ("Courier", 24, "bold"))
        #TODO ->
        # self.goto(0, -30)
        # self.color("yellow")
        # self.write("Press 'C' To Continue Or 'Q' To Quit The Game.", False, "center", ("Courier", 12, "bold"))
    

    def increce_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()