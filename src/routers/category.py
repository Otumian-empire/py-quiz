from inquirer import Confirm, prompt, Text, Checkbox


class CategoryRouter:

    def main(self):
        questions = [
            Checkbox(
                name="main",
                message="SELECT A CATEGORY OPTION:",
                choices=["CREATE", "READ", "UPDATE",  "DELETE"],
                default=["CREATE"]),
        ]

        return prompt(questions)

    def create(self):
        questions = [
            Text(name="category", message="Enter category name"),
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
            Text(name="name", message="Enter name"),
        ]

        return prompt(questions)

    def delete(self):
        questions = [
            Text(name="id", message="Enter id"),
        ]

        return prompt(questions)
