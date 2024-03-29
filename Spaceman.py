import random, collections

WORDS_FILE = "random_words.txt"

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open(WORDS_FILE, 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    return collections.Counter(list(secret_word)) == collections.Counter(letters_guessed)

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guess = ""
    count = 0
    for char in secret_word:
        if char == letters_guessed:
            guess += letters_guessed
            count += 1
        else:
            guess += " _ "
    return (guess, count)
    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    pass
    if guess in secret_word:
        return True
    else:
        return False

def get_blank_word(secret_word):
    guess = ""
    for char in secret_word:
        guess+=" _ "
    return guess

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    #get_blank_word(secret_word)

    #TODO: show the player information about the game according to the project spec
    print(secret_word)
    print("Your guessing is {}".format(get_blank_word(secret_word)))

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    #give me a letters
    correct_letters = []
    incorrect_guess = 0
    while(is_word_guessed(secret_word, correct_letters) is False and incorrect_guess < 5):
        user_guess = raw_input("give input")
        #print(user_guess)
        #determine is letter rights
        is_correct = is_guess_in_word(user_guess, secret_word)
        #fill in correct letters from guessed
        #repeat
        if(is_correct):
            guessed_word = get_guessed_word(secret_word, user_guess)[0]
            amount_of_words = get_guessed_word(secret_word, user_guess)[1]
            print(guessed_word)
            for i in range(amount_of_words):
                correct_letters.append((user_guess))
        else:
            incorrect_guess+=1

    if(is_word_guessed(secret_word, correct_letters)):
        print("Congrats, you've guessed the word correctly")
    else:
        print("Womp womp womp, you've run out of guesses. Better luck next time")
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
