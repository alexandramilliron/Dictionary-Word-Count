import sys
from collections import Counter

def count_words(file):
    """ Returns the count of all words in provided file argument. 

    Input is a text file.
    Output prints the words with their respective counts to the terminal.

    """

    count_words = {}

    #cnt = Counter()

    open_file = open(file)
    
    for line in open_file:
        split_line = line.rstrip().lower().split(" ")
        for word in split_line:
            stripped_word = word.strip(",.?")
            count_words[stripped_word] = count_words.get(stripped_word, 0) + 1
    for word, count in count_words.items():
        print(word, count)

    
    # for word in stripped_list:
    #     cnt[word] += 1

    # return cnt 

print(count_words(sys.argv[1]))



# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()