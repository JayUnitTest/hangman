#%%
import milestone_2

# Takes in user input, checks if guess matches conditions to pass as a valid guess
#calls check_guess function to check if the letter is in the word
def ask_for_input():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid input. Please enter a single alphabetical character.")

#function to check if the letter input by the user is in the word. 
def check_guess(guess):
    if guess in milestone_2.random_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

ask_for_input()

# %%
