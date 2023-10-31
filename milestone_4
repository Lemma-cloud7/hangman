# import random

# class Hangman:
#     def __init__(self, word_list, num_lives=5):
#         # Initialize attributes
#         self.word_list = word_list
#         self.num_lives = num_lives
#         self.word = random.choice(word_list)
#         self.word_guessed = ['_'] * len(self.word)
#         self.num_letters = len(set(self.word))
#         self.list_of_guesses = []

#     def display_word(self):
#         return ' '.join(self.word_guessed)

#     def guess_letter(self, letter):
#         if letter not in self.list_of_guesses:
#             self.list_of_guesses.append(letter)
#             if letter in self.word:
#                 for i, char in enumerate(self.word):
#                     if char == letter:
#                         self.word_guessed[i] = letter
#             else:
#                 self.num_lives -= 1

#     def is_game_over(self):
#         if self.num_lives == 0:
#             return True, "You lose! The word was: " + self.word
#         elif '_' not in self.word_guessed:
#             return True, "Congratulations! You guessed the word: " + self.word
#         else:
#             return False, ""

# if __name__ == "__main__":
#     # Example usage:
#     word_list = ["apple", "banana", "kiwi", "grapes", "melon"]
#     hangman_game = Hangman(word_list)
    
#     while True:
#         print("Word to guess:", hangman_game.display_word())
#         print("Number of lives:", hangman_game.num_lives)
#         print("List of guesses:", hangman_game.list_of_guesses)
        
#         guess = input("Guess a letter: ").lower()
#         hangman_game.guess_letter(guess)
        
#         game_over, message = hangman_game.is_game_over()
#         print("\n" + message)
        
#         if game_over:
#             play_again = input("Do you want to play again? (yes/no): ").lower()
#             if play_again != "yes":
#                 break
#             else:
#                 hangman_game = Hangman(word_list)








import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialize attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def display_word(self):
        return ' '.join(self.word_guessed)

    def guess_letter(self, letter):
        if letter not in self.list_of_guesses:
            self.list_of_guesses.append(letter)
            if letter in self.word:
                for i, char in enumerate(self.word):
                    if char == letter:
                        self.word_guessed[i] = letter
                        self.num_letters -= 1
            else:
                self.num_lives -= 1

    def is_game_over(self):
        if self.num_lives == 0:
            return True, "You lose! The word was: " + self.word
        elif '_' not in self.word_guessed:
            return True, "Congratulations! You guessed the word: " + self.word
        else:
            return False, ""

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.guess_letter(guess)
                break

if __name__ == "__main__":
    # Example usage:
    word_list = ["apple", "banana", "kiwi", "grapes", "melon"]
    hangman_game = Hangman(word_list)
    
    while True:
        print("Word to guess:", hangman_game.display_word())
        print("Number of lives:", hangman_game.num_lives)
        print("List of guesses:", hangman_game.list_of_guesses)
        
        hangman_game.ask_for_input()
        
        game_over, message = hangman_game.is_game_over()
        print("\n" + message)
        
        if game_over:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
            else:
                hangman_game = Hangman(word_list)
