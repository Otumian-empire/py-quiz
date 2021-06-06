from inquirer import Checkbox, prompt


class MainRouter:

    def main(self) -> dict:
        questions = [
            Checkbox(
                name="main",
                message="SELECT AN OPTION:",
                choices=["ADMIN", "PLAY",  "EXIT"])
        ]

        return prompt(questions)

    def admin(self) -> dict:
        questions = [
            Checkbox(
                name="admin",
                message="SELECT AN OPTION:",
                choices=["Category", "Quiz"])
        ]

        return prompt(questions)

    def play(self) -> dict:
        questions = [
            Checkbox(
                name="play",
                message="PLAY BY:",
                choices=[
                    "CATEGORY - select all quizzes from a category",
                    "QUIZ - select a particular question",
                    "RANDOM - select a random question"])
        ]

        return prompt(questions)

    def quiz(self, quizzes) -> dict:
        questions = [
            Checkbox(
                name="id",
                message="CHOOSE QUIZ:",
                choices=[
                    f"{row['id']} - {row['question']}"
                    for row in quizzes])
        ]

        return prompt(questions)

    def category(self, categories) -> dict:

        questions = [
            Checkbox(
                name="id",
                message="CHOOSE CATEGORY:",
                choices=[
                    f"{row['id']} - {row['name']}"
                    for row in categories])
        ]

        return prompt(questions)
