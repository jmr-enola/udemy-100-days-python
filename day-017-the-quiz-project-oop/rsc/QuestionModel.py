class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def printData(self):
        print(self.text)
        print(self.answer)