from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk() 
        self.window.title("Quizzler")
        self.window.config(pady=150,padx=20, bg=THEME_COLOR) 
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, font=("Arial", 20, "italic"), text="Random question", fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)
    

        self.true_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.true_img, highlightthickness=0, command=self.correct_ans)
        self.correct_button.grid(column=0, row=2, pady=20)


        self.false_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.false_img, highlightthickness=0, command=self.default_ans)
        self.wrong_button.grid(column=1, row=2, pady=20)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.reset_img = PhotoImage(file="images/false.png")
        self.reset_button= Button(image=self.reset_img, command=self.reset_game)
        # self.reset_button.grid(column=1, row=3)

        

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.reset_button.config(state="disabled")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
        #  self.window.after_cancel(self.timer)
            q_text = self.quiz.next_question()
            
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

            self.reset_button.config(state="active")
    
    def default_ans(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def correct_ans(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.score_board() 

    def give_feedback(self, is_right):
        self.timer = self.window.after(ms=1000, func=self.get_next_question)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def score_board(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
    
    def reset_game(self):
        self.quiz.score=0
        self.quiz.reset_brain() 
        self.correct_button.config(state="active")
        self.wrong_button.config(state="active")
