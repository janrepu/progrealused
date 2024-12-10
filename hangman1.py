import random

print("Hangman davai noh ütle sõna")
print("-------------------------------------------")

wordDictionary = ["maja", "lill", "tont", "janre","neeger","sõna", "hey", "mida", "markus"]


randomWord = random.choice(wordDictionary)

for x in randomWord:
  print("_", end=" ")

def print_hangman(vale):
  if(vale == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(vale == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(vale == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(vale == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(vale == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(vale == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(vale == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")

def printWord(guessedLetters):
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
paljuvale = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(paljuvale != 6 and current_letters_right != length_of_word_to_guess):
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")

  letterGuessed = input("\nGuess a letter: ")

  if(randomWord[current_guess_index] == letterGuessed):
    print_hangman(paljuvale)

    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()

  else:
    paljuvale+=1
    current_letters_guessed.append(letterGuessed)

    print_hangman(paljuvale)

    current_letters_right = printWord(current_letters_guessed)
    printLines()

print("MÄNG LÄBI")
