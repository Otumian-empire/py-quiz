from models import Category


class CategoryView:

    def create(self, name) -> bool:
        try:
            return Category().create(name)
        except:
            return False

    def read_one(self, id) -> list:
        try:
            return Category().read().one(id)
        except:
            return []

    def read_all(self) -> list:
        try:
            return Category().read().all()
        except:
            return []

    def update(self, id, **kwargs) -> bool:
        try:
            return Category().update(id, **kwargs)
        except:
            return False

    def delete(self, id) -> bool:
        try:
            return Category().delete(id)
        except:
            return False
