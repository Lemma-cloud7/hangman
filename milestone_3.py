# Step 1: Create a while loop that runs continuously
while True: 
# Step : Ask the user to guess a letter and assign it to the "guess" variable    
    guess = input("Guess a letter: ")

#Step 3: Check if "guess" is a single alphabetical character
    if guess.isalpha() and len(guess) == 1: 
#Step 4:  If the guess passes the check, break out of the loop
        break
    else:
#Step 5: If the guess does not pass the check, print error messege
        print ("Invalid letter. Please, enter a single alphabetical character.")

#The program will continue once a valid letter is entered
print(f"You guessed: {guess}")