import os
# # 'r' - Open a file for reading
#
# try:
#     with open('example.txt', 'r') as file:
#         content = file.read()
#         print("Reading from file 'example.txt':")
#         print(content)
# except FileNotFoundError:
#     print("File 'example.txt' not found.")

# # Program 1: write_name.py
# def write_name_to_file():
#     # Get name from user
#     name = input("Please enter a name: ")
#
#     # Open file in append mode ('a')
#     with open('names.txt', 'a') as file:
#         # Write the name and add a newline
#         file.write(name + '\n')
#
#     print(f"Added {name} to names.txt")
#
#
# # Program 2: greet_names.py
# def read_and_greet():
#     try:
#         # Open and read the file
#         with open('names.txt', 'r') as file:
#             # Read all lines
#             names = file.readlines()
#
#         # Check if file is empty
#         if not names:
#             print("No names found in the file!")
#             return
#
#         print("Greetings to everyone:")
#         # Greet each name
#         for name in names:
#             # Remove newline character and any extra whitespace
#             name = name.strip()
#             print(f"Hello {name}! Have a wonderful day and may all your dreams come true!")
#
#     except FileNotFoundError:
#         print("The names.txt file was not found!")
#
#
# # Demonstration of using both programs
# if __name__ == "__main__":
#     print("Adding three different names:")
#
#     # Call the first program three times
#     for i in range(3):
#         print(f"\nEntering name {i + 1}:")
#         write_name_to_file()
#
#     print("\nNow reading and greeting all names:")
#     read_and_greet()

# # Checking if "data.txt" exists in the current directory
# if os.path.exists('data.txt'):
#     print("'data.txt' exists in the current directory.")
# else:
#     print("'data.txt' does not exist in the current directory.")

# # Copying contents of "source.txt" to "destination.txt"
# try:
#     with open('source.txt', 'r') as source_file:
#         content = source_file.read()
#
#     with open('destination.txt', 'w') as destination_file:
#         destination_file.write(content)
#         print("Contents of 'source.txt' have been copied to 'destination.txt'.")
# except FileNotFoundError:
#     print("'source.txt' does not exist.")

# # ValueError example:
# try:
#     user_input = "abc"  # Invalid input for conversion
#     number = int(user_input)  # Will raise ValueError
# except ValueError as e:
#     print("Error: Invalid input. Please enter a valid integer.",e)

# # PermissionError example:
# try:
#     with open('test_file.txt', 'w') as file:  # Trying to write to a restricted file
#         file.write("This will fail due to permissions.")
# except PermissionError as e:
#     print("Error: You don't have permission to modify this file.", e)

# # Multiple Exceptions example:

# try:
#     num_list = [1, 2, 3]
#     index = 5  # Out of range
#     result = num_list[index] / 0  # Will raise an error before division
# except IndexError:
#     print("Error: Index is out of range.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# # KeyboardInterrupt example:
#
# try:
#     print("Press Ctrl+C to interrupt...")
#     while True:
#         pass  # Simulating a long-running task
# except KeyboardInterrupt:
#     print("\nProgram interrupted by the user.")

# # FileNotFoundError example:
#
# try:
#     with open('nonexistent_file.txt', 'r') as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Error: The file does not exist.")

# # Finally example:
#
# try:
#     file = open('example1.txt', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: File not found.")
# finally:
#     print("Execution complete.")

# Need to go over this lesson again either with itamar/gali or rewatch it or watch the python course

# #Debugger example1:
# def calculate_average(numbers):
#     """
#     Calculate the average of a list of numbers.
#     """
#     total = 0
#     for num in numbers:
#         total += num
#     # Logical bug: should divide by len(numbers)
#     average = total / len(numbers)  # Error if numbers is empty
#     return average
#
#
# def find_maximum(numbers):
#     """
#     Find the maximum number in a list.
#     """
#     # Logical bug: starts with 0 instead of first number
#     max_num = 0
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
#
#
# if __name__ == "__main__":
#     numbers = [2, 8, 3, 7, 10]
#
#     print("Debugging Demonstration")
#     print("Original list:", numbers)
#
#     # Call calculate_average (set a breakpoint here)
#     try:
#         average = calculate_average(numbers)
#         print("Average:", average)
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero. The list may be empty.")
#
#     # Call find_maximum (set another breakpoint here)
#     max_num = find_maximum(numbers)
#     print("Maximum:", max_num)
#

# #Debugger example2:
# def reverse_words(sentence):
#     """
#     Reverse the words in a given sentence.
#     """
#     words = sentence.split()  #split is to take a string and to take out every word into a list # Handle extra spaces automatically
#     reversed_sentence = " ".join(reversed(words))
#     return reversed_sentence
#
#
# def count_vowels(sentence):
#     """
#     Count the number of vowels in a given sentence.
#     """
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in sentence:
#         if char in vowels:
#             count += 1
#     return count
#
#
# # Get the sentence from user input
# test_sentence = input("Enter a sentence: ")
#
# print("\nDebugging with Strings Example")
# print("Original sentence:", repr(test_sentence))
#
# # Call reverse_words
# reversed_sentence = reverse_words(test_sentence)
# print("Reversed sentence:", repr(reversed_sentence))
#
# # Call count_vowels
# vowel_count = count_vowels(test_sentence)
# print("Number of vowels:", vowel_count)

#Debugger example3:
from fibo import fib,fib2,eduard
print("Fibonacci Series Demonstration")

# # Get user input for Fibonacci functions
# try:
#     n = int(input("Enter a positive integer for Fibonacci calculations: "))
#     if n <= 0:
#         raise ValueError("The number must be positive.")
#
#     print("\nUsing fib(n) to print the series up to n:")
#     fib(n)
#
#     print("\nUsing fib2(n) to return the series as a list:")
#     fib_series = fib2(n)
#     print(fib_series)
#
# except ValueError as e:
#     print("Invalid input:", e)
#
# # Using eduard function
# print("\nUsing the eduard() function:")
# eduard_value = eduard()
# print(f"The eduard function returned: {eduard_value}")
