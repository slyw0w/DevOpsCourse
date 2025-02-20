#1.
age = 25
height = 5.8
name = "Alex"

print(age, type(age))
print(height, type(height))
print(name, type(name))

#2.
num1 = int(input("choose your first number:"))
num2 = int(input("choose your second number:"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

#3.
x = 10
x += 5
print(x)

#4.
num1 = int(input("Choose your first number:"))
num2 = int(input("Choose your second number:"))
if num1 > num2:
    print("Greater")
elif num1 < num2:
    print("Less than")
else:
    print("Equal")

#5.
x = 8
y = 6
if x == y:
    print("Equal")
else:
    print("Not equal")

#6.
num = int(input("choose your number:"))
if num%2 == 0:
    print("Even")
else:
    print("Odd")

#7.
base = 6
base = base**3
print(base)

#8.
num1 = int(input("Choose your first number: "))
num2 = int(input("Choose your second number: "))
operator = input("Enter operator (+, -, *, /): ")
result = 0

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator")

print("The result is: ", result)

#9.
num = int(input("Choose your number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#10.
x = [1, 2, 3, 4 ,5]
print(x[0], x[4])