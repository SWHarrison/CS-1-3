def histogram_dictionary(text):
    '''Dictionary representation of histogram of text'''
    to_return = {}
    for letter in text:
        if letter.lower() in to_return:
            to_return[letter.lower()] += 1
        else:
            to_return[letter.lower()] = 1
    return to_return

def is_anagram(word1, word2):

    list_1 = list(word1)
    list_2 = list(word2)
    histo_1 = histogram_dictionary(list_1)
    histo_2 = histogram_dictionary(list_2)

    if(len(histo_1.keys()) != len(histo_2.keys())):
        return False

    for key in histo_1.keys():
        try:
            if(histo_1[key] != histo_2[key]):
                return False
        except KeyError:
            return False

    return True

def find_anagrams(word):

    histo = histogram_dictionary(list(word))

    file = open('/usr/share/dict/words','r')
    read_words = file.readlines()
    file.close()

    to_return = list()
    for new_word in read_words:
        new_word = new_word.strip()
        if(is_anagram(word, new_word) == True):
            to_return.append(new_word)

    return to_return

print(is_anagram("Sams", "Mass"))
print(find_anagrams("gelatin"))
