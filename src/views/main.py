from models import Category, Quiz
from random import choice


class MainView:
    def category(self) -> list:
        return Category().read().all()

    def quiz(self) -> list:
        return Quiz().read().all()

    def random(self) -> None:
        """ Returns a random question  """
        return [choice(Quiz().read().all())]

    def evaluate_result(self, results: tuple) -> dict:
        """ Evaluate the result from the Test """
        scores = 0
        message = ""

        answers, correct_answers = results

        number_of_questions = len(correct_answers)

        for i in range(number_of_questions):
            message += str(i+1)

            correct_answer = correct_answers[i]
            answer = answers[i]

            if answer and (answer[0] == correct_answer):
                message += " C"
                scores += 1
            else:
                message += " Inc"

            message += f"orrect Ans:[{correct_answer}]"
            message += "\n"

        return {
            "scores": scores,
            "total": number_of_questions,
            "message": message
        }
