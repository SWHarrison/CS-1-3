#!python

from linkedlist import LinkedList
import random, time

class HashTable(object):

    def __init__(self, init_size=64):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0
        self.load = init_size
        self.resize_factor = 0.75

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        return self.size/self.load

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #O(n) as it runs through the entire hash table once, n is number of items in structure.
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #O(n) as it runs through the entire hash table once, n is number of items in structure.
        #Loop through all buckets
        all_values = list()
        for bucket in self.buckets:
            #Collect all values in each bucket
            for key, value in bucket.items():
                all_values.append(value)

        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #O(n) as it runs through the entire hash table once, n is number of items in structure.
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets."""
        # Running time: O(b) Where b is the number of buckets
        '''length = 0
        #Loop through all buckets
        for bucket in self.buckets:
            #Count number of key-value entries in each bucket
            length += bucket.length()

        return length'''

        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(1) in best case where bucket is empty or only has 1 item, O(l) is average case
        #Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        node = self.buckets[index].find(lambda item: item[0] == key)
        return(node != None)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(1) in best case where bucket is empty or only has 1 item, O(l) is average case
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, return value associated with given key
        # Otherwise, raise error to tell user get failed
        index = self._bucket_index(key)
        node_data = self.buckets[index].find(lambda item: item[0] == key)
        if(node_data != None):
            return node_data[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(1) in best case where bucket is empty or only has the the item with matching key
        # O(l) is average case where l is the number of items in structure divided by # of buckets
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, update value associated with given key
        # Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key)
        node = self.buckets[index]._find_node(lambda item: item[0] == key)
        if(node == None):
            node_data = (key,value)
            self.buckets[index].append(node_data)
            self.size += 1
        else:
            node.data = (key,value)

        if(self.load_factor() > self.resize_factor):
            self.resize()

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(1) in best case where bucket is empty or only has the the item with matching key
        # O(l) is average case where l is the number of items in structure divided by # of buckets
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, delete entry associated with given key
        # Otherwise, raise error to tell user delete failed
        # raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        node_data = self.buckets[index].find(lambda item: item[0] == key)
        if(node_data == None):
            raise KeyError('Key not found: {}'.format(key))
        else:
            self.buckets[index].delete(node_data)

        self.size -= 1

    def resize(self):
        print("resizing at size " + str(self.size))
        print("load is " + str(self.load))

        to_rehash = self.items()
        self.load *= 2
        self.size = 0
        self.buckets = [LinkedList() for _ in range(self.load)]
        for key_value in to_rehash:
            self.set(key_value[0], key_value[1])




def test_hash_table():

    file = open('/usr/share/dict/words','r')
    read_words = file.readlines()
    file.close()

    current = time.perf_counter()
    ht = HashTable()

    for i in range(100000):
        ht.set(read_words[random.randrange(235886)], None)

    print(time.perf_counter()-current)
    print("Size is " + str(ht.size))
    print("load is " + str(ht.load))



if __name__ == '__main__':
    test_hash_table()
