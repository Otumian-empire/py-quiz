from inquirer import Confirm, prompt, Text, Checkbox


class QuizRouter:

    def main(self):
        questions = [
            Checkbox(
                name="main",
                message="SELECT A QUIZ OPTION:",
                choices=["CREATE", "READ", "UPDATE",  "DELETE"],
                default=["CREATE"]),
        ]

        return prompt(questions)

    def create(self):
        questions = [
            Text(name="cat_id", message="Enter category id"),
            Text(name="question", message="Enter question"),
            Text(name="options", message="Enter options"),
            Text(name="answer", message="Enter answer"),
        ]

        return prompt(questions)

    def read(self):
        questions = [
            Text(name="id", message="Enter category id"),
        ]

        return prompt(questions)

    def update(self):
        questions = [
            Text(name="id", message="Enter id"),
            Text(name="cat_id", message="Enter category id"),
            Text(name="question", message="Enter question"),
            Text(name="options", message="Enter options"),
            Text(name="answer", message="Enter answer"),
        ]

        return prompt(questions)

    def delete(self):
        questions = [
            Text(name="id", message="Enter id"),
        ]

        return prompt(questions)
