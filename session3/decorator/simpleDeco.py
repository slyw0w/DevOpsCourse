# Step 1: Define a decorator function
def my_decorator(func):
    # Define the wrapper function that adds behavior around the original function
    def wrapper():
        # This code runs before the original function
        print("Something is happening before the function is called.")
        func()  # Call the original function
        # This code runs after the original function
        print("Something is happening after the function is called.")
    return wrapper  # Return the wrapper function

# Step 2: Use the decorator
@my_decorator  # This is equivalent to: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello, World!")  # Original function logic

# Step 3: Call the decorated function
say_hello()