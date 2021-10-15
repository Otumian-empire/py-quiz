from glob import glob
from random import choice

import inquirer


if __name__ == "__main__":
    questions = [
        inquirer.List("category",
                      message="Select question category",
                      choices=["Math", "CS", "Random"],),
    ]

    questions_dir = "questions/"
    category = inquirer.prompt(questions).get("category").lower()

    question_files = glob(f"{questions_dir}*")

    print(question_files)

    if category == "random":
        category_file = choice(question_files)
    else:
        category_file = f"{questions_dir}{category}_questions"

    print(category, category_file)

    with open(category_file, 'r') as fp:
        for category_question in fp.readlines():
            key, question, options, answer = category_question.split(';')

            questions = [
                inquirer.List(str(key),
                              message=str(question),
                              choices=[option.strip()
                                       for option in options.split(":")],
                              ),
            ]

            user_answer = inquirer.prompt(questions)[key]

            if answer == user_answer:
                print("Correct")
            else:
                print("Incorrect")
