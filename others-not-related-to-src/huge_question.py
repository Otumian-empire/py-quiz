import inquirer

if __name__ == '__main__':

    questions = [
        inquirer.List("answer",
                      message="x = 12; What is x += 3",
                      choices=[3, 4, 9, 15],),
    ]

    answer = inquirer.prompt(questions)#.get("category")

    print(answer)
