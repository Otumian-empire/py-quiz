from inquirer import Confirm, prompt, Text, Checkbox


class CategoryRouter:

    def main(self) -> dict:
        questions = [
            Checkbox(
                name="main",
                message="SELECT A CATEGORY OPTION:",
                choices=["CREATE", "READ", "UPDATE",  "DELETE"])
        ]

        return prompt(questions)

    def create(self) -> dict:
        questions = [
            Text(name="name", message="Enter category name"),
        ]

        return prompt(questions)

    def update(self, id) -> dict:
        questions = [
            Text(name="name",
                 message=f"Enter new name for category with ID={id}")
        ]

        return prompt(questions)

    def delete(self, id) -> dict:
        questions = [
            Confirm(
                name="DELETE",
                message=f"Delete Category with ID {id}",
                default=True)
        ]

        return prompt(questions)
