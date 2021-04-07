from data import question_data
from questions import Question
from quiz_brain import QuizBrain

question_bank = []
counter = 1


def generate_bank():
    for i in question_data:
        new_q = Question(i['question'], i['correct_answer'])
        question_bank.append(new_q)
    return question_bank


if __name__ == "__main__":
    question_bank = generate_bank()
    quiz = QuizBrain(question_bank, )

    while quiz.still_has_questions():
        answer = quiz.next_question()

    quiz.end()
