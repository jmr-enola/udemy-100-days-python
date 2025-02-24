from typing import List
from rsc.QuestionModel import Question

class QuizBrain:
    
    def __init__(self, q_list:List[Question]) -> None:
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def nextQuestion(self) -> bool:
        ans = input(f"Q.{self.q_num + 1} {self.q_list[self.q_num].text}. (True/False)? ").lower()
        
        if self.q_list[self.q_num].answer.lower() == ans:
            self.score += 1

        self.q_num += 1
        
        return self.q_num < len(self.q_list) 

        

