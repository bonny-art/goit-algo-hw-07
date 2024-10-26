"""
Модуль для генерації коментарів.

Цей модуль містить функцію для створення ієрархії коментарів, 
використовуючи випадкові дані, згенеровані за допомогою бібліотеки Faker.
"""

import random
from .comment import Comment
from faker import Faker

fake = Faker()

def generate_comments(num_comments: int) -> Comment:
    """
    Генерує ієрархію коментарів з випадковими даними.

    Аргументи:
    num_comments (int): Кількість коментарів для генерації.

    Повертає:
    Comment: Кореневий коментар з усіма його відповідями.
    """
    root_comment = Comment(fake.sentence(), fake.name())
    comments = [root_comment]

    for _ in range(num_comments - 1):
        parent = random.choice(comments)  # Вибір випадкового батьківського коментаря
        new_comment = Comment(fake.sentence(), fake.name())  # Генерація нового коментаря
        parent.add_reply(new_comment)  # Додавання нової відповіді
        comments.append(new_comment)

    return root_comment
