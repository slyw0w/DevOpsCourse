import random
import time
# #1.
# def calculator_challenge():
#     print("Welcome to the Ultimate Calculator!")
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Choose an operation (+, -, *, /): ")
#
#     if operation == "+":
#         print(f"Result: {num1 + num2}")
#     elif operation == "-":
#         print(f"Result: {num1 - num2}")
#     elif operation == "*":
#         print(f"Result: {num1 * num2}")
#     elif operation == "/":
#         if num2 == 0:
#             print("Error: Division by zero is not allowed!")
#         else:
#             print(f"Result: {num1 / num2}")
#     else:
#         print("Invalid operation. Please try again!")
#
# calculator_challenge()

# #2.
# def number_guess_game():
#     print("Guess the Number Game!")
#     secret_num = random.randint(1, 100)
#     attempts = 0
#
#     while True:
#         try:
#             player_guess = int(input("Guess a number between 1-100: "))
#             attempts += 1
#             if player_guess < secret_num:
#                 print("Too low! Try a bigger number.")
#             elif player_guess > secret_num:
#                 print("Too high! Try a smaller number.")
#             else:
#                 print(f"Awesome! You got it in {attempts} tries.")
#                 break
#         except ValueError:
#             print("Oops! Please enter a valid number.")

# #3.
# def rps_game():
#     print("Let's play Rock-Paper-Scissors!")
#     options = ["rock", "paper", "scissors"]
#     player_choice = input("Pick rock, paper, or scissors: ").lower()
#     ai_choice = random.choice(options)
#
#     if player_choice not in options:
#         print("Invalid choice! Please select a valid option.")
#         return
#
#     print(f"Computer chose: {ai_choice}")
#     if player_choice == ai_choice:
#         print("It's a draw!")
#     elif (player_choice == "rock" and ai_choice == "scissors") or \
#          (player_choice == "paper" and ai_choice == "rock") or \
#          (player_choice == "scissors" and ai_choice == "paper"):
#         print("You won!")
#     else:
#         print("You lost!")

# #4.
# def find_the_treasure():
#     print("Treasure Hunt Begins!")
#     treasure_x, treasure_y = random.randint(1, 5), random.randint(1, 5)
#
#     while True:
#         try:
#             guess_x = int(input("Guess X coordinate (1-5): "))
#             guess_y = int(input("Guess Y coordinate (1-5): "))
#
#             if (guess_x, guess_y) == (treasure_x, treasure_y):
#                 print("Hooray! You found the hidden treasure!")
#                 break
#             else:
#                 print("No treasure here. Keep searching!")
#         except ValueError:
#             print("Please enter numbers only between 1 and 5.")

# #5.
# def memory_challenge():
#     print("Memory Test Begins!")
#     pattern = []
#
#     for round_num in range(1, 5):
#         pattern.append(random.randint(1, 9))
#         print(f"\nRound {round_num}: Memorize this pattern: {pattern}")
#
#         time.sleep(1)
#         print("\n" * 50)  # Clears screen by pushing content out
#
#         input("Press Enter when you're ready to recall...")
#         user_guess = input("Enter the pattern (space-separated numbers): ")
#
#         try:
#             user_sequence = list(map(int, user_guess.split()))
#         except ValueError:
#             print("Oops! Enter numbers only.")
#             return
#
#         if user_sequence != pattern:
#             print("Incorrect sequence! Game over.")
#             return
#
#         print("Nice work! Moving to the next round.")
#
#     print("Fantastic! Your memory skills are impressive.")

# #6.
# def rpg_game():
#     print("Prepare for Battle!")
#     foes = [("Ghost", 20), ("Skeleton", 60), ("Dragon", 100)]
#
#     for enemy in foes:
#         name, hp = enemy
#         print(f"A wild {name} appeared with {hp} HP!")
#         while hp > 0:
#             damage = random.randint(5, 20)
#             hp -= damage
#             print(f"You strike {name} for {damage} damage. Remaining HP: {max(0, hp)}")
#         print(f"The {name} has been defeated!\n")
#
#     print("Victory! You conquered all enemies!")

# #7.
# def adventure_game():
#     print("Welcome to the Mystery House!")
#     locations = {
#         "lobby": {"desc": "You stand in the lobby. Doors lead elsewhere.", "paths": ["kitchen", "study"]},
#         "kitchen": {"desc": "You're in the kitchen. Something smells delicious.", "paths": ["lobby"]},
#         "study": {"desc": "You're in the study. It's eerily quiet.", "paths": ["lobby"]},
#     }
#
#     current_place = "lobby"
#
#     while True:
#         print(locations[current_place]["desc"])
#         move = input(f"Where next? Options: {locations[current_place]['paths']}: ").lower()
#
#         if move in locations[current_place]["paths"]:
#             current_place = move
#         else:
#             print("That path is not an option!")

# #8.
# def roll_die_game():
#     print("Rolling the Dice!")
#
#     while True:
#         try:
#             sides = int(input("How many sides does your die have? "))
#             if sides < 1:
#                 raise ValueError("The die must have at least one side!")
#
#             roll_result = random.randint(1, sides)
#             print(f"You rolled a {roll_result}!")
#             break
#         except ValueError as e:
#             print(f"Invalid input: {e}. Please try again.")

