#%%
import random

def _get_random_word():
    word_list = ['Banana', 'Apple', 'Mango', 'Grapes', 'Pear']
    random_word = random.choice(word_list).lower()
    return random_word

def _get_user_guess():
    user_guess = input("Enter a single letter: ").lower()
    return user_guess

def _is_valid_guess(user_guess):
    return len(user_guess) == 1 and user_guess.isalpha()

user_guess = _get_user_guess()

if _is_valid_guess(user_guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# %%
