from tkinter import *
from quiz_brain import QuizBrain
from time import sleep

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 18, "italic")

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = quiz.score
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")
        # self.minsize = self.window.minsize(width=400, height=525)

        # LABELS
        self.score_label = Label(text=f"score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=20, padx=20)

        # CANVAS
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quote_text = self.canvas.create_text(
            150,
            125,
            width= 280,    # Set max with and fit text inside the canvas
            text="question",
            font=FONT,
        )
        self.canvas.config(background="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)


        # Buttons
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_image = PhotoImage(file="./images/true.png")

        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)

        self.true_button = Button(image=self.true_image, bg=THEME_COLOR, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=0, row=2, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Get the question text from the instance QuizBrain that was passed as parameter.
        To really read the instance and use the method you need to define the parameter type
        importing the class from the quiz_brain file"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}/10")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text="You reach the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def check_answer_false(self, user_answer="False"):
        result = self.quiz.check_answer(user_answer)
        self.give_feedback(result)


    def check_answer_true(self, user_answer="True"):
        result = self.quiz.check_answer(user_answer)
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question) #    Equivalent to time.sleep() but using to work inside window.mainloop()



