class Question:

    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

    def printData(self) -> None:
        print(self.text)
        print(self.answer)