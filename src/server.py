from routers import CategoryRouter, MainRouter, QuizRouter
from views import CategoryView, MainView, QuizView


def category_app() -> None:
    main = CategoryRouter().main()['main']

    if not main:
        print("No Category option selected")

    elif main[0] == "CREATE":
        create = CategoryRouter().create()
        name = create['name']

        if name:
            if CategoryView().create(name):
                print("OK")
            else:
                print("create ERROR")
        else:
            print("name ERROR")

    elif main[0] == "READ":
        rows = CategoryView().read_all()

        if rows:
            MainRouter().category(rows)
        else:
            print("read ERROR")

    elif main[0] == "UPDATE":
        rows = CategoryView().read_all()
        row_id = MainRouter().category(rows)['id']

        if row_id:
            id = row_id[0].split(' - ')[0].strip()

            update = CategoryRouter().update(id)

            if CategoryView().update(id, **update):
                print("OK")
            else:
                print("update ERROR")

        else:
            print("row selection ERROR")

    elif main[0] == "DELETE":
        rows = CategoryView().read_all()
        row_id = MainRouter().category(rows)['id']

        if row_id:
            id = row_id[0].split(' - ')[0].strip()

            delete = CategoryRouter().delete(id)['DELETE']

            if delete:
                if CategoryView().delete(int(id)):
                    print("OK")
                else:
                    print("Ok - no row affected")
            else:
                print("No row affected")
        else:
            print("row selection ERROR")

    return


def quiz_app() -> None:
    main = QuizRouter().main()['main']

    if not main:
        print("No Quiz option selected")

    elif main[0] == "CREATE":
        rows = CategoryView().read_all()

        if not rows:
            create = CategoryRouter().create()
            name = create['name']

            if name:
                if CategoryView().create(name):
                    rows = CategoryView().read_all()
                else:
                    print("name ERROR - No name for Category")
            else:
                print("create ERROR - every quiz needs a Category")

        row_id = MainRouter().category(rows)['id']

        if row_id:
            cat_id = row_id[0].split(' - ')[0].strip()

            create = QuizRouter().create()

            if all(create.values()):
                question = create['question']
                options = create['options']
                answer = create['answer']

                if QuizView().create(cat_id, question, options, answer):
                    print("OK")
                else:
                    print("create ERROR")
            else:
                print(
                    "fields ERROR - question, option and answer is required to create a quiz")

        else:
            print("row selection ERROR - category is required")

    elif main[0] == "READ":
        rows = QuizView().read_all()

        if rows:
            MainRouter().quiz(rows)
        else:
            print("read ERROR")

    elif main[0] == "UPDATE":
        rows = QuizView().read_all()
        row_id = MainRouter().quiz(rows)['quiz']

        if row_id:
            print(row_id)

            id = row_id[0].split(' - ')[0].strip()

            update = QuizRouter().update(id)
            update = {k: v for k, v in update.items() if v}

            if update and all(update.values()):

                if QuizView().update(id, **update):
                    print("OK")
                else:
                    print("update ERROR")
            else:
                print("update ERROR - at least a field is needed for update")

        else:
            print("row selection ERROR")

    elif main[0] == "DELETE":
        rows = QuizView().read_all()
        row_id = MainRouter().quiz(rows)['id']

        if row_id:
            id = row_id[0].split(' - ')[0].strip()

            delete = QuizRouter().delete(id)['DELETE']

            if delete:
                if QuizView().delete(id):
                    print("OK")
                else:
                    print("Ok - no row affected")
            else:
                print("No row affected")
        else:
            print("row selection ERROR")

    return


def play_app() -> None:

    def start_game(questions):
        results = list(MainRouter().play_quiz(questions).values())

        answers = [question['answer'] for question in questions]

        response = MainView().evaluate_result((results, answers))

        print(f"RESULTS: {response['scores']}/{response['total']}")
        print(response['message'])

    play = MainRouter().play()['play']

    if not play:
        print("Exiting, no Play option selected.")
        return

    option = play[0].split(" - ")[0].strip()

    if "CATEGORY" == option:
        rows = MainView().category()
        cat = MainRouter().category(rows)['id']

        if not cat:
            print("No Category selected")
            return

        cat_id = cat[0].split(" - ")[0]
        quizzes = MainView().quiz()

        questions = [quiz for quiz in quizzes
                     if quiz['cat_id'] == int(cat_id)]

        if not questions:
            print("Question is not selected.")
            return

        start_game(questions)

    elif "QUIZ" == option:
        rows = MainView().quiz()
        row_ids = MainRouter().quiz(rows)['id']

        if row_ids:
            quizzes = MainView().quiz()

            questions = [quizzes[int(row_id.split(' - ')[0].strip())]
                         for row_id in row_ids]

            if not questions:
                print("Question is not selected.")
                return

            start_game(questions)

        else:
            print("row selection ERROR")

    elif "RANDOM" == option:
        questions = MainView().random()

        if not questions:
            print("Question is not selected.")
            return

        start_game(questions)
    return


def app() -> None:

    res = MainRouter().main()['main']

    if not res:
        print("No Main option selected")

    elif res[0] == "ADMIN":
        admin = MainRouter().admin()['admin']

        if not admin:
            print("No Admin option selected")

        elif admin[0] == 'Category':
            return category_app()
        elif admin[0] == 'Quiz':
            return quiz_app()

    elif res[0] == "PLAY":
        return play_app()

    return


if __name__ == "__main__":
    app()
