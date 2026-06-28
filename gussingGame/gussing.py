import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess a number (1-100): "))

    if userChoice == target:
        print("Congratulations! You guessed the correct number 😃")
        break

    elif userChoice < target:
        print("Too low! Try a bigger number. ⬆️")

    else:
        print("Too high! Try a smaller number. ⬇️")

print("---- GAME OVER ----")