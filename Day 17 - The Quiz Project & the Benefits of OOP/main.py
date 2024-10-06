from data import question_data2
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

question_bank = []

print(logo)
for item in question_data2:
    question = Question(q_text=item["question"], q_answer=item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You Have Completed The Quiz.")
print(f"You'r Final Score is {quiz.score}/{quiz.question_number}")