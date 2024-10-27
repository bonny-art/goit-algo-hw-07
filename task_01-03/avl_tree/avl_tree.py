"""Модуль для реалізації самобалансованого AVL-дерева пошуку.

Цей модуль містить реалізацію AVL-дерева, що підтримує збалансованість при кожній вставці,
гарантуючи час роботи для основних операцій (вставка, пошук, обхід) на рівні O(log n).
"""

from .node import Node

class AVLTree:
    """Клас, що представляє самобалансоване AVL-дерево пошуку.

    AVL-дерево автоматично підтримує баланс після кожної операції вставки,
    виконуючи обертання вузлів. AVL-дерево зберігає різницю висот піддерев
    будь-якого вузла не більше ніж 1, що забезпечує ефективний пошук та обхід.

    Методи:
        insert: Додає новий вузол із зазначеним значенням.
        pre_order_traversal: Виконує обхід дерева в прямому порядку.
        in_order_traversal: Виконує обхід дерева в центрованому порядку.
        post_order_traversal: Виконує обхід дерева в зворотному порядку.
        find_max: Знаходить максимальне значення в дереві.
        find_min: Знаходить мінімальне значення в дереві.
        sum_values: Обчислює суму всіх значень у дереві.
    """
    def __init__(self) -> None:
        """Ініціалізує порожнє AVL-дерево."""
        self.root = None

    def get_height(self, node: Node) -> int:
        """Повертає висоту вузла.

        Args:
            node (Node): Вузол дерева.

        Returns:
            int: Висота вузла, або 0, якщо вузол відсутній.
        """
        return 0 if not node else node.height

    def update_height(self, node: Node) -> None:
        """Оновлює висоту вузла.

        Args:
            node (Node): Вузол дерева, для якого слід оновити висоту.
        """
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node: Node) -> int:
        """Обчислює баланс-фактор вузла.

        Args:
            node (Node): Вузол дерева.

        Returns:
            int: Різниця висот лівого і правого піддерев.
        """
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y: Node) -> Node:
        """Здійснює праве обертання навколо зазначеного вузла.

        Args:
            y (Node): Вузол, навколо якого здійснюється праве обертання.

        Returns:
            Node: Новий корінь піддерева після обертання.
        """
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x: Node) -> Node:
        """Здійснює ліве обертання навколо зазначеного вузла.

        Args:
            x (Node): Вузол, навколо якого здійснюється ліве обертання.

        Returns:
            Node: Новий корінь піддерева після обертання.
        """
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, key: int) -> None:
        """Вставляє новий ключ у AVL-дерево.

        Args:
            key (int): Ключ для вставки в дерево.
        """
        self.root = self._insert(self.root, key)

    def _insert(self, node: Node, key: int) -> Node:
        """Вставляє новий ключ у дерево та виконує балансування.

        Args:
            node (Node): Кореневий вузол дерева або піддерева.
            key (int): Ключ для вставки в дерево.

        Returns:
            Node: Новий корінь піддерева після вставки та балансування.
        """
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def pre_order_traversal(self, root: Node) -> None:
        """Виконує обхід дерева в прямому порядку.

        Args:
            root (Node): Корінь дерева або піддерева.
        """
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def in_order_traversal(self, root: Node) -> None:
        """Виконує обхід дерева в центрованому порядку.

        Args:
            root (Node): Корінь дерева або піддерева.
        """
        if not root:
            return
        self.in_order_traversal(root.left)
        print(f"{root.key} ", end="")
        self.in_order_traversal(root.right)

    def post_order_traversal(self, root: Node) -> None:
        """Виконує обхід дерева в зворотному порядку.

        Args:
            root (Node): Корінь дерева або піддерева.
        """
        if not root:
            return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(f"{root.key} ", end="")

    def find_max(self, root: Node) -> int | None:
        """Знаходить максимальне значення в дереві.

        Args:
            root (Node): Корінь дерева або піддерева.

        Returns:
            int | None: Найбільше значення в дереві або None, якщо дерево порожнє.
        """
        current = root
        while current and current.right:
            current = current.right
        return current.key if current else None

    def find_min(self, root: Node) -> int | None:
        """Знаходить мінімальне значення в дереві.

        Args:
            root (Node): Корінь дерева або піддерева.

        Returns:
            int | None: Найменше значення в дереві або None, якщо дерево порожнє.
        """
        current = root
        while current and current.left:
            current = current.left
        return current.key if current else None

    def sum_values(self, root: Node) -> int:
        """Обчислює суму всіх значень у дереві.

        Args:
            root (Node): Корінь дерева або піддерева.

        Returns:
            int: Сума всіх значень вузлів дерева.
        """
        if root is None:
            return 0
        return root.key + self.sum_values(root.left) + self.sum_values(root.right)
