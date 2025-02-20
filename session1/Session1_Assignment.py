#A.
a = 7
b = 44.3

# Result of adding first to second
print(a+b)

# Result of multiplying first by second
print(a*b)

# Result of dividing second by first
print(b/a)

#B.
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8
print(c)

#Final results
a = 9
b = 8
#C is 15 because only the last assignment matters so a = 9. the later changes to b happen after c is already executed so they dont affect the value of c.
c = 15 #(6+9)


#C. double qoutes are for text and single qoute behaves like an identifier. However, there is no real difference, you need to choose single or double qoutes depends on the context.

#the issue with the code is that you cant concatenate str with an int.

#suggested fix 1:
my_number = 5+5
print("my result is: " + str(+my_number))
#suggested fix 2:
my_number = 5+5
print(f"my result is: {my_number}")


#D. the result will be 7
x = 5
y = 2.36
print(x+int(y))

#CHALLENGE
a = 8
b = "123"
# wrong - print(a+b)
# fixed
print(a+int(b))