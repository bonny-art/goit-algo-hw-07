"""
Модуль для роботи з AVL-деревом, включаючи генерацію випадкових ключів
та їх вставку у дерево. Реалізує методи обходу дерева та обчислення
найбільших і найменших значень, а також суму всіх значень у дереві.
"""

from avl_tree.avl_tree import AVLTree
from avl_tree.helpers import generate_random_keys

def main():
    """
    Головна функція для створення та управління AVL-деревом.

    Генерує випадкові ключі, вставляє їх у AVL-дерево, виконує обходи дерева,
    знаходить найбільше і найменше значення, а також обчислює суму всіх значень.
    """
    tree = AVLTree()
    root = None

    # Параметри для генерації
    num_keys = 100  # Кількість чисел
    min_value = 1  # Мінімальне значення
    max_value = 1000  # Максимальне значення

    # Генерація випадкових чисел
    keys = generate_random_keys(num_keys, min_value, max_value)
    print("\nГенеровані ключі:")
    print(keys)

    # Вставка елементів у AVL-дерево
    for key in keys:
        root = tree.insert(root, key)

    # Обхід дерева
    print("\nПрямий обхід AVL-дерева:")
    tree.pre_order_traversal(root)
    print("\n\nЦентровий обхід AVL-дерева:")
    tree.in_order_traversal(root)
    print("\n\nЗворотній обхід AVL-дерева:")
    tree.post_order_traversal(root)

    # Знаходження найбільшого та найменшого значень
    print("\n\nНайбільше значення в дереві:", tree.find_max(root))
    print("Найменше значення в дереві:", tree.find_min(root))

    # Обчислення суми всіх значень у дереві
    print("\nСума всіх значень в дереві:", tree.sum_values(root))

    # todo: add visualization of tree with blue circules and lines

if __name__ == "__main__":
    main()
