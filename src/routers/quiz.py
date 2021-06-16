from inquirer import Confirm, prompt, Text, Checkbox


class QuizRouter:

    def main(self) -> dict:
        """
        >>> QuizRouter().main()
        Returns a dictionary with key, main.
        Displays a checkbox based question with choices to pick from.        
        """

        questions = [
            Checkbox(
                name="main",
                message="SELECT A QUIZ OPTION:",
                choices=["CREATE", "READ", "UPDATE",  "DELETE"])
        ]

        return prompt(questions)

    def create(self) -> dict:
        """ 
        >>> QuizRouter().create()
        Displays a text field which accepts input for the quiz name and returns a dictionary witk keys: question, options and answer
        """

        questions = [
            Text(name="question", message="Enter question"),
            Text(name="options", message="Enter options"),
            Text(name="answer", message="Enter answer")
        ]

        return prompt(questions)

    def update(self, id) -> dict:
        """ 
        >>> QuizRouter().update(id: int)
        Accpets int argument, id which is used in the message
        Displays a text field which accepts input for the quiz name and returns a dictionary witk keys: question, options and answer
        """

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
        """ 
        >>> QuizRouter().delete(id: int)
        Accpets int argument, id which is used in the message
        Displays a confirm field which accepts input to delete quiz and returns a dictionary witk key, DELETE
        """

        questions = [
            Confirm(
                name="DELETE", message=f"Delete Quiz with ID {id}", default=True)
        ]

        return prompt(questions)
