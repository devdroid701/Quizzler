import html
from data import GenerateData

from question_model import Question

class QuizBrain:

    def __init__(self):

        self.question_number = 0
        self.score = 0
        self.ques_gen()
        self.question_list = self.question_bank

        self.current_question = None

    def ques_gen(self):
        question_data = GenerateData().question_data
        self.question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_bank.append(new_question)

        self.question_list = self.question_bank

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        #  user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        #  self.check_answer(user_answer)
        return f"Q.{self.question_number}: {q_text}"
        
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False 

    def reset_brain(self):
        self.question_number = -1
        self.score = -1
        self.current_question = None
        self.ques_gen()
        self.next_question()
