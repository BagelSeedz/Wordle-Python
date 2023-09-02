from wordlist import getWords
import random
import time

difficulty = int(input("Difficulty?: "))
maxGuesses = 6

words = getWords()

print("Searching For Word...")
randomWord = None
while True:
  randomWord = random.choice(words)
  if len(randomWord) == difficulty:
    break
  time.sleep(0.1)

currentList = ""
for i in range(difficulty):
  currentList = f"{currentList}_"

print(f"WORDLE! (HARD MODE) | {difficulty} Letter Word")
print("----------------------")
print(currentList)

beat = False
guessCount = 1
while True:
  print("----------------------")
  test = input(f"Guess {guessCount}/{maxGuesses}: ")
  if len(test) != difficulty:
    print(f"Please insert a {difficulty} letter word")
    continue

  alreadyFound = []
  for i in range(difficulty):
    for neededLetter in randomWord:
      if test[i] == neededLetter:
        letterFound = False
        for letter in alreadyFound:
          if letter == neededLetter:  
            letterFound = True
        if not letterFound:
          print(f"Discovered Letter {neededLetter}")
          alreadyFound.append(neededLetter)
        if test[i] == randomWord[i]:
          currentList = currentList[:i] + test[i] + currentList[i+1:]
    
  if currentList == randomWord:
    beat = True
    break
  elif guessCount == maxGuesses:
    break
  
  guessCount+=1
  print("----------------------")
  print(currentList)

if beat:
  print(f"You won! The word was {randomWord}.")
else:
  print(f"You lost. The word was {randomWord}.")
