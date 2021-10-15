import sys
from glob import glob

import inquirer

from utils import clear_screen, create_question

if __name__ == '__main__':
    # categories, create file, exit
    questions_dir = "questions/"
    question_files = glob(f"{questions_dir}*")

    categories = sorted([category.split("/")[1]
                         for category in question_files])

    categories += ['create question', 'exit']

    # display the categories
    questions = [
        inquirer.List("option",
                      message="Choose a category for a question, create a question or exit",
                      choices=categories,
                      ),
    ]
    user_answer = inquirer.prompt(questions)

    option = user_answer.get('option')

    if not option or option == 'exit':
        sys.exit()
    elif option == 'create question':
        # import create question and pass the category (option) to it
        create_question(option)
    else:
        # proceed with the Quiz

        print(user_answer)

    # get the category from the questions category
    # if category is not given the create
