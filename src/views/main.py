from models import Category, Quiz


class MainView:

    def category(self) -> list:
        return Category().read().all()

    def quiz(self) -> list:
        return Quiz().read().all()

    def random(self) -> None:
        pass
