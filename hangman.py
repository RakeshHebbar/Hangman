import random

HANGMANPICS = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def pickARandomWord(wordList):
    wIndex = random.randint(0, len(wordList) - 1)
    return wordList[wIndex]

def guess():

    wordToGuess = pickARandomWord(words)
    blanks = '-'*len(wordToGuess)
    guessedLetters = ''
    cnt = 0

    while cnt <= len(HANGMANPICS) - 1:

        print(blanks)

        userGuess = raw_input("Guess a letter : ")

        if len(userGuess) != 1:
            userGuess = raw_input("I said 'a' letter : ")

        while 1:
            if userGuess in guessedLetters:
                userGuess = raw_input("You already used this letter. Try a differnt one : ")
            else:
                break

        for i in range(len(wordToGuess)):
            if userGuess == wordToGuess[i]:
                blanks = blanks[:i] + userGuess + blanks[i+1:]

        guessedLetters += userGuess

        if userGuess not in wordToGuess:
            print(HANGMANPICS[cnt])
            cnt += 1

        if blanks == wordToGuess:
            print("Well Done. Go Have an ice-cream now!!.")
            break

        if cnt == len(HANGMANPICS):
            print("You LOOSE !! The Word was " + wordToGuess)



def play():
    print("H A N G M A N")
    print("Hint : Animal Names.")
    print('')
    guess()


#if __name__ == _main_:
play()
