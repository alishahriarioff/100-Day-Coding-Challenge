class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = str(input(f"Q.{self.question_number}: {current_question.text}. (True/False): ")).lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, currect_answer):
        if user_answer == currect_answer.lower():
            print("You Got It Right! :)")
            self.score += 1
        else:
            print("You Got It Wrong! :(")
        print(f"The currect Answer Was: {currect_answer}")
        print(f"Your Current Score Is: {self.score}/{self.question_number}")
        print("\n")