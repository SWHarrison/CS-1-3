#!python

from decimal_search_tree import DecimalSearchTree, DecimalTreeNode
import unittest


class DecimalTreeNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = DecimalTreeNode(data)
        assert node.data is data
        for next in node.nexts:
            assert next is None

    def test_is_leaf(self):
        # Create node with no children
        node = DecimalTreeNode(2)
        assert node.is_leaf() is True
        # Attach 1st child node
        node.nexts[1] = DecimalTreeNode(1)
        assert node.is_leaf() is False
        # Attach 3rd child node
        node.nexts[3] = DecimalTreeNode(3)
        assert node.is_leaf() is False
        # Detach 1st child node
        node.nexts[1] = None
        assert node.is_leaf() is False
        # Detach 3rd child node
        node.nexts[3] = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = DecimalTreeNode(2)
        assert node.is_branch() is False
        # Attach 1st child node
        node.nexts[1] = DecimalTreeNode(1)
        assert node.is_branch() is True
        # Attach 3rd child node
        node.nexts[3] = DecimalTreeNode(3)
        assert node.is_branch() is True
        # Detach 1st child node
        node.nexts[1] = None
        assert node.is_branch() is True
        # Detach 3rd child node
        node.nexts[3] = None
        assert node.is_branch() is False

    def test_height(self):
        # Create node with no children
        node = DecimalTreeNode(4)
        assert node.height() == 0
        # Attach left child node
        node.nexts[2] = DecimalTreeNode(2)
        assert node.height() == 1
        # Attach right child node
        node.nexts[6] = DecimalTreeNode(6)
        assert node.height() == 1
        # Attach left-left grandchild node
        node.nexts[2].nexts[1] = DecimalTreeNode(1)
        assert node.height() == 2
        # Attach right-right grandchild node
        node.nexts[6].nexts[8] = DecimalTreeNode(8)
        assert node.height() == 2
        # Attach right-right-left great-grandchild node
        node.nexts[2].nexts[1].nexts[7] = DecimalTreeNode(7)
        assert node.height() == 3


