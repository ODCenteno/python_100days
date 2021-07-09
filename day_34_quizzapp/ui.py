from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 18, "italic")

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")
        # self.minsize = self.window.minsize(width=400, height=525)

        # LABELS
        self.score_label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=20, padx=20)

        # CANVAS
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quote_text = self.canvas.create_text(
            150,
            125,
            text="question",
            font=FONT,
        )
        self.canvas.config(background="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)


        # Buttons
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_image = PhotoImage(file="./images/true.png")

        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)

        self.true_button = Button(image=self.true_image, bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(column=0, row=2, pady=20, padx=20)

        
        self.window.mainloop()

