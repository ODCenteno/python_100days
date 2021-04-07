# from main import question_bank

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        # self.right_answer = r_answer
        self.score = 0

        # TODO: asking the questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. \nType True/False: ").lower().strip()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer.lower():
            print(f"You got it right!")
            self.score += 1
        else:
            print(f"That's wrong.")
            print(f"Your score is {self.score}/{self.question_number}")
        print(f"Your score is {self.score}/{self.question_number}")
        print(F"The correct answer was: {str(current_answer)}.\n\n")

    def end(self):
        print(f'Congratulations, you did it to the end!')
        print(f"Your final score was: {self.score}/{self.question_number}")