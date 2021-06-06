from models import Category


class CategoryView:
    def create(self, cat_name):
        try:
            return Category().create(cat_name)
        except:
            return False

    def read_one(self, id):
        try:
            return Category().read().one(id)
        except:
            return False

    def read_all(self, id=None):
        try:
            return Category().read().all()
        except:
            return False

    def update(self, id, **kwargs):
        try:
            return Category().update(id, **kwargs)
        except:
            return False

    def delete(self, id):
        try:
            return Category().delete(id)
        except:
            return False
