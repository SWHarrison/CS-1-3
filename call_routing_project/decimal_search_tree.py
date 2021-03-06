import pickle, time

class DecimalTreeNode(object):

    def __init__(self, data):
        """Initialize this Decimal tree node with the given data."""
        self.data = data
        self.nexts = [None] * 10

    def __repr__(self):
        """Return a string representation of this Decimal tree node."""
        return 'DecimalTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        for next in self.nexts:
            if next != None:
                return False

        return True


    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return not self.is_leaf()

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best case: O(1) when node is a leaf
        Worst case: O(n) when node is root and n is items in tree"""
        if(self.is_leaf()):  # base case
            return 0

        heights = []
        for next in self.nexts:
            if(next != None):
                heights.append(next.height())

        max_height = max(heights)

        return 1 + max_height  # visit current node

class DecimalSearchTree(object):

    def __init__(self):
        """Initialize this Decimal search tree and insert the given items."""
        self.root = DecimalTreeNode('+')
        self.size = 0
        self.num_nodes = 0

    def __repr__(self):
        """Return a string representation of this Decimal search tree."""
        return 'DecimalSearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this Decimal search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best case: O(1) when root is a leaf
        Worst case: O(n) when node is root and n is items in tree"""
        if(not self.is_empty()):
            return self.root.height()

        return None

    def contains(self, number, node):
        """Return True if this Decimal search tree contains the given number.
        Best case: O(1) when root has the number
        Worst case: O(log n) when node is lowest level of tree"""
        if(len(number) == 0):
            return True

        digit = number[0]
        remainder = number[1:]

        if(node.nexts[digit] != None):
            self.contains(remainder, node.nexts[digit])
        else:
            return False

    def search(self, number):

        return self._search(number, self.root)

    def _search(self, number, node):
        """Return an number in this Decimal search tree matching the given number,
        or None if the given number is not found.
        Best case: O(1) when root has the number
        Worst case: O(log n) when node is lowest level of tree"""
        if(len(number) == 0):
            print("returning node data ", node.data)
            return node.data

        digit = int(number[0])
        remainder = number[1:]

        if(node.nexts[digit] != None):
            return self._search(remainder, node.nexts[digit])
        else:
            return None

    def insert(self, number, data):

        #print("inserting base: ",number)
        self._insert(number, data, self.root)

    def _insert(self, number, data, node):
        """Insert the given number in order into this Decimal search tree.
        Best case: O(1) when adding to empty tree
        Worst case: O(log n) when node is lowest level of tree"""
        # Handle the case where the tree is empty
        if(len(number) == 0):
            if(node.data == None):
                self.size += 1
                node.data = data
            elif(node.data > data):
                node.data = data
            return

        digit = int(number[0])
        remainder = number[1:]

        if(node.nexts[digit] == None):
            node.nexts[digit] = DecimalTreeNode(None)
            self.num_nodes += 1
        self._insert(remainder, data, node.nexts[digit])

    def replace(self, number, data):

        self._replace(number, data, self.root)

    def _replace(self, number, data, node):
        """Insert the given number in order into this Decimal search tree.
        Best case: O(1) when adding to empty tree
        Worst case: O(log n) when node is lowest level of tree"""
        # Handle the case where the tree is empty
        if(len(number) == 0):
            node.data = data
            return

        digit = int(number[0])
        remainder = number[1:]

        if(node.nexts[digit] == None):
            raise KeyError ('Number not in tree')
        self._replace(remainder, data, node.nexts[digit])

    def find_price(self, number):

        current_best_price = None
        node = self.root
        digit = int(number[0])
        remainder = number[1:]
        while(node.nexts[digit] != None):
            #print("current best price is",current_best_price)
            node = node.nexts[digit]
            if(node.data != None):
                current_best_price = node.data

            #print("remainder of number is", remainder)
            if(len(remainder) > 0):
                digit = int(remainder[0])
                remainder = remainder[1:]
            else:
                break

        #print("returning best price as",current_best_price)
        return current_best_price


if __name__ == '__main__':

    current = time.perf_counter()
    file = open('route-costs-10000000.txt','r')
    read_numbers = file.readlines()
    file.close()
    print(time.perf_counter()-current)



    tree = DecimalSearchTree()

    for number in read_numbers:
        split_number = number.strip().split(',')
        phone_num = split_number[0][1:]
        cost = float(split_number[1])
        #print(phone_num)
        #print(cost)
        tree.insert(phone_num,cost)

    print(tree.size)
    print(tree.num_nodes)
    print(time.perf_counter()-current)
    pickle.dump(tree, open( "save.p", "wb" ))
    #tree = pickle.load( open( "save.p", "rb" ) )
    #print("time to load:",time.perf_counter()-current)
    '''print(tree.size)

    file = open('phone-numbers-10000.txt','r')
    read_numbers = file.readlines()
    file.close()

    file2 = open('phone-numbers-10000-test.txt',"w")

    for number in read_numbers:
        number = number.strip()
        phone_num = number[1:]
        cost = tree.find_price(phone_num)
        file2.write(phone_num + " cost: " + str(cost)+"\n")

    file2.close()
    print("time to check numbers:",time.perf_counter()-current)'''
