from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = '#66A3A7'

class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(height=250, width=300, bg='white', borderwidth=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='some question text',
            fill='#2E5793',
            font=('Arial', 20, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        correct_image = PhotoImage(file='images/true.png')
        self.correct = Button(image=correct_image, highlightthickness=0, command=self.correct_pressed)
        self.correct.grid(row=3, column=0)

        wrong_image = PhotoImage(file='images/false.png')
        self.wrong = Button(image=wrong_image, highlightthickness=0, command=self.wrong_pressed)
        self.wrong.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='QUIZ OVER')
            self.correct.config(state='disabled')
            self.wrong.config(state='disabled')

    def correct_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)


    def wrong_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='#3cb371') #green
        else:
            self.canvas.config(bg='#f08080') #red
        self.window.after(1000, self.get_next_question)




