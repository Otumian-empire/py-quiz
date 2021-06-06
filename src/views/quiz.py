from models import Quiz


class QuizView:

    def create(self, *args) -> bool:
        try:
            return Quiz().create(*args)
        except:
            return False

    def read_one(self, id) -> list:
        try:
            return Quiz().read().one(id)
        except:
            return False

    def read_all(self) -> list:
        try:
            return Quiz().read().all()
        except:
            return False

    def update(self, id, **kwargs) -> bool:
        try:
            return Quiz().update(id, **kwargs)
        except:
            return False

    def delete(self, id) -> bool:
        try:
            return Quiz().delete(id)
        except:
            return False
