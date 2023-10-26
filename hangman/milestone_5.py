#%%
import random

class Hangman():
    '''
    Hangman game that will ask for the user for a letter and checks it against the 
    randomly selected word. The player will begin with a default amount of lives(5) which will decrement
    each time an incorrect guess is made. 

    parameters: 
    ------------
    word_list : list 
        This is a list of words to be used within the game. 
    num_lives : int
        Number of lives the player has in the game. 

    Attributes:
    -----------
    word : str 
        This is the word to be guessed, selected randomly from the word_list
    word_guessed: list 
        A list of the letters in the word. Each letter that has not been guessed has a 
        place holder of '_' until guessed correctly. For example, if the word is 'mango'
        the word_guessed list would look like: ['_','_','_','_','_']. Upon a successful guess 
        i.e 'm', the word_guessed list will be updated such that it will look like: ['m','_','_','_','_']
    list_of_guesses: list
        This is a list of the letters that have been attempted. 
    num_letters: int
        The number of unique letters in the word that have yet to be guessed.
    list_letters: list
        A list of the letters that have already been guessed 
    
    Methods:
    --------

    check_letter(letter)
        This checks if the letter is in the word. 
    
    ask_for_input()
        Asks the user to input a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = set(self.word)
        self.list_of_guesses = []
        print(f"The mystery word has {len(self.num_letters)} characters")
        print(self.word_guessed)

    def check_letter(self, letter):
        '''
        Method to check if the letter is in the word. 
        If the letter is in the word, it replaces the '_' placeholder in the word_guessed list 
        with the corresponding letter. 
        If the letter is not in the word, it decrements the players lives by 1.

        Parameters:
        ------------
        letter: str 
            The input letter being checked.
        '''
        letter = letter.lower()  
        if letter not in self.list_of_guesses:
            self.list_of_guesses.append(letter) 
            if letter in self.num_letters:
                print(f"Good guess! {letter} is in the word")
                for i, letter_in_word in enumerate(self.word):
                    if letter_in_word == letter:
                        self.word_guessed[i] = letter
                self.num_letters.remove(letter)  
                print(f"Guess: {' '.join(self.word_guessed)}")
            else:
                self.num_lives -= 1
                print(f"Sorry, {letter} is not in the word.")
                print(f"You have {self.num_lives} lives left.")
        else:
                print(f"You have already guessed '{letter}', try a different letter...")

    def ask_for_input(self):
        '''
        This method asks the user to enter a letter and then performs a few operations:
        1. A check if the letter has already been guessed
        2. If the character is a single character or not. 
        Upon successfully passing checks, it will then call the check_letter method
        '''
        while True:
            letter = input("Guess a letter: ").lower()
            if len(letter) == 1 and letter.isalpha():
                if letter not in self.list_of_guesses:
                    self.check_letter(letter)
                    break
                else:
                    print(f"You have already guessed '{letter}', try a different letter...")
            else:
                print("Invalid input. Please enter a single alphabetical character.")

def play_game(word_list):
    '''
    Instantiate an instance of the game. Call this method to begin playing Hangman!.
    '''
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters:
        game.ask_for_input()
    if game.num_lives == 0:
        print("You lost! The word was", game.word)
    else:
        print("Congratulations, You won the game!")
        print(f"The word was {game.word}")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'mango']
    play_game(word_list)

# %%
