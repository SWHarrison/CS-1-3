# All permutation n choose k
# Example: n = 3, k = 2, Returns [[1,2],[1,3],[2,3],[2,1],[3,1],[3,2]]
def permutation(n, k = None):

    if(k == None):
        k = n

    if not isinstance(n, int) or n < 1:
        raise ValueError('Permutations are undefined for n = {}'.format(n))

    if not isinstance(k, int) or k < 1:
        raise ValueError('Permutations are undefined for k = {}'.format(k))

    if n < k:
        raise ValueError('Permutation is undefined when n > k, {} > {}'.format(n,k))

    num_list = list()

    for i in range(0,n):
        num_list.append(i+1)

    print("All permutations of {} pick {}: ".format(n,k))

    if(k < 2):
        to_return = []
        for value in num_list:
            to_return.append([value])

        return to_return

    perms = recursive_perm_pick_k(num_list,k)

    return perms

def recursive_perm_pick_k(arr,k):

    if(len(arr) == 1):

        to_return = []
        to_return.append([arr[0]])
        return to_return

    to_return = []

    for index, value in enumerate(arr):

        new_list = arr.copy()
        new_list.remove(value)

        new_list1 = arr[0:index]
        new_list2 = arr[index+1:]
        new_list3 = new_list1 + new_list2
        #print("new list 1 " + str(new_list1))
        #print("new list 2 " + str(new_list2))
        #print("new list 3 " + str(new_list3))
        #print("new list   " + str(new_list))


        next_value = recursive_perm_pick_k(new_list,k)

        for item in next_value:
            to_add = item.copy()
            if(len(next_value[0]) < k):
                to_add.insert(0,value)
            to_return.append(to_add)

    return to_return

def all_perms(n):

    num_list = list()

    for i in range(0,n):
        num_list.append(i+1)

    print("All permutations of: " + str(num_list))

    perms = recursive_perm(num_list)
    return perms

def recursive_perm(arr):

    #print("*********" + str(arr))
    if(len(arr) == 1):

        to_return = []
        to_return.append([arr[0]])
        return to_return

    to_return = []

    for value in arr:

        new_list = arr.copy()
        new_list.remove(value)

        next_value = recursive_perm(new_list)

        for item in next_value:
            to_add = item.copy()
            to_add.insert(0, value)
            to_return.append(to_add)

    return to_return

print(all_perms(3))
perm = (permutation(5, 2))
print(perm)
print(len(perm))
