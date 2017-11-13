import random
import string


words = []
hangWord = ''
allowedGuesses = 1
guessedLetters = []
goodGuessMessage = "Good Guess!"


def importWordList(filename): # You can import your own custom list
    f = open(filename, 'r')

    while True:
        word = f.readline()
        fixed_word = word.replace("\n", '')
        if fixed_word != '':
            words.append(fixed_word)
        else:
            break
    f.close()


def setHangWord():
    pos = random.randint(0, len(words)-1)
    global hangWord
    hangWord = words[pos]


def askForInput():
    print "Please enter a letter or word to guess."
    guessed = ""
    guessed = str(raw_input(""))
    return guessed


def isLetterInWord(letter):
    inLetter = False
    for i in range(len(hangWord)):
        if hangWord[i] == letter:
            inLetter = True
    return inLetter

def isWordInWord(word):
    return string.lower(word) == hangWord


def guessSingleLetter(letter):
    global goodGuessMessage
    if isLetterInWord(letter):
        print goodGuessMessage

def main():
    importWordList("noun_list.txt")
    setHangWord()
    for i in range(allowedGuesses):
        askForInput()

main()
