#A.
x = 5
y = 3
if x > y:
    print("big")
elif x < y:
    print("small")

#B.
for i in range(5):
    print(f"Iteration number: {i}")

#C.
n = 2

if n == 1:
    print("summer")
elif n == 2:
    print("winter")
elif n == 3:
    print("fall")
elif n == 4:
    print("spring")

#D. the loop will run 10 times, the last print will be 10.

#E.
age = 30
last_name_initial = "Y"
shekel_dollar_rate = 0.27
flew_abroad = True
apartment_number = 10
print("Age:", age)
print("Last name initial:", last_name_initial)
print("Current shekel-dollar rate:", shekel_dollar_rate)
print("Flew abroad:", flew_abroad)
print("Apartment number:", apartment_number)

result = age + shekel_dollar_rate
print("Age plus shekel-dollar rate:", result)

#F.
phone_num = input("Please enter your phone number:" )
result = (f"phone number: {phone_num}")
print(result)

#G.
def printhello():
    print('Hello')
printhello()

def calculate():
    result = 5 + 3.2
    print(result)
calculate()

#H.
def entername(name):
    print(name)
entername('gal')

def n(a):
    result = a / 2
    print(result)
n(6)

#I.
def sum(a, b):
    result = a + b
    return result

def space(a, b):
    result = a + " " + b
    return result

#K.
for i in range(1,6):
    stars = ""
    for k in range(i):
        stars += "*"
    print(stars)

#L.
size = 7

for i in range(size):
    stars = ""
    for j in range(size):
        if j == i or j == (size - 1 - i):
            stars += "*"
        else:
            stars += " "
    print(stars)

#M.
def get_number():
    number = int(input("Please enter a number: "))
    return number

def sum_digits(number):
    total = 0
    while number%10 > 0:
       total += int(number%10)
       number = int(number/10)
    return total

num = get_number()
result = sum_digits(num)
print(f"The sum of digits in {num} is {result}")



