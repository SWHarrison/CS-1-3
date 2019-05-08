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

words = []
to_take_out = [[0,2],[0,4],[1,0],[1,1],[1,3],[2,4],[3,3],[3,4]]
#words.append(find_anagrams("tefon"))
#words.append(find_anagrams("sokik"))
#words.append(find_anagrams("niumem"))
#words.append(find_anagrams("siconu"))
words.append("often")
words.append("kiosk")
words.append("immune")
words.append("cousin")

print(find_anagrams("stinks"))

'''letters = ""
for item in to_take_out:
    letters += words[item[0]][item[1]]

print(letters)
list_num = list(range(len(letters)))
print(list_num)
already_done = []

for i in range(len(letters)):

    not_i = letters[0:i] + letters[i+1:]
    #print(not_i)
    for j in range(len(not_i)):

        not_j = not_i[0:j] + not_i[j+1:]
        dict = histogram_dictionary(not_j)
        if(dict is in already_done):'''
