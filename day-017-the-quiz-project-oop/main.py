from rsc.Data import question_data
from rsc.QuestionModel import Question

questions = []

for data in question_data:
    questions.append(Question(**data))

questions[0].printData() 