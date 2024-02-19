import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")
display = []
for _ in chosen_word:
  display += "_"
print(display)
guess = input("Guess a letter: ").lower()
list = []
for position in range(len(chosen_word)):
  if guess == chosen_word[position]:
    display[position] = guess
print(display)
