#! python3
import random, re
from openapi import create_spec
import json_pattern_validator
import lodash
import lodash

# All available words
wordBank = [
    'cat',
    'mattress',
    'alienate',
    'jargon',
    'juggalo',
    'spillage',
    'gangrenous',
    'deer',
    'jazz',
    'hangman',
    'acrobatics',
    'hymn',
    'wonderous',
    'alibi',
    'elbow',
    'bazooka',
    'zookeeper',
    'bookkeeper',
    'counterclockwise',
    'sky',
    'tongue',
    'seventeen'
]

# Dictionary of all hangman stages
manStage = [r'''
    |



''','''
    |
    O


''','''
    |
    O
    |
    
''','''
    |
    O
   /|
   
''','''
    |
    O
   /|\\
   
''','''
    |
    O
   /|\\
   /
''','''
    |
    O
   /|\\
   / \\
''']

play = True
while play == True: # Main game loop, false ends program
    
    num = random.randint(0,int(len(wordBank))-1)
    word = wordBank[num] # Sets 'word' as random word from wordBank
    
    #Global variables
    stage = 0 # Stage of the game
    win  = False # If guessed correctly or not
    letterCount = 0
    wordCount = 0

    # Dictionary of correct guesses
    guess = [None]*(int(len(word)))*2
    # Dictionary of guessed letters
    guessed = []

    # Fills 'guess' with dashes and spaces
    for i in range(0,(int(len(word)))*2):
        if i%2 == 0 or i == 0:
            guess[i] = '_'
        else:
            guess[i] = ' '

    # Initialize regex for 'word' letters
    guessRegex = re.compile(r'[a-z]')

    # Single stage loop
    while win == False:
        choice = True
        guessedS = ', '.join(guessed)
        wordGuess = ''.join(guess)
        
        # Printing game
        print('----------------')
        print(manStage[stage])
        print('Guesses: '+guessedS)
        print(wordGuess)

        # While game unfinished
        while choice == True:
            choice = False
            print('Pick a letter or take a guess')
            letter = input()
            letter = letter.lower() # Converts input to lowercase
            letterCheck = guessRegex.search(letter)

            # Checking if word guess is right
            if int(len(letter)) == int(len(word)) and letterCheck != None:
                if letter == word:
                    win = True
                    break
                else:
                    print('Wrong guess')
                    choice == True
                    break
                
            # Checking if valid input
            if letterCheck == None or int(len(letter))>1:
                print('Invalid')
                choice = True
            
            # Checking if already chosen and incorrect
            for i in range(0,int(len(guessed))):
                if letter == guessed[i]:
                    print('Already guessed')
                    choice = True
                    break
                    
            # Checking if already chosen and correct
            for i in range(0,int(len(guess))):
                if letter == guess[i]:
                    print('Already guessed')
                    choice = True
                    break

        for i in range(0,int(len(word))):
            # If guess is in word, fill in word
            if letter == word[i]:
                guess[i*2] = word[i]
                letterCount+=1
                wordCount+=1
                
        # If letter isn't in word, advance stage
        if letterCount == 0 and int(len(letter)) == 1:
            print('Wrong letter')
            guessed.append(letter)
            stage+=1

        # Resets 'letterCount' for next game
        letterCount = 0

        if wordCount == int(len(word)):
            win = True

        if stage == 6:
            break

    # Printing game conclusion
    print('----------------')
    if win == False:
        print(manStage[6])
        print('Loser :(')
        print('The word was '+word)
    else:
        print('You Are Winner!')
        print('You guessed '+word)

    print('Do you want to play again? (y/n)')
    game = input()
    if game.lower() == 'n':
        play = False


