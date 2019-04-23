#!python
import random, time

class HashTable(object):

    def __init__(self, init_size=16):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [None] * init_size
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
        all_keys = list()
        for bucket in self.buckets:
            if(bucket):
                all_keys.append(bucket[0])
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #O(n) as it runs through the entire hash table once, n is number of items in structure.
        #Loop through all buckets
        all_values = list()
        for bucket in self.buckets:
            if(bucket):
                all_values.append(bucket[1])
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #O(n) as it runs through the entire hash table once, n is number of items in structure.
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            if(bucket):
                all_items.append(bucket)
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets."""
        # Running time: O(b) Where b is the number of buckets
        '''length = 0
        #Loop through all buckets
        for bucket in self.buckets:
            if(bucket):
                length+=1

        return length'''

        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(1) in best case where bucket is empty or only has 1 item, O(l) is average case
        #Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        while(self.buckets[index%self.load]):
            if(self.buckets[index%self.load][0] == key):
                return True
            else:
                index+=1
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(1) in best case where bucket is empty or only has 1 item, O(l) is average case
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, return value associated with given key
        # Otherwise, raise error to tell user get failed
        index = self._bucket_index(key)
        while(self.buckets[index%self.load]):
            if(self.buckets[index%self.load][0] == key):
                return self.buckets[index%self.load][1]
            else:
                index+=1

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
        while(self.buckets[index%self.load]):
            #print(index)
            if(self.buckets[index%self.load][0] == key):
                self.buckets[index%self.load] = (key, value)
                #print(str(key) + " is in hash table")
                return
            else:
                index+=1

        #print(str(key) + " is not in hash table")
        self.size += 1
        self.buckets[index%self.load] = (key, value)

        if(self.load_factor() > self.resize_factor):
            self._resize()

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
        print("deleting",key)
        to_rehash = list()
        index = self._bucket_index(key)
        not_found = True
        while (self.buckets[index%self.load]):
            if (self.buckets[index%self.load][0] == key):
                print("found match at " + str(index))
                not_found = False
                self.buckets[index%self.load] = None
                new_index = index + 1
                while(self.buckets[new_index%self.load]):
                    to_rehash.append(self.buckets[new_index%self.load])
                    self.buckets[new_index%self.load] = None
                    self.size -= 1
                    new_index+=1
                break
            else:
                index+=1

        if(not_found):
            raise KeyError('Key not found: {}'.format(key))

        for key_value in to_rehash:
            self.set(key_value[0], key_value[1])

        self.size -= 1
        print("size after deletion", self.size)

    def _resize(self, new_size = None):

        print("Resizing from " + str(self.size))
        print("Max load is " + str(self.load))

        if new_size is None:
            self.load *= 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            self.load /= 2  # Half size
        else:
            self.load = new_size

        to_rehash = self.items()
        self.size = 0
        self.buckets = [None] * self.load

        for key_value in to_rehash:
            self.set(key_value[0], key_value[1])



def test_hash_table():
    file = open('/usr/share/dict/words','r')
    read_words = file.readlines()
    file.close()

    current = time.perf_counter()
    ht = HashTable()
    '''print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))'''

    for i in range(100000):
        #ht.set(random.randrange(10000))
        #ht.set(chr(random.randrange(26)+97))
        ht.set(read_words[random.randrange(235886)])

    print(time.perf_counter()-current)
    #print(ht.items())
    print("Size is " + str(ht.size))
    print("load is " + str(ht.load))
    #print(time.perf_counter()-current)

if __name__ == '__main__':
    #test_hash_table()
    ht = HashTable()
    ht.set('I', 1)
    ht.set('V', 5)
    ht.set('X', 10)
    print(ht.buckets)
    assert ht.length() == 3
    assert ht.size == 3
    ht.delete('I')
    ht.delete('X')
    print(ht.buckets)
    print(ht.size)
    assert ht.length() == 1
    assert ht.size == 1
    print(ht.size)
    #with self.assertRaises(KeyError):
    #ht.delete('X')  # Key no longer exists
    #with self.assertRaises(KeyError):
    #ht.delete('A')  # Key does not exist
