from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.resizable(False, False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.quiz = quiz

        self.score_board = Label(text= "Score: 0", font=("Arial", 12), background=THEME_COLOR, fg="white")
        self.score_board.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="The Question Place Holder", font=("Arial", 16, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_image = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=check_image, highlightthickness=0, border=False, command=self.is_true)
        self.true_btn.grid(column=0, row=2)
        
        cross_image = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=cross_image, highlightthickness=0, border=False, command=self.is_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        