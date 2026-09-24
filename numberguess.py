import random

def play_number_guessing_game(max_attempts):
  number = random.randint(1, 100)
  attempt = 0 # 

  print(f"\nYou have {max_attempts} attempts to guess the number.")

  while attempt < max_attempts:
    try:
      guess = int(input("Guess the number: "))
      attempt += 1
    except ValueError:
      print("Invalid input. Please enter an integer.")
      continue 

    if guess == number:
      print("Congratulations! You guessed the number in", attempt, "attempts.")
      return 
    elif guess < number:
      print("Too low! Try again.")
    else:
      print("Too high! Try again.")

  print("Sorry, you've run out of attempts. The number was", number)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

print("Please choose difficulty level:")
print("1. Easy (10 attempts)")
print("2. Medium (7 attempts)")
print("3. Hard (5 attempts)")

difficulty_choice = input("Enter the difficulty level (1/2/3): ")

if difficulty_choice == "1":
  play_number_guessing_game(10)
elif difficulty_choice == "2":
  play_number_guessing_game(7)
elif difficulty_choice == "3":
  play_number_guessing_game(5)
else:
    print("Invalid difficulty level. Please choose 1, 2, or 3.")
