from glob import glob


def create_question(category):
    questions_dir = "questions/"
    category_file = f"{questions_dir}{category}_questions"

    # question_files = glob(f"{questions_dir}*")

    with open(category_file, '+a') as fp:
        key = category
        question = input('Enter question: ')

        options = []

        for i in range(4):
            option = input(f"Enter option {i+1}: ")

            if not option:
                break

            options.append(option.strip())

        options = ":".join(options)

        answer = input("Enter answer: ")

        category_question = (
            ";".join([key, question, options, answer])).strip()

        print(category_question, file=fp)
        print("Question added!!!")
