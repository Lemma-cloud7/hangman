# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Milestone 1: Setting Up the Game


### Milestone 2: Creating a List of Fruits
To run the Hangman Game on your local machine, follow these steps:

1. Clone the repository to your local system:

   ```bash 
   git clone https://github.com/your-username/hangman-game.git
   git pull

2. Follow the steps outlined in the lab

```
git add milestone_2.py

git commit -m "Added milestone_2.py with Hangman code"

git push origin main
```

##### Editing a Markdown File with Git Bash


``` 
Use the `cd` command to navigate to the directory where your Markdown file is located. 
```

Then use the following commands to edit and save changes using nano text editor:
```
nano Readme.md
```
**Usage**



Step 1: Creating a List of Fruits
-	Creates a list containing the names of your 5 favorite fruits.

Step 2: Assigning the List to a Variable
-	Assigns the created list to a variable called word_list.

Step 3: Printing the List
-	Prints out the newly created list to the standard output (screen).
Generating a Random Word from the List
-	Imports the random module.
-	Generates a random word from the word_list and assigns it to the word variable.
-	Prints out the randomly selected word.
Taking User Input
-	Asks the user to enter a single letter using the input function.
-	Validates user input to ensure it is a single letter and consists of alphabetical characters.
-	Prints "Good guess!" if the input is valid; otherwise, it prints "Oops! That is not a valid input."


### Milestone 3: Adding Word Selection and Guessing Logic

**Usage**

Step 1: Create a While Loop
- Creates a while loop with the condition set to True, ensuring that the code runs continuously.

Step 2: Ask the User to Guess a Letter
- Asks the user to guess a letter and assigns it to a variable called guess.

Step 3: Check the Validity of the Guess
- Checks that the guess is a single alphabetical character using the isalpha method.

Step 4: Break Out of the Loop
- If the guess passes the checks, it breaks out of the loop.

Step 5: Handle Invalid Guesses
- If the guess does not pass the checks, it prints a message saying "Invalid letter. Please, enter a single alphabetical character."
- Check if the Letter Guessed is in the Secret Word
- Checks whether the letter guessed by the user is in the secret word randomly chosen by the computer.

Step 1: Create an If Statement
- Creates an if statement that checks if the guess is in the secret word.

Step 2: Provide Feedback for a Correct Guess
- If the guess is in the word, it prints a message saying "Good guess! {guess} is in the word." 
   The string is formatted to display the actual guess.

Step 3: Provide Feedback for an Incorrect Guess
- Creates an else block that prints a message saying "Sorry, {guess} is not in the word. Try again."  
     This block of code runs if the guess is not in the word.

- The code is structured with two functions, check_guess and ask_for_input, to improve readability and maintainability.

- Defined a function called check_guess that takes the guessed letter as an argument.
- Converts the guess into lowercase.
- Contains the code to check if the guess is in the word.
- Defined a function called ask_for_input.
- Contains the code to ask the user for input and validate it.
- Calls the check_guess function to check if the guess is in the word, passing in the guess as an argument.

### Milestone 4: 

**Usage**

-	Creates a class called Hangman.
-	Initializes the attributes of the class, including word, word_guessed, num_letters, num_lives, word_list, and list_of_guesses.
-	The num_lives is set to 5 by default, but you can change it by passing a different value when creating an instance of the class.

-	Defined a method called check_guess that takes the guessed letter as a parameter.
-	Converts the guessed letter to lowercase.
-	Checks if the guess is in the word.
-	If the guess is in the word:
-	Replaces the corresponding "_" in the word_guessed with the guess.
-	Reduces num_letters by 1.
-	If the guess is not in the word:
-	Reduces num_lives by 1.
-	Prints a message saying "Sorry, {letter} is not in the word."
-	Prints another message saying "You have {num_lives} lives left."

-	Defined a method called ask_for_input.
-	Contains a while loop that runs continuously.
-	Asks the user to guess a letter and assigns it to a variable called guess.
-	Checks if the guess is a single alphabetical character and not already in the list_of_guesses.
-	If the guess passes the checks, it calls the check_guess method, passing in the guess as an argument.
-	Appends the guess to the list_of_guesses.


### Milestone 5: Enhancing the Gameplay Loop

**Usage**

- play_game Function
- Takes word_list as a parameter.
- Initializes a variable num_lives and assigns it to 5.
- Creates an instance of the Hangman class, assigning it to a variable called game, and passing word_list and num_lives as arguments.
-Contains a while loop with the condition set to True to control the game flow.
- Checks if num_lives is 0. If it is, the game has ended, and the user lost. It prints a message saying "You lost!"
- Checks if num_letters is greater than 0. In this case, it continues the game by calling the ask_for_input method.
- If num_lives is not 0 and num_letters is not greater than 0, it means the user has won the game. It prints a message saying "Congratulations. You won the game!"

## What I've Learned
 - Practicing Python programming, including working with lists, loops, and user input.
- Version control with Git, including cloning repositories, committing changes, 
and pushing code to remote repositories.
- Understanding and implementing the rules and logic of the Hangman game.
- Creating and maintaining project documentation using Markdown for README files.

## Thank you, AiCore, for this amazing experience!