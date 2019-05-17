'''
Look at the decimal search tree, it can accomplish scenario 3, 4 and 5.

Decimal tree is essentially a trie or prefix tree that stores the number
and cost associated with that number. I considered it to be the potential
best solution for the following reasons:

1. Much less memory usage than a hash table
2. No resizing that will cause downtime during the process
3. Maximum steps to access a cost is 11, or the length of the longest #
    This is still reasonably fast, even though a hash table would be faster

Due to the nature of the tree, there will never be downtime, as deletions
do not break links, they only change values to None.

One potential improvement to consider is to turn the trie into a compact
trie. This would greatly reduce the memory cost of the tree as most empty
nodes would be removed. However it would make adding new phone numbers
cause potential breaks in the tree temporarily. This means to accomplish
scenario 5's goal, there would need to be a secondary trie built that
would take changes then switch into production, potentially taking even
more memory usage.
'''
