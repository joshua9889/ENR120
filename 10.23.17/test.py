import random
import string

hangWord = ""
words = []
guessedLetters = []
guessedLettersLogic = []

def addToGuessedLetters(letter):
    guessedLetters.append(letter)
    sorted(guessedLetters)


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

# Find the word we are going to guess
def getRandomWord():
    pos = random.randint(0, len(words)-1)
    global hangWord
    hangWord = words[pos]
    return hangWord

# Guess a SINGLE letter
def guess_letter(letter):
    addToGuessedLetters(letter)
    isInWord = False

    for i in range(len(hangWord)):
        if hangWord[i] == str(letter):
            guessedLettersLogic.append(True)
            isInWord =

    return isInWord

# Guess a WHOLE word
def guess_word(word):
    return string.lower(word) == hangWord


def guessLogic(guess):
    if len(guess) != 1:
        return guess_letter(str(guess))
    else:
        return guess_word(guess)


def askForInput():
    print "Please enter a letter or word to guess."
    guessed = ""
    while True:
        guessed = str(raw_input(""))

        isAnumber = False

        for i in range(len(guessed)):
            for x in range(9):
                if guessed[i] == str(x):
                    isAnumber = True

        if not isAnumber:
            break
        else:
            print "Please enter a valid letter or word."
        pass

    return guessed

# Main game
def main():
    importWordList('noun_list.txt')

    isStillPlaying = True
    didWin = False

    while isStillPlaying and not didWin:
        try:
            correctGuess = guessLogic(askForInput())
        except KeyboardInterrupt:
            break

    print hangWord

main()
