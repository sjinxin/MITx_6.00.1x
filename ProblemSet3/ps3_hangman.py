# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed_):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE..
    for c in secretWord:
        if not c in lettersGuessed_:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed_):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    GuessWord=''
    for c in secretWord:
        if not c in lettersGuessed_: 
            GuessWord+='_ '
        else: 
            GuessWord +=c
    return GuessWord


def getAvailableLetters(lettersGuessed_):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    AvailableLetters=''
    for c in string.ascii_lowercase:
        if not c in lettersGuessed_: 
            AvailableLetters +=c
    return AvailableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    numOfGuesses=8
    lettersGuessed=[]
    GuessWord=''     
    print "%s" % secretWord
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long." % len(secretWord)
    while numOfGuesses > 0 and not isWordGuessed(secretWord, lettersGuessed):
	print "-------------"
    	print "You have %d guesses left." % numOfGuesses
    	print "Available letters: %s" % getAvailableLetters(lettersGuessed)
	guessInLowerCase  = raw_input("Please guess a letter:").lower()
        
	if guessInLowerCase in lettersGuessed:
                print "Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord,lettersGuessed)
                continue
	print "."
	lettersGuessed +=guessInLowerCase

	if guessInLowerCase in secretWord:
		print "Good guess: %s" % getGuessedWord(secretWord,lettersGuessed)
	else:
		print "Oops! That letter is not in my word: %s" % getGuessedWord(secretWord,lettersGuessed)
		numOfGuesses-=1

    print "-------------"
    if numOfGuesses == 0:
	print "Sorry, you ran out of guesses. The word was else. "
    else:
	print "Congratulations, you won!" 

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman("tact")
