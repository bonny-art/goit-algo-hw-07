"""
Модуль для системи коментарів, що реалізує ієрархічну структуру коментарів із відповідями.

Цей модуль містить функцію main для генерації коментарів, видалення випадкових коментарів
та виведення структури коментарів на екран.
"""

import random
from typing import List
from comment_system.generator import generate_comments
from comment_system.utils import collect_all_comments
from comment_system.comment import Comment


def main(num_comments: int, num_to_remove: int) -> None:
    """
    Основна функція для генерації коментарів, видалення випадкових коментарів
    та виведення структури коментарів.

    Параметри:
    num_comments (int): Загальна кількість коментарів для генерації.
    num_to_remove (int): Кількість коментарів, які слід видалити.
    """
    root_comment = generate_comments(num_comments)

    # Збираємо всі коментарі у список
    all_comments: List[Comment] = []
    collect_all_comments(root_comment, all_comments)

    # Вибираємо випадкові коментарі для видалення
    active_comments = [c for c in all_comments if not c.is_deleted]
    for _ in range(min(num_to_remove, len(active_comments))):
        random_comment = random.choice(active_comments)
        random_comment.remove_reply()

    # Виведення всієї ієрархії коментарів
    root_comment.display()

if __name__ == "__main__":
    total_comments = 20  # Задайте кількість коментарів
    comments_to_remove = 5  # Задайте кількість коментарів для видалення
    main(total_comments, comments_to_remove)
