class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        number_of_questions = len(self.question_list)
        return number_of_questions > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Acertou!")
            self.score += 1
        else:
            print("Errou")
        print(f"A resposta certa é {correct_answer}")
        print(f"Seu score é: {self.score}/{self.question_number}")
        print("\n")

    def end_of_quiz(self):
        print("Acabou o teste")
        print(f"Seu score final foi {self.score}/{self.question_number}")
