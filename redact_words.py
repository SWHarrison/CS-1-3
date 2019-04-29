from set import Set

def redact_words(words, banned_words):
    # O(n+m) runtime where n is length of words and m is length of banned_words
    if(len(banned_words) == 0):
        return words


    banned_set = Set(banned_words)

    # Other way to parse words, line 23 handles this on 1 line
    '''to_return = []
    for word in words:

        if(word not in banned_set):
            to_return.append(word)

    #print(to_return)
    return to_return'''

    #return [word for word in words if word not in banned_set]

    return list(filter(lambda word: word not in banned_set, words))