class DecimalSearchTreeTest(unittest.TestCase):

    def test_init(self):
        tree = DecimalSearchTree()
        assert tree.root.data == '+'
        assert tree.size == 0
        assert tree.is_empty() is False

    def test_insert_with_phone_numbers(self):
        tree = DecimalSearchTree()
        assert tree.size == 0
        assert tree.is_empty() is False
        tree.insert('000',0.50)
        assert tree.size == 1
        assert tree.root.nexts[0].data is None
        assert tree.root.nexts[0].nexts[0].data is None
        assert tree.root.nexts[0].nexts[0].nexts[0].data == 0.50
        tree.insert('001',0.05)
        assert tree.size == 2
        assert tree.root.nexts[0].data is None
        assert tree.root.nexts[0].nexts[0].data is None
        assert tree.root.nexts[0].nexts[0].nexts[1].data == 0.05
        tree.insert('01',0.06)
        assert tree.size == 3
        assert tree.root.nexts[0].data is None
        assert tree.root.nexts[0].nexts[0].data is None
        assert tree.root.nexts[0].nexts[1].data == 0.06
        tree.insert('0',0.08)
        assert tree.size == 4
        assert tree.root.nexts[0].data == 0.08
        tree.insert('00',0.09)
        assert tree.size == 5
        assert tree.root.nexts[0].data == 0.08
        assert tree.root.nexts[0].nexts[0].data == 0.09
        assert tree.root.nexts[0].nexts[1].data == 0.06
        tree.insert('00',0.4)
        assert tree.size == 5
        assert tree.root.nexts[0].data == 0.08
        assert tree.root.nexts[0].nexts[0].data == 0.4
        assert tree.root.nexts[0].nexts[1].data == 0.06
        for i in range(1,10):
            assert tree.root.nexts[i] is None

    def test_search_with_phone_numbers(self):
        tree = DecimalSearchTree()
        assert tree.size == 0
        assert tree.is_empty() is False
        tree.insert('000',0.50)
        tree.insert('001',0.05)
        tree.insert('01',0.06)
        tree.insert('0',0.08)
        tree.insert('00',0.09)
        assert tree.search('000') == 0.50
        assert tree.search('001') == 0.05
        assert tree.search('01') == 0.06
        assert tree.search('00') == 0.09
        assert tree.search('0') == 0.08
        assert tree.search('1') == None
        assert tree.search('02') == None
        assert tree.search('002') == None


    def test_find_price(self):
        tree = DecimalSearchTree()
        tree.insert('000',0.50)
        tree.insert('001',0.05)
        tree.insert('01',0.06)
        tree.insert('0',0.08)
        tree.insert('00',0.09)
        assert tree.find_price('0') == 0.08
        assert tree.find_price('00') == 0.09
        assert tree.find_price('000') == 0.50
        assert tree.find_price('001') == 0.05
        assert tree.find_price('04') == 0.08

    '''def test_search_with_3_items(self):
        # Create a complete Decimal search tree of 3 items in level-order
        items = [2, 1, 3]
        tree = DecimalSearchTree(items)
        assert tree.search(1) == 1
        assert tree.search(2) == 2
        assert tree.search(3) == 3
        assert tree.search(4) is None

    def test_search_with_7_items(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = DecimalSearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search(8) is None

    def test_search_with_3_strings(self):
        # Create a complete Decimal search tree of 3 items in level-order
        items = ['B', 'A', 'C']
        tree = DecimalSearchTree(items)
        assert tree.search('A') == 'A'
        assert tree.search('B') == 'B'
        assert tree.search('C') == 'C'
        assert tree.search('D') is None

    def test_search_with_7_strings(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = ['D', 'B', 'F', 'A', 'C', 'E', 'G']
        tree = DecimalSearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search('H') is None

    def test_insert_with_3_items(self):
        # Create a complete Decimal search tree of 3 items in level-order
        tree = DecimalSearchTree()
        tree.insert(2)
        assert tree.root.data == 2
        assert tree.root.left is None
        assert tree.root.right is None
        tree.insert(1)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right is None
        tree.insert(3)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3

    def test_insert_with_7_items(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = DecimalSearchTree()
        for item in items:
            tree.insert(item)
        assert tree.root.data == 4
        assert tree.root.left.data == 2
        assert tree.root.right.data == 6
        assert tree.root.left.left.data == 1
        assert tree.root.left.right.data == 3
        assert tree.root.right.left.data == 5
        assert tree.root.right.right.data == 7

    def test_delete_with_3_items(self):
        # Create a complete Decimal search tree of 3 items in level-order
        items = [2, 1, 3]
        tree = DecimalSearchTree(items)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3
        tree.delete(2)
        assert tree.root.data == 1
        assert tree.root.left is None
        assert tree.root.right.data is 3
        tree.delete(1)
        assert tree.root.data == 3
        assert tree.root.left is None
        assert tree.root.right is None
        tree.delete(3)
        assert tree.root is None

    def test_delete_with_7_items(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = DecimalSearchTree(items)
        tree.delete(4)
        assert tree.root.data == 3
        assert tree.root.left.data == 2
        assert tree.root.right.data == 6
        assert tree.root.left.left.data == 1
        assert tree.root.left.right is None
        tree.delete(6)
        assert tree.root.data == 3
        assert tree.root.left.data == 2
        assert tree.root.right.data == 5
        assert tree.root.right.left is None
        assert tree.root.right.right.data == 7
        tree.delete(5)
        assert tree.root.data == 3
        assert tree.root.left.data == 2
        assert tree.root.right.data == 7
        assert tree.root.right.left == None
        assert tree.root.right.right == None

    def test_delete_with_unbalanced_trees(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [3, 6, 1, 2, 5, 7]
        tree = DecimalSearchTree(items)
        tree.delete(2)
        assert tree.root.data == 3
        assert tree.root.left.data == 1
        assert tree.root.right.data == 6
        assert tree.root.left.left is None
        assert tree.root.left.right is None

    def test_items_in_order_with_3_strings(self):
        # Create a complete Decimal search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = DecimalSearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == ['A', 'B', 'C']

    def test_items_pre_order_with_3_strings(self):
        # Create a complete Decimal search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = DecimalSearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == ['B', 'A', 'C']

    def test_items_post_order_with_3_strings(self):
        # Create a complete Decimal search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = DecimalSearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == ['A', 'C', 'B']

    def test_items_level_order_with_3_strings(self):
        # Create a complete Decimal search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = DecimalSearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == ['B', 'A', 'C']

    def test_items_in_order_with_7_numbers(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [5, 3, 1, 2, 4, 7, 6, 8]
        tree = DecimalSearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_items_pre_order_with_7_numbers(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = DecimalSearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == [4, 2, 1, 3, 6, 5, 7]

    def test_items_post_order_with_7_numbers(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = DecimalSearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == [1, 3, 2, 5, 7, 6, 4]

    def test_items_level_order_with_7_numbers(self):
        # Create a complete Decimal search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = DecimalSearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]'''


if __name__ == '__main__':
    unittest.main()
