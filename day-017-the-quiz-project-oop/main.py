from rsc.Data import question_data
from rsc.QuestionModel import Question
from rsc.QuizBrain import QuizBrain

questions = []

for data in question_data:
    questions.append(Question(**data))

quiz = QuizBrain(questions)

quiz.nextQuestion()