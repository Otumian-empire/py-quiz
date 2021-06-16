import os
from settings import DATABASE


def placeholder_update(keys: list) -> str:
    """ 
    >>> placeholder_update(keys: list) -> str
    >>> keys = ['full_name', 'age', 'dob']
    >>> placeholder_update(keys)
    >>> "full_name=?, age=?, dob=?"
    Create places holder for keys with a default delimeter of =? """

    delimeter = "=?"
    res = ""

    for i, v in enumerate(keys):
        res += "".join([v, delimeter])

        if i < len(keys) - 1:
            res += ", "

    return res


def clear_screen():
    """ Clear screen - OS independent """
    os.system('cls' if os.name == 'nt' else 'clear')
