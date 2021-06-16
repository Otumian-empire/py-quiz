from routers import quiz
from inquirer import Checkbox, prompt


class MainRouter:

    def main(self) -> dict:
        """    
        >>> MainRouter().main()
        Returns a dictionary with key, main.
        Displays a checkbox based question with choices to pick from.        
        """

        questions = [
            Checkbox(
                name="main",
                message="SELECT AN OPTION:",
                choices=["ADMIN", "PLAY",  "EXIT"])
        ]

        return prompt(questions)

    def admin(self) -> dict:
        """    
        >>> MainRouter().admin()
        Returns a dictionary with key, admin.
        Displays a checkbox based question with choices to pick from.        
        """

        questions = [
            Checkbox(
                name="admin",
                message="SELECT AN OPTION:",
                choices=["Category", "Quiz"])
        ]

        return prompt(questions)

    def play(self) -> dict:
        """    
        >>> MainRouter().play()
        Returns a dictionary with key, play.
        Displays a checkbox based question with choices to pick from.        
        """

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
        """    
        >>> MainRouter().quiz()
        Returns a dictionary with key, main.
        Displays a checkbox based question with choices to pick from.        
        """

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
        """    
        >>> MainRouter().category()
        Returns a dictionary with key, id.
        Displays a checkbox based question with choices to pick from.        
        """

        questions = [
            Checkbox(
                name="id",
                message="CHOOSE CATEGORY:",
                choices=[
                    f"{row['id']} - {row['name']}"
                    for row in categories])
        ]

        return prompt(questions)

    def play_quiz(self, quizzes: list) -> dict:
        """    
        >>> MainRouter().play()
        Returns a dictionary with key, quiz['id] from the quizzes.
        Displays a checkbox based question with choices to pick from.        
        """

        questions = [
            Checkbox(
                name=quiz['id'],
                message=quiz['question'].upper(),
                choices=quiz['options'].split(", "),)
            for quiz in quizzes
        ]

        return prompt(questions)
