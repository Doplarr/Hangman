import random
import string
import pdb
word_list = []

def load_words():
    infile = open("wordlist.txt", "r")
    line = infile.readlines(1)
    for line in infile:
        line.strip("\n")
        word_list.append(line)

word_list = []
load_words()

random_word = random.choice(word_list)


print("The word has", (len(random_word) -1), "letters in it")
random_word_len_fix = (len(random_word) -1)

right = ["_"] * (len(random_word) -1)
wrong = []

def  score():
        if len(wrong) > 5:
            print("You lose")
            print("The word was:", random_word)
            input("Press Enter to close the program")

def update():
    for i in right:
        print(i, end = " ")
    print()

update()

while True:
    print("==============================")
    guess = input("Guess a letter:")
    if guess in random_word:
        if guess in right:
            print("you already guessed that")
        else:
            index = 0
            for i in random_word:
                if i == guess:
                    right[index] = guess
                index += 1
            update()
    else:
        if guess not in wrong:
            wrong.append(guess)
            print("Wrong letters:", wrong)
            score()
        else:
            print("you already guessed that")
    if "_" not in right:
        input("You win!, Press Enter to close the program")
        break
