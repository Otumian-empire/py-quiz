from inquirer import Confirm, prompt, Text, Checkbox


class CategoryRouter:

    def main(self) -> dict:
        """
        >>> Category().main()
        Returns a dictionary with key, main.
        Displays a checkbox based question with choices to pick from.        
        """

        questions = [
            Checkbox(
                name="main",
                message="SELECT A CATEGORY OPTION:",
                choices=["CREATE", "READ", "UPDATE",  "DELETE"])
        ]

        return prompt(questions)

    def create(self) -> dict:
        """ 
        >>> Category().create()
        Displays a text field which accepts input for the category name and returns a dictionary witk key, name
        """

        questions = [
            Text(name="name", message="Enter category name"),
        ]

        return prompt(questions)

    def update(self, id) -> dict:
        """ 
        >>> Category().update(id: int)
        Accpets int argument, id which is used in the message
        Displays a text field which accepts input for the category name and returns a dictionary witk key, name
        """

        questions = [
            Text(name="name",
                 message=f"Enter new name for category with ID={id}")
        ]

        return prompt(questions)

    def delete(self, id) -> dict:
        """ 
        >>> Category().delete(id: int)
        Accpets int argument, id which is used in the message
        Displays a confirm field which accepts input to delete category and returns a dictionary witk key, DELETE
        """

        questions = [
            Confirm(
                name="DELETE",
                message=f"Delete Category with ID {id}",
                default=True)
        ]

        return prompt(questions)
