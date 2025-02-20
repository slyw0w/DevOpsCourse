# import sys
# import time
#
# #1.
# def input_output_demo():
#     user_name = input("What's your name? ")
#     try:
#         user_age = int(input("How old are you? "))
#         age_in_future = user_age + 10
#         response = f"Hey {user_name}, in a decade, you'll be {age_in_future} years old!\n"
#         print(response)
#         with open("output_log.txt", "w") as file:
#             file.write(response)
#     except ValueError:
#         sys.stderr.write("Oops! Please provide a valid numeric value for age.\n")
#
# #2.
# def log_errors():
#     try:
#         age_input = int(input("Please enter your age: "))
#         print(f"Great! You are {age_input} years old.")
#     except ValueError:
#         sys.stderr.write("Error: Age must be a numerical value.\n")
#
#
# #3.
# def read_write_file():
#     file_name = "records.txt"
#     with open(file_name, "a+") as file:
#         file.writelines([f"Entry {i}\n" for i in range(1, 6)])
#     with open(file_name, "r") as file:
#         print(file.read())
#
# #4.
# def copy_binary_file():
#     try:
#         with open("records.txt", "rb") as src, open("backup.bin", "wb") as dest:
#             dest.write(src.read())
#     except FileNotFoundError:
#         print("Error: Source file 'records.txt' is missing.")
#
#
# #5.
# def count_words():
#     try:
#         with open("story.txt", "r") as file:
#             content = file.read().lower().replace(",", "").replace(".", "")
#             words_list = content.split()
#             word_frequencies = {word: words_list.count(word) for word in set(words_list)}
#
#         with open("word_stats.txt", "w") as output_file:
#             for word, freq in word_frequencies.items():
#                 output_file.write(f"{word}: {freq}\n")
#
#     except FileNotFoundError:
#         print("Oops! The file 'story.txt' could not be found.")
#
# #6.
# def missing_file_handler():
#     try:
#         with open("story.txt", "r") as file:
#             print(file.read())
#     except FileNotFoundError:
#         print("File not found! Please provide another file name.")
#         alt_filename = input("Enter the file name: ")
#         try:
#             with open(alt_filename, "r") as file:
#                 print(file.read())
#         except FileNotFoundError:
#             print("Sorry, that file is also missing. Exiting now.")
#
# #7.
# def divide_safely():
#     while True:
#         try:
#             number1 = float(input("Enter the first number: "))
#             number2 = float(input("Enter the second number: "))
#             division_result = number1 / number2
#             print(f"Result: {division_result}")
#             break
#         except ZeroDivisionError:
#             print("Warning: Division by zero is not possible. Try again.")
#         except ValueError:
#             print("Invalid input! Please enter numeric values only.")
#
# #8.
# def debugging_demo():
#     num_list = list(range(1, 11))
#     doubled_values = []
#
#     for num in num_list:
#         try:
#             doubled_values.append(num * 2)
#         except TypeError:
#             print(f"Unexpected error when processing {num}.")
#
#     print(doubled_values)
#
# 9.
# def function_decorator(func):
#     def wrapped():
#         print("Execution starting...")
#         func()
#         print("Execution completed.")
#     return wrapped
#
# @function_decorator
# def say_hello():
#     print("Greetings, world!")
#
# #10.
# def execution_timer(func):
#     def wrapped(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Function completed in {end - start:.4f} seconds")
#         return result
#     return wrapped
#
# @execution_timer
# def compute_large_sum():
#     print(sum(range(1, 1_000_001)))
#
#
# if __name__ == "__main__":
#     print("Executing Various Functions...\n")
#     input_output_demo()
#     log_errors()
#     read_write_file()
#     copy_binary_file()
#     count_words()
#     missing_file_handler()
#     divide_safely()
#     debugging_demo()
#     say_hello()
#     compute_large_sum()
#     print("\nAll tasks completed successfully!")