from inquirer import Confirm, prompt, Text, Checkbox


class QuizRouter:

    def main(self) -> dict:
        questions = [
            Checkbox(
                name="main",
                message="SELECT A QUIZ OPTION:",
                choices=["CREATE", "READ", "UPDATE",  "DELETE"])
        ]

        return prompt(questions)

    def create(self) -> dict:
        questions = [
            Text(name="question", message="Enter question"),
            Text(name="options", message="Enter options"),
            Text(name="answer", message="Enter answer")
        ]

        return prompt(questions)

    def update(self, id) -> dict:
        questions = [
            Text(
                name="question",
                message=f"Enter new question for quiz with ID={id}"),

            Text(
                name="options",
                message=f"Enter new options for quiz with ID={id}"),

            Text(
                name="answer",
                message=f"Enter new answer for quiz with ID={id}")
        ]

        return prompt(questions)

    def delete(self, id) -> dict:
        questions = [
            Confirm(
                name="DELETE", message=f"Delete Quiz with ID {id}", default=True)
        ]

        return prompt(questions)
