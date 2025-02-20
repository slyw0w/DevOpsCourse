# number = int(input("Please enter a number:"))
# # if 15 < number < 15:
# #     print(f"{number} is Bigger than 10 and smaller than 15")
# #
# # if 10 < number and number % 2 == 0:
# #     print(f"{number} is Bigger than 10 and smaller than 15")
#
# if 10 < number or number < 15:
#     print(f"{number} is Bigger than 10 and smaller than 15")
#
#     if number == 14:
#         print("Bingo!!!")
# elif 15 < number < 20:
#     print(f"{number} is between 15-20")
# else:
#     if number < 10:
#         print(f"{number} is smaller than 10")
#     if number > 15:
#         print(f"{number} is bigger than 15")
#     else:
#         print("Not a number")
# from itertools import count

# my_dict = {'name': 'John', 'age': 25, 'country': 'USA'}
# my_dict2 = {'name':['John','edi','daniel'] , 'age': 25, 'country': 'USA'}
# print(my_dict2["name"][1])
# name = 0
# for name in my_dict2["name"]:
#     print(name)
#     if name != "David":
#         my_dict2["name"].append("David")
#
# print(my_dict2.keys())


# for num in range(1, 101):
#     if num % 7 != 0 and '7' not in str(num):
#         print(num)
#         print()
#
#     else:
#         print("BOOM!")

# name = input("Please enter a name")
# b=0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(len(numbers))
# while b < 10:
#     while True:
#         for b in range(10)
# for b in range(len(numbers)):
#     print(numbers[b],b)
# for b in numbers:
#     print(b)

# while True:
#     try:
#         a = int(input("enter first number: "))
#         b = int(input("enter second number: "))
#         result = a / b
#         print(result)
#         break
#     except ValueError:
#         print("enter a correct number")
#     except ZeroDivisionError:
#         print("could not divide by zero")
#     except BaseException as e:
#         print(e.args)

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

# count=0
# while(count<5):
#     print(count)
#     count +=1
# else:
#     print("count value reached %d" %(count))
#
# # Prints out 1,2,3,4
# for i in range(1, 10):
#     if(i%5==0):
#         break
#     print(i)
# else:
#     print("this is not printed because for loop is terminated because of break but not due to fail in condition")


# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]
# for num in numbers:
#     if num == 237:
#         break
#     if num%2==0:
#         print(num)


# you can create a function locally and call it by using the command "import" and then it will import the WHOLE function.
# if you need just something specific from the function you can call it by using "from (function_name) import (action)"

# import arithmetic_actions
# from arithmetic_actions import multiplication

# number1 = int(input("Pick a number: "))
# number2 = int(input("Pick a number: "))

# print(arithmetic_actions.addition(multiplication (number1 ,number2), arithmetic_actions.division(number1 ,number2)))


# next lesson we are going to study about flask package

# for final project please keep conventions, the name of the project will be World of Games