# a = 1 # integer
# a = 5 # > python takes the most recent file, it reads it from top to bottom so the one of the bottom is the newest one
# b = 2.3 # float
# c = "Jay" # string
# d = True # Boolean
# e = "1ewrwt" #
# f = 'Jay' #
# string1="1234"
# string2="5678"
# string3="9213"
# print(a,b,c)
# print("my name is:",c)
# print(string1+string2+string3)

# names = ["jay", "sofie", "nadav",1,b,True] # list note that the we are using []
# print(names[1])

# dictionary01 = {"name": ["jay", "sofie", "nadav", "tammy"], "Hobbie": "basketball"}
# print(dictionary01["name"])
# dictionary will ALWAYS starts with {} and NOT []
# in a dictionary ({}) you can have many dictionary and lists ([])

course = {"name": {"age": {"class": [True, False]}, "gender": ["male", "female"]}, "Hobbie": "basketball"}

#
#
# print(course["name"]["age"]["class"][1])
# the dictionary below is preferable as it looks better
# dictionary = {
#     "name": "jay"
#     "Gender": "male"
# }

# Modulo (%) = calculates the remainder of a division operation
a = 9 % 5
b = 7
c = 14
d = c/b
# print(d)
# print(d != a)
# print(b > c)

# a = 4*2
# b = 4/4
# c = 4 % 2
# d = 1+1
# sum= (a + b + c)*d
# print(a,b,c,d)
# print(sum)
# helloworld = "hello" + "world" # if i want to print 2 strings to gether i just use +
# print(helloworld)

# user = input("Please Enter your name:")
# print(f"Your name is: {user}")
# print("Your name is:", user)
# print(f"Your name is {{ {user} }} and you are a devops engineer")
# print("your name is:",user,"and you are a devops engineer")
#
# number = float(input("Please enter a number:"))
# number2 = float(input("Please enter a number:"))
#
# # sum = int(number) + int(number2)
# # print(int(number)+int(number2))
# sum = number + number2
# print(int(sum))
# sum = sum + 6
# print(sum)

number = int(input("Please enter a number:"))
if 10 < number < 15:
    print(f"{number} is Bigger than 10 and smaller than 15")


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
