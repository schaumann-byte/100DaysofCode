import random


#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#chosen_word = random.choice(word_list)
chosen_word = word_list[random.randint(0,2)]
print(chosen_word)

guess = input("Guess a letter: ")
guess_lower = guess.lower()

for i in range(0,len(chosen_word)):
  if guess_lower in chosen_word[i]:
      print("Right")
  else:
      print("Wrong")