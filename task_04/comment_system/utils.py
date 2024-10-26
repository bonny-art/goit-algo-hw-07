"""
Модуль для обробки коментарів та відповідей у ієрархії коментарів.

Цей модуль містить функцію для збору всіх коментарів, включаючи їхні відповіді, у один список.
"""
from .comment import Comment

def collect_all_comments(comment: 'Comment', all_comments: list) -> None:
    """
    Збирає всі коментарі та їх відповіді у один список.

    Args:
        comment (Comment): Коментар, з якого починається збір.
        all_comments (list): Список, в який будуть додані всі коментарі та їх відповіді.

    Returns:
        None: Функція не повертає значення, результат зберігається в `all_comments`.
    """
    all_comments.append(comment)
    for reply in comment.replies:
        collect_all_comments(reply, all_comments)
