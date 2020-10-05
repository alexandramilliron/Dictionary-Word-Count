import sys

def count_words(file):
    """ Returns the count of all words in provided file argument. 

    Input is a text file.
    Output prints the words with their respective counts to the terminal.

    """

    count_words = {}

    open_file = open(file)
    
    for line in open_file:
        split_line = line.rstrip().lower().split(' ')
        for word in split_line:
            stripped_word = word.rstrip(",.?")
            count_words[stripped_word] = count_words.get(stripped_word, 0) + 1
    for word, count in count_words.items():
        print(word, count)

count_words(sys.argv[1])

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()