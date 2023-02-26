from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lb = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_lb.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_question = self.canvas.create_text(150, 125, width=280, text="Question here.",
                                                       font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_img = PhotoImage(file="images/true.png")
        self.true_bt = Button(image=true_img, highlightthickness=0, command=self.true_click)
        self.true_bt.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_bt = Button(image=false_img, highlightthickness=0, command=self.false_click)
        self.false_bt.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lb.config(text=f"Score: {self.quiz.score}")
            new_question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question, text=new_question)
        else:
            self.canvas.itemconfig(self.canvas_question, text="You've reached the end of the quiz.")
            self.true_bt.config(state="disabled")
            self.false_bt.config(state="disabled")

    def true_click(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_click(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

