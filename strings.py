#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    index = find_index(text,pattern)

    if(index == None):
        return False

    return True


def find_index(text, pattern, offset = 0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    if(len(pattern) == 0):
        return 0 + offset

    #for index, letter in enumerate(text):
    for index in range(offset, len(text) - len(pattern) + 1):

        if(text[index] == pattern[0]):

            no_nonmatch = True
            for i in range(1,len(pattern)):

                if(text[index+i] != pattern[i]):
                    no_nonmatch = False
                    index += i
                    break

            if(no_nonmatch):
                return index

    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    to_return = []
    current_index = 0
    offset = 0

    if(len(pattern) == 0):

        return list(range(0,len(text)))

    while(current_index != None and offset <= (len(text) - len(pattern))):

        #print("offset " + str(offset))


        current_index = find_index(text,pattern, offset)
        #print("current_index " + str(current_index))
        if(current_index == None):
            return to_return

        offset = (1 + current_index)


        to_return.append(current_index)

    return to_return


def test_string_algorithms(text, pattern):
    pass
    #found = contains(text, pattern)
    #print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    #index = find_index(text, pattern)
    #print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    #indexes = find_all_indexes(text, pattern)
    #print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    #main()

    #print(find_index('abCabDabE','ab',3))
    print(find_index('abababaabaaabab', 'baab'))

    #arr = [[0,1],[2,3]]

    #for i in range(len(arr) * len(arr[0])):

        #print(arr[i//2][i%2])
