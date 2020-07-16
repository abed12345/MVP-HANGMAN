import random
from wordList import wordList

##get word from word list 
def get_word():
    word = random.choice(wordList)
    return word.upper()

##makes game
def play(word):
    wordComp = "_" * len(word)
    guessed = False
    guseedLetters = []
    guseedWords = []
    tries = 6
    print("Would you like to play Hangman!")
    print(display_hangman(tries))
    print(wordComp)
    print("\n")
    ##loop for guessing
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guseedLetters:
                print("You already guessed", guess)
            elif guess not in word:
                print(guess, "is not in the letter.")
                tries -= 1
                guseedLetters.append(guess)
            else:
                print("You Win!", guess, "was the word!")
                guseedLetters.append(guess)
                wordAsList = list(wordComp)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexes:
                    wordAsList[index] = guess
                wordComp = "".join(wordAsList)
                if "_" not in wordComp:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guseedWords:
                print("You already guessed", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guseedWords.append(guess)
            else:
                guessed = True
                wordComp = word
        else:
            print("Guess Again.")
        print(display_hangman(tries))
        print(wordComp)
        print("\n")
    if guessed:
        print("You win!")
    else:
        print("You Lose! The word was " + word + ". Maybe next time!")

##creates hangman image
def display_hangman(tries):
    stages = [  ## final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                ## head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                ## head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                ## head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                ## head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                ## head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                ## initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

##loops game after first play through
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()