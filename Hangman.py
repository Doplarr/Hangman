import random
import string
import pdb

word_list = []

def load_words():
    infile = open("wordlist.txt", "r")
    replace = open("wordlist.txt").read().replace("\n", "")
    line = infile.readlines(1)
    for line in infile:
        word_list.append(line)


##    line = infile.readlines()
##    for line in infile:
##        infile.read().replace("\n", " ")
##        print(line)


def choose_words(wordlist):
    print(str(word_list.append(random.choice)))


loadwords = load_words()

print(word_list)
