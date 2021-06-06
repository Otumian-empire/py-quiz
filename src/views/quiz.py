from models import Quiz


class QuizView:
    def create(self, **kwarg):
        try:
            return Quiz().create(**kwarg)
        except:
            return False

    def read_one(self, id):
        try:
            return Quiz().read().one(id)
        except:
            return False

    def read_all(self, id=None):
        try:
            return Quiz().read().all()
        except:
            return False

    def update(self, id, **kwargs):
        try:
            return Quiz().update(id, **kwargs)
        except:
            return False

    def delete(self, id):
        try:
            return Quiz().delete(id)
        except:
            return False
