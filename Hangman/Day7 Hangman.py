stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']










import random
word_list = ["ardvark" , "baboon" , "camel"]

word = random.choice(word_list)
print(word)

display = []

len = int(len(word))
lives = 6
count = 0
for _ in range(len):
    display += "_"


while count >= 0:
    guess = input("Guess a letter: ")
    for position in range(len):
        if word[position] == guess:
            display[position] = guess

    if guess not in word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lost")
            count = -1
    print(display)

    if "_" not in display:
        count -= 1
        print("You Win!")











