from question_model import Question
from data import GenerateData
from quiz_brain import QuizBrain
from ui import QuizInterface

#  def ques_gen():
    #  question_data = GenerateData().question_data
    #  return question_data
#
#  question_bank = []
#  for question in ques_gen():
    #  question_text = question["question"]
    #  question_answer = question["correct_answer"]
    #  new_question = Question(question_text, question_answer)
    #  question_bank.append(new_question)


quiz = QuizBrain()
quiz_ui = QuizInterface(quiz)

#  while quiz.still_has_questions():
    #  quiz.next_question()

print("You've copleted the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
