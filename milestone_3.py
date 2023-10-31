
# import random

# word_list = ["apple", "banana", "kiwi", "grapes", "melon"]
# word = random.choice(word_list)
# print(word)

# # Create a set to store correctly guessed letters
# correct_guesses = set(word)

# # Create a set to store incorrect guesses
# incorrect_guesses = set()

# # Step 1: Create a while loop that runs continuously
# while True: 
#     # Step 2: Ask the user to guess a letter and assign it to the "guess" variable    
#     guess = input("Guess a letter: ")
#     if len(guess) == 1 and guess.isalpha():
#         if guess in word:
#             correct_guesses.discard(guess)  # Remove the correct guess from the set
#             print(f"Good guess! {guess} is in the word.")
#         else:
#             incorrect_guesses.add(guess)  # Add incorrect guesses to a separate set
#             print(f"Sorry, {guess} is not in the word. Try again.")

#         # Step 3: Check if all letters in the word have been guessed
#         if not correct_guesses:
#             print(f'Congratulations! You guessed the word: {word}')
#             break
#     else:
#         # Step 4: If the guess does not pass the check, print an error message
#         print("Invalid letter. Please, enter a single alphabetical character.")


# import random

# word_list = ["apple", "banana", "kiwi", "grapes", "melon"]
# word = random.choice(word_list)
# print(word)

# # Create a dictionary to store the remaining occurrences of each letter in the word
# remaining_letters = {letter: word.count(letter) for letter in set(word)}

# # Create a set to store incorrect guesses
# incorrect_guesses = set()

# # Step 1: Create a while loop that runs continuously
# while True:
#     # Step 2: Ask the user to guess a letter and assign it to the "guess" variable
#     guess = input("Guess a letter: ").lower()  # Convert the guess to lowercase for case-insensitivity
#     if len(guess) == 1 and guess.isalpha():
#         if guess in remaining_letters and remaining_letters[guess] > 0:
#             remaining_letters[guess] -= 1  # Decrease the remaining occurrences of the guessed letter
#             print(f"Good guess! {guess} is in the word.")
#         else:
#             incorrect_guesses.add(guess)  # Add incorrect guesses to a separate set
#             print(f"Sorry, {guess} is not in the word. Try again.")

#         # Step 3: Check if all letters in the word have been guessed
#         if all(remaining == 0 for remaining in remaining_letters.values()):
#             print(f'Congratulations! You guessed the word: {word}')
#             break
#     else:
#         # Step 4: If the guess does not pass the check, print an error message
#         print("Invalid letter. Please, enter a single alphabetical character.")



import random

word_list = ["apple", "banana", "kiwi", "grapes", "melon"]
word = random.choice(word_list)
print(word)

# Create a dictionary to store the remaining occurrences of each letter in the word
remaining_letters = {letter: word.count(letter) for letter in set(word)}

# Create a set to store incorrect guesses
incorrect_guesses = set()

# Function to check if the guessed letter is in the word
def check_guess(guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()
    
    # Step 3: Check if the guess is in the word
    if guess in remaining_letters and remaining_letters[guess] > 0:
        remaining_letters[guess] -= 1  # Decrease the count of the guessed letter
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        incorrect_guesses.add(guess)  # Add incorrect guesses to a separate set
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

# Function to ask for user input and call check_guess
def ask_for_input():
    # Create a while loop that runs continuously
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Guess a letter: ")
        
        # Step 2: Move the code that checks the input into this function block
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word
            if check_guess(guess):
                # Step 3: Check if all letters in the word have been guessed
                if all(remaining == 0 for remaining in remaining_letters.values()):
                    print(f'Congratulations! You guessed the word: {word}')
                    break
        else:
            # Step 2: If the guess does not pass the check, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Call the ask_for_input function to test your code
ask_for_input()

