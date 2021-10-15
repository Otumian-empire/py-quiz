#################### Installation ####################
# pip install inquirer


#################### sample code ####################

# import inquirer

# if __name__ == '__main__':

#     questions = [
#         inquirer.Text('user', message='Please enter your github username',
#                       validate=lambda _, x: x != '.'),
#         inquirer.Password('password', message='Please enter your password'),
#         inquirer.Text('repo', message='Please enter the repo name',
#                       default='default'),
#         inquirer.Checkbox('topics', message='Please define your type of project?', choices=[
#                           'common', 'backend', 'frontend'], ),
#         inquirer.Text(
#             'organization', message='If this is a repo from a organization please enter the organization name, if not just leave this blank'),
#         inquirer.Confirm(
#             'correct',  message='This will delete all your current labels and create a new ones. Continue?', default=False),
#     ]

#     answers = inquirer.prompt(questions)

#     print(answers)


#################### Question types ####################

# idea = create an array of questions and call the prompt render.
# every question comes with an argument
# question - types
# TEXT 	    Expects a text answer.
# CONFIRM 	Requires a boolean answer.
# LIST 	    Show a list and allow to select just one answer.
# CHECKBOX 	Show a list and allow to select a bunch of them.
# EDITOR 	Expects a text answer, entered through external editor.
# PASSWORD 	Do not prompt the answer.
# PATH 	    Requires valid path and allows additional validations.
# Object(name:required, message)
# Object(name:required, message, choices=[...]) List, Checkbox
# this behaves like a JSON


#################### TEXT ####################

# from inquirer import Text, prompt

# if __name__ == "__main__":
#     # get full name and job title using the Text object
#     questions = [
#         Text(name="full_name", message="What is your full name", default="No name"),
#         Text(name="job_title", message="What is your job title")
#     ]

#     # get the answers for the full_name and the job_title using the prompt
#     # pass the list of questions to the prompt - we'd get a JSON (dict)
#     answers = prompt(questions)

#     for k, v in answers.items():
#         print(k, v)


########## CONFIRM #########

# from inquirer import Confirm, prompt

# if __name__ == "__main__":
#     questions = [
#         Confirm(name="sit", message="May I sit", default=True),
#         Confirm(name="exit_program", message="Should the program end", default=False),
#     ]

#     answer = prompt(questions)
#     print(answer)


########## LIST #########

# from inquirer import List, prompt

# if __name__ == "__main__":
#     choices = ["Python", "C/C++", "Rust", "JavaScript", "Java"]
#     questions = [
#         List(name="best_lang", message="What is the best language",
#              default=choices[-1],  # the last option is the default
#              choices=choices)
#     ]

#     answer = prompt(questions)
#     print(answer)


########## CHECKBOX #########

from inquirer import Checkbox, prompt

if __name__ == "__main__":
    questions = [
        Checkbox(name="bool", message="Which of these will evaluate to True",
                 choices=[1, 0, True, False, -1, "", "Yes", "No"],
                 default=[False, -1])
    ]

    answer = prompt(questions)
    print(answer)
