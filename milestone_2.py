#import random

#word_list = ["apple", "banana", "kiwi", "grapes", "melon"]

#word = random.choice(word_list)
#print(word)

#guess = input("Enter a single letter: ")

#if len(guess)==1 and guess.isalpha():
	#print("Good guess!")
#else:
	#print("Oops! That is not a valid input."
import random

word_list = ["apple", "banana", "kiwi", "grapes", "melon"]

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")

if len(guess)==1 and guess.isalpha():
    if guess in word:
    	print("Good guess!")
    else:
        print("Oops! That is not a valid input.")


