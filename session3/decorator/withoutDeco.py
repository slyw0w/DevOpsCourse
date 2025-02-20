def view_dashboard():
    return "Welcome to your dashboard!"

@login_required
def view_dashboard():
    return "Welcome to your dashboard!"

def view_profile():
    user_logged_in = True  # Example check
    if not user_logged_in:
        return "Access denied. Please log in first."
    return "This is your profile."

def view_settings():
    user_logged_in = True  # Example check
    if not user_logged_in:
        return "Access denied. Please log in first."
    return "These are your settings."


print(view_dashboard())
print(view_profile())
print(view_settings())