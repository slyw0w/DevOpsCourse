def login_required(func):
    def wrapper(*args, **kwargs):
        # Call the original function with all its arguments.
        # *args allows any number of positional arguments, and **kwargs allows any number of keyword arguments.
        # This ensures that the decorator works with functions of any signature.
        # The result of the original function is then returned to the caller.
        user_logged_in = True  # Example check
        print("Username is:",{user_logged_in})
        if not user_logged_in:
            return "Access denied. Please log in first."
        return func(*args, **kwargs)
    return wrapper


@login_required
def view_dashboard():
    return "Welcome to your dashboard!"

@login_required
def view_profile():
    return "This is your profile."

@login_required
def view_settings():
    return "These are your settings."

print(view_dashboard())
print(view_profile())
print(view_settings())