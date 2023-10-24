#%%
import random

word_list = ['Banana', 'Apple', 'Mango', 'Grapes', 'Pear']

print(word_list)

random_word = random.choice(word_list).lower()

print(random_word)

def get_user_guess():
    user_guess = input("Enter a single letter: ").lower()
    return user_guess

# Check if the user's guess is a single alphabetical character
def is_valid_guess(user_guess):
    return len(user_guess) == 1 and user_guess.isalpha()

user_guess = get_user_guess()

# Check if the user's guess is valid
if is_valid_guess(user_guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
# %%
