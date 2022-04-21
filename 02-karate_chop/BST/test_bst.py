from bst import *

def test_bst_1_node():
    bst = create_BST_from_sorted_list([0])
    assert bst == Node(None, Element(0, 0), None)

def test_bst_2_node():
    bst = create_BST_from_sorted_list([0, 1])
    assert bst == Node(Node(None, Element(0, 0), None), Element(1, 1), None)

def test_bst_3_node():
    bst = create_BST_from_sorted_list([0, 1, 2])
    assert bst == Node(Node(None, Element(0, 0), None), Element(1, 1), Node(None, Element(2 ,2), None))

def test_bst_4_node():
    bst = create_BST_from_sorted_list([0, 1, 2, 3, 4])
    assert bst == Node(\
                Node(Node(None, Element(0, 0), None), Element(1, 1), None),
                Element(2, 2),
                Node(Node(None, Element(3, 3), None), Element(4, 4), None))

def test_search():
    bst = Node(Node(Node(None, Element(0, 0), None), Element(1, 1), None), 
            Element(8, 2), 
            Node(Node(None, Element(3, 3), None), Element(4, 4), None))
    assert search(bst, 2) == 8

def test_chop():
    assert chop(3, []) == -1
    assert chop(3, [1]) == -1
    assert chop(1, [1]) == 0
    assert chop(1, [1, 3, 5]) == 0
    assert chop(3, [1, 3, 5]) == 1
    assert chop(5, [1, 3, 5]) == 2
    assert chop(0, [1, 3, 5]) == -1
    assert chop(2, [1, 3, 5]) == -1
    assert chop(4, [1, 3, 5]) == -1
    assert chop(6, [1, 3, 5]) == -1
    assert chop(1, [1, 3, 5, 7]) == 0
    assert chop(3, [1, 3, 5, 7]) == 1
    assert chop(5, [1, 3, 5, 7]) == 2
    assert chop(7, [1, 3, 5, 7]) == 3
    assert chop(0, [1, 3, 5, 7]) == -1
    assert chop(2, [1, 3, 5, 7]) == -1
    assert chop(4, [1, 3, 5, 7]) == -1
    assert chop(6, [1, 3, 5, 7]) == -1
    assert chop(8, [1, 3, 5, 7]) == -1

