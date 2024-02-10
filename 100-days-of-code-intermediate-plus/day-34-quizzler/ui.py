from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="initial text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0/0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "normal"))
        self.score_label.grid(row=0, column=1)

        true_button_image = PhotoImage(file="images/true.png")
        false_button_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=true_button_image,
            width=100,
            height=100,
            highlightthickness=0,
            command=self.answer_true
        )
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(
            image=false_button_image,
            width=100,
            height=100,
            highlightthickness=0,
            command=self.answer_false
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def answer_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)