from binary_tree import BinaryTreeNode
from queue import Queue
from stack import Stack

class TreeMap(object):

    def __init__(self, items = None):

        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.size == 0

    def keys(self):

        items = self.items()
        keys = []
        for item in items:
            keys.append(item[0])

        return keys

    def values(self):

        items = self.items()
        values = []
        for item in items:
            values.append(item[1])

        return values

    def items(self):

        items = self.items_in_order()
        return items

    def contains(self, key):
        """Return True if this binary search tree contains the given item.
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(key, self.root)
        # Return True if a node was found, or False
        return node is not None

    def set(self, key, value):
        """Insert the given item in order into this binary search tree.
        Best case: O(1) when adding to empty tree
        Worst case: O(log n) when node is lowest level of tree"""
        # Handle the case where the tree is empty
        key_value = (key, value)

        if self.is_empty():
            self.root = BinaryTreeNode(key_value)
            self.size += 1
            return
        parent = self._find_parent_node_recursive(key, self.root)
        if key < parent.data[0]:
            if(parent.left == None):
                self.size += 1
                parent.left = BinaryTreeNode(key_value)
            else:
                parent.left.data = key_value

        elif key > parent.data[0]:
            if(parent.right == None):
                self.size += 1
                parent.right = BinaryTreeNode(key_value)
            else:
                parent.right.data = key_value

    def get(self, key):
        """Insert the given item in order into this binary search tree.
        Best case: O(1) when adding to empty tree
        Worst case: O(log n) when node is lowest level of tree"""
        # Handle the case where the tree is empty
        node = self._find_node_recursive(key, self.root)

        print(node)
        if(node == None):
            raise KeyError ("Key not in map!")
        return node.data[1]

    def _find_node_iterative(self, key):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data[0] == key:
                return node
            elif node.data[0] > key:
                node = node.left
            elif node.data[1] < key:
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, key, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of a full tree
        O(n) for a tree with only 1 path"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        elif node.data[0] == key:
            # Return the found node
            return node
        elif key < node.data[0]:
            return self._find_node_recursive(key, node.left)
        elif key > node.data[0]:
            return self._find_node_recursive(key, node.right)

    def _find_parent_node_iterative(self, key):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data[0] == key:
                # Return the parent of the found node
                return parent
            elif key < node.data[0]:
                parent = node
                node = node.left
            elif key > node.data[0]:
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, key, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion).
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        if node.data[0] == key:
            # Return the parent of the found node
            return parent

        elif key < node.data[0]:
            parent = node
            return self._find_parent_node_recursive(key, node.left, parent)
        elif key > node.data[0]:
            parent = node
            return self._find_parent_node_recursive(key, node.right, parent)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case: O(1) when root has the item and tree is otherwise empty
        Worst case: O(log n) when predecessor/successor is in lowet level of tree"""

        #parent = self._find_parent_node_iterative(item)
        parent = self._find_parent_node_recursive(item, self.root)
        node = None
        if(parent == None):
            #node = self._find_node_iterative(item)
            node = self._find_node_recursive(item, self.root)
        elif(item < parent.data):
            node = parent.left
        else:
            node = parent.right
        print("Node is",node)
        if(node == None):
            raise ValueError("Item not in tree!")

        if(node.is_leaf()):
            print(node, "is leaf")
            if(node == self.root):
                self.root = None
                return

            if(node.data < parent.data):
                parent.left = None
            else:
                parent.right = None

        elif(node.is_branch()):
            print(node, "is branch")

            #find predecessor
            if(node.left != None):
                current = node.left
                parent = node
                while(not current.is_leaf()):
                    parent = current
                    current = current.right

                node.data = current.data
                if(parent != node):
                    parent.right = None
                else:
                    parent.left = None

            #find successor
            else:
                current = node.right
                parent = node
                while(not current.is_leaf()):
                    parent = current
                    current = current.left

                node.data = current.data
                if(parent != node):
                    parent.left = None
                else:
                    parent.right = None


    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        if(node is not None):
            self._traverse_in_order_recursive(node.left, visit)
            visit(node.data)
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            if(stack.peek().left != None):
                stack.push(stack.peek().left)
            else:
                node = stack.pop()  # child of next node to be popped
                visit(node.data)
                if(not stack.is_empty() and node.right == None):
                    node = stack.pop()  # parent of node previously popped
                    visit(node.data)
                if(node.right is not None):
                    stack.push(node.right)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
            #self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        if(node is not None):
            visit(node.data)
            self._traverse_pre_order_recursive(node.left, visit)
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            node = stack.pop()
            visit(node.data)
            if(node.right != None):
                stack.push(node.right)
            if(node.left != None):
                stack.push(node.left)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []  # original
        def array_prepend(item):  # closure on items variable
            items.insert(0, item)  # O(n) -- too slow

        llist = LinkedList()  # linked version
        def llist_prepend(item):  # closure on llist variable
            llist.prepend(item)  # O(1) -- fast

        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)  # original
            #self._traverse_post_order_iterative(self.root, array_prepend)  # hacked version
            #self._traverse_post_order_iterative(self.root, llist_prepend)  # linked version
            # items = self._traverse_post_order_iterative(self.root)
        # Return post-order list of all items in tree
        # return items  # original
        return llist.items()  # linked version  # O(n)

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        if(node is not None):
            self._traverse_post_order_recursive(node.left, visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit = None):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        # Unused code using set to ensure no duplicates
        '''stack = Stack()
        stack.push(node)
        visited = set()
        while not stack.is_empty():
            if(stack.peek().left != None and stack.peek().left.data not in visited):
                stack.push(stack.peek().left)
            elif(stack.peek().right != None and stack.peek().right.data not in visited):
                stack.push(stack.peek().right)
            else:
                node = stack.pop()
                visit(node.data)
                visited.add(node.data)'''

        #items = [None] * self.size

        #i = self.size
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            #i -= 1
            node = stack.pop()
            #items[i] = node.data
            visit(node.data)
            if(node.left != None):
                stack.push(node.left)
            if(node.right != None):
                stack.push(node.right)

        #return items

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to 2 to the power of heigh of tree,
        as it must fully traverse node and store it's children, meaning
        the queue at one point stores every node in the bottom level, which
        has a max number of nodes of 2^h """
        queue = Queue()
        queue.enqueue(start_node)
        while not queue.is_empty():
            node = queue.dequeue()
            visit(node.data)
            if(node.left != None):
                queue.enqueue(node.left)
            if(node.right != None):
                queue.enqueue(node.right)
