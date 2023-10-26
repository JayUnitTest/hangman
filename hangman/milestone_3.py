#%%
import milestone_2

def _ask_for_input():
    random_word = milestone_2.get_random_word()
    guessed_letters = set()
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already guessed {guess}, try a different letter...")
            else:
                guessed_letters.add(guess)
                _check_guess(guess, random_word)
        else:
            print("Invalid input. Please enter a single alphabetical character.")

def _check_guess(guess, random_word):
    if guess in random_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

_ask_for_input()

# %%
