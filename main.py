from question_model import Question
from data import question_data

question_bank = []
for questions in question_data:
    question_bank.append(Question(questions["text"], questions["answer"]))
