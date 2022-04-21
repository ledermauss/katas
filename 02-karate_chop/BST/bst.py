class Node:
    def __init__(self, left, root, right):
        self.root = root
        self.left = left
        self.right = right
        self.index = None # should store the index we are actually returning

    def __eq__(self, other):
        if not isinstance(other, Node): 
            return NotImplemented
        return self.root == other.root \
            and self.left == other.left \
            and self.right == other.right 


class Element:
    def __init__(self, idx, element):
        self.idx = idx
        self.element = element

    def __eq__(self, other):
        if not isinstance(other, Element): 
            return NotImplemented
        return self.idx == other.idx \
            and self.element == other.element


def chop(element, sorted_list):
    bst = create_BST_from_sorted_list(sorted_list)
    return search(bst, element)


def create_BST_from_sorted_list(sorted_list):
    indexed_elements = []
    for idx, element in enumerate(sorted_list):
        indexed_elements.append(Element(idx, element))
    return create_BST_from_sorted_list_with_indexes(indexed_elements)


def create_BST_from_sorted_list_with_indexes(sorted_list):
    if (len(sorted_list)) == 0:
        return None
    mid = len(sorted_list) // 2
    root = Node(None, sorted_list[mid], None)
    if len(sorted_list) == 1:
        return root
    left = sorted_list[:mid]
    root.left = create_BST_from_sorted_list_with_indexes(left)
    right = sorted_list[mid+1:]
    root.right = create_BST_from_sorted_list_with_indexes(right)
    return root
        

def search(bst, number):
    if bst is None:
        return -1
    if bst.root.element == number:
        return bst.root.idx
    elif bst.root.element < number:
        return search(bst.right, number)
    elif bst.root.element > number:
        return search(bst.left, number)


def inorder(tree):
    if tree is None:
        return None
    inorder(tree.left)
    print("{}".format(tree.root), end = " ")
    inorder(tree.right)

def preorder(tree):
    if tree is None:
        return None
    print("{}".format(tree.root), end = " ")
    preorder(tree.left)
    preorder(tree.right)
    
def postorder(tree):
    if tree is None:
        return None
    postorder(tree.left)
    postorder(tree.right)
    print("{}".format(tree.root), end = " ")

    
        
