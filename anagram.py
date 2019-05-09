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
    if(len(list_1) != len(list_2)):
        return False
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

def is_anagram_histograms(histo1, histo2):

    if(len(histo1.keys()) != len(histo2.keys())):
        return False

    for key in histo1.keys():
        try:
            if(histo1[key] != histo2[key]):
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
        if(len(word) == len(new_word)):
            histo2 = histogram_dictionary(new_word)
            if(is_anagram_histograms(histo, histo2) == True):
                to_return.append(new_word)

    return to_return

words = []
to_take_out = [[0,2],[0,4],[1,0],[1,1],[1,3],[2,4],[3,3],[3,4]]
words.append(find_anagrams("tefon"))
words.append(find_anagrams("sokik"))
words.append(find_anagrams("niumem"))
words.append(find_anagrams("siconu"))


print(words)

letters = ""
for item in to_take_out:
    word = words[item[0]][0]
    #print(word)
    letter = word[item[1]]
    #print(letter)
    letters += letter

print(letters)
list_num = list(range(len(letters)))
print(list_num)
already_done = []

for i in range(len(letters)):

    not_i = letters[0:i] + letters[i+1:]
    for j in range(len(not_i)):

        not_j = not_i[0:j] + not_i[j+1:]
        print(find_anagrams(not_j))
