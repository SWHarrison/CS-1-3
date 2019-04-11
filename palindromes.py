#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    #return is_palindrome_recursive(text)

LETTERS = frozenset(string.ascii_letters)
def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    left = 0
    right = len(text) - 1

    #while (left <= right and text[left] not in string.ascii_letters):
    #    left += 1
    #while (left <= right and text[right] not in string.ascii_letters):
    #    right -= 1

    while(left <= right):

        print("left " + text[left])
        print("right " + text[right])

        while (left <= right and not text[left].isalpha()):
            left += 1
        while (left <= right and text[right] not in LETTERS):
            right -= 1

        print("left " + text[left])
        print("right " + text[right])
        #No match, not a palindrome
        if(text[left].lower() != text[right].lower()):
            return False

        left += 1
        right -= 1


    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if(len(text) <= 1):
        return True

    # TODO fix left <= right when right is None
    if(left == None and right == None):
        left = 0
        right = len(text) - 1

        while (left <= right and text[left] not in string.ascii_letters):
            left += 1

        while (left <= right and text[right] not in string.ascii_letters):
           right -= 1

    #print(str(left) + " " + text[left])
    #print(str(right) + " " + text[right])

    while (left <= right and text[left] not in string.ascii_letters):
        left += 1
    while (left <= right and text[right] not in string.ascii_letters):
        right -= 1

    print(str(left) + " " + text[left])
    print(str(right) + " " + text[right])

    if(left > right):
        return True

    if(text[left].lower() == text[right].lower()):
        return is_palindrome_recursive(text, left + 1, right - 1)

    if(text[left] != text[right]):
        return False



    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    #main()
    print(is_palindrome_iterative('B==b-----'))
