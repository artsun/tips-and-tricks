
//  Двоичное дерево:
//  - у каждого узла не более двух дочерних узлов; целочисленные значения в узлах
//
//  Двоичное дерево поиска:
//  - для ЛЮБОГО узла дерева
//    - его значение БОЛЬШЕ значений ВСЕХ узлов его левого поддерева
//    - его значение МЕНЬШЕ или РАВНО значений ВСЕХ узлов его правого поддерева
//
//  Написать проверку является ли двоичное дерево деревом поиска 

class Node:
    value: int 
    left: Node
    right: Node


def is_tree(node: Node) -> bool:

    if node.left is not None:
        if not (node.value >= node.left.value):
            return False
    
    if node.right is not None:
        if not node.value < node.right.value:
        return False
    
    if node.left is None and node.right is None:
        return True
    
    for nd in [node.left, node.right]:
        if not is_tree(nd):
            return False
    
    return True

    





