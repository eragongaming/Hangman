#Words made of random letters

import random
import string
alphabet=[]
for x in string.ascii_lowercase:
    alphabet.append(x)
hangman=[]
length=int(input("How many letters do you want the word to be?: "))
randomamounts=[]
for x in range(length):
    randomamounts.append(random.randrange(25))
for value in randomamounts:
    hangman.append(alphabet[value])
fails=0
correct=0
guesses=[]
while fails<6 and correct<len(hangman):
    attempt=input("Enter a letter to guess: ")
    while attempt in guesses:
        print("You already guessed that, try again.\n")
        attempt = input("Enter a letter to guess: ")
    guesses.append(attempt)
    if attempt in hangman:
        print("Correct, {} is in the word!".format(attempt))
        correct+=1
    else:
        print("Incorrect, {} is not in the word. You have {} guesses remaining.".format(attempt,6-fails))
        fails+=1
show = ''
for x in hangman:
    show += x
if correct==len(hangman):
    print("You guessed the word! It was {}".format(hangman))
if fails==6:
    print("You did not guess the word, it was {}".format(hangman))
