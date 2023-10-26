#%%
import random
import milestone_3

class Hangman():
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
        if letter in self.word:
            print(f"Good guess! {letter} is in the word")
            for i, letter_in_word in enumerate(self.word):
                if letter_in_word == letter:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else: 
            self.num_lives -= 1 
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            letter = input("Guess a letter: ").lower()
            if len(letter) == 1 and letter.isalpha():
                if letter in self.list_of_guesses:
                    print(f"You have already guessed {letter}, try a different letter...")
                else:
                    self.list_of_guesses.append(letter)
                    self.check_letter(letter, self.word_guessed)
            else:
                print("Invalid input. Please enter a single alphabetical character.")
            
                
new_game = Hangman()
new_game.ask_for_input()

# %%
