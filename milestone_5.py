
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []

    def display_word(self):
        return ' '.join(self.word_guessed)

    def guess_letter(self, letter):
        if letter not in self.list_of_guesses:
            self.list_of_guesses.append(letter)
            if letter in self.word:
                print(f"Good guess! {letter} is in the word.")
                for i, char in enumerate(self.word):
                    if char == letter:
                        self.word_guessed[i] = letter
            else:
                print(f"Sorry, {letter} is not in the word.")
                self.num_lives -= 1

    def is_game_over(self):
        if self.num_lives == 0:
            return True, "You lose! The word was: " + self.word
        elif '_' not in self.word_guessed:
            return True, "Congratulations! You guessed the word: " + self.word
        else:
            return False, ""

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.guess_letter(guess)
                break

def play_game(word_list):
    game = Hangman(word_list)

    while True:
        print("Word to guess:", game.display_word())
        print("Number of lives:", game.num_lives)
        print("List of guesses:", game.list_of_guesses)

        game_over, message = game.is_game_over()
        if game_over:
            print(message)
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
            else:
                game = Hangman(word_list)
        else:
            game.ask_for_input()

if __name__ == "__main__":
    word_list = ["apple", "banana", "kiwi", "grapes", "melon"]
    play_game(word_list)
