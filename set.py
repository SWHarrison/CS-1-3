from linear_probing import HashTable

class Set(object):

    def __init__(self, items = None):

        self.ht = HashTable()

        if items is not None:
            for item in items:
                self.ht.set(item,item)

    def __repr__(self):
        items = ['{!r}'.format(key) for key in self.ht.keys()]
        return '{' + ', '.join(items) + '}'

    def size(self):

        return self.ht.size

    def contains(self, element):

        try:
            item = self.ht.get(element)
            return True
        except KeyError:
            return False

    def __contains__(self, element):

        return self.contains(element)

    def add(self, element):

        self.ht.set(element, element)

    def remove(self, element):

        self.ht.delete(element)

    def union(self, other_set):

        new_set = Set()

        for item in self.ht.values():
            new_set.add(item)

        for item in other_set.ht.values():
            new_set.add(item)

        return new_set

    def intersection(self, other_set):

        new_set = Set()

        for item in self.ht.values():
            if(other_set.contains(item)):
                new_set.add(item)

        return new_set

    def difference(self, other_set):

        new_set = Set()

        for item in self.ht.values():
            if(not other_set.contains(item)):
                new_set.add(item)

        return new_set

    def is_subset(self, other_set):

        for item in other_set.ht.values():
            if(not self.contains(item)):
                return False

        return True
