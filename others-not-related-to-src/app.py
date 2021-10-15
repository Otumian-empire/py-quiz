import inquirer

if __name__ == '__main__':
    with open('questions/math_questions', 'r') as mq:

        for row in mq.readlines():
            key, question, options, answer = row.split(';')
            questions = [
                inquirer.List(str(key),
                              message=str(question),
                              choices=[option.strip()
                                       for option in options.split(":")],
                              ),
            ]
            user_answer = inquirer.prompt(questions)[key]

            if answer.strip() == user_answer.strip():
                print("Correct")
            else:
                print("Incorrect")
