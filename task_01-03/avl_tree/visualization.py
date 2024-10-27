"""
Модуль для побудови та візуалізації дерева з використанням бібліотеки NetworkX.
"""

import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph: nx.DiGraph, node, pos: dict, x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    """
    Додає ребра до графа для представлення дерева.

    :param graph: Граф, до якого будуть додані ребра.
    :param node: Поточний вузол дерева.
    :param pos: Словник, що містить позиції вузлів.
    :param x: Поточна координата x.
    :param y: Поточна координата y.
    :param layer: Номер шару, на якому розташований вузол.
    :return: Оновлений граф.
    """
    if node is not None:
        graph.add_node(node.key, label=node.key)
        if node.left:
            graph.add_edge(node.key, node.left.key)
            l = x - 1 / 2 ** layer
            pos[node.left.key] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.key, node.right.key)
            r = x + 1 / 2 ** layer
            pos[node.right.key] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, width: int = 40, height: int = 12, margin: float = 0) -> None:
    """
    Візуалізує дерево, зберігаючи зображення в PNG форматі.

    :param tree_root: Корінь дерева, яке потрібно візуалізувати.
    :param width: Ширина фігури для візуалізації.
    :param height: Висота фігури для візуалізації.
    :param margin: Відстань між краями графа і краями фігури.
    """
    tree = nx.DiGraph()
    pos = {tree_root.key: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(width, height))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=500,
            node_color="skyblue",
            font_size=9,
            font_color="black"
           )

    plt.xlim(-1 - margin, 1 + margin)
    plt.savefig('task_01-03/tree_visualization.png', format='png', bbox_inches='tight')
    plt.close()
