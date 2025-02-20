import requests
import random
from selenium import webdriver

# #1.
# username = "avielb"
# url = f"https://api.github.com/users/{username}/repos"
# response = requests.get(url)
#
# if response.status_code == 200:
#     repositories = response.json()
#
#     if len(repositories) >= 5:
#         print(f"User '{username}' has {len(repositories)} repositories.")
#     else:
#         print(f"User '{username}' has only {len(repositories)} repositories, less than the required 5.")
#
# else:
#     print("Failed to fetch repositories. Status code:", response.status_code)

# #2.
# import names
#
# for i in range(3):  # Generate 3 random names
#     random_name = names.get_first_name()  # Get a random first name
#     response = requests.get(f"https://api.agify.io/?name={random_name}")
#
#     if response.status_code == 200:
#         age = response.json().get("age", -1)  # Get the predicted age
#         print(f"Name: {random_name}, Predicted Age: {age}, Valid: {0 <= age <= 120}")
#     else:
#         print(f"Failed to fetch data for {random_name}. Status code: {response.status_code}")

# #3.
#
# url = "http://universities.hipolabs.com/search?country=Israel"
# response = requests.get(url)
#
# if response.status_code == 200:
#     universities = response.json()
#     university_count = len(universities)
#
#     if university_count >= 5:
#         print(f"Israel has {university_count} universities.")
#     else:
#         print(f"Israel has only {university_count} universities, which is below the required 5.")
#
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")

# #4.
# driver = webdriver.Chrome()
# driver.get("https://www.ycombinator.com/")
# page_title = driver.title
#
# if page_title == "Y Combinator":
#     print("Title is correct: 'Y Combinator'")
# else:
#     print(f"Title mismatch! Expected: 'Y Combinator', Got: '{page_title}'")
#
# driver.quit()

# #5.
# driver = webdriver.Chrome()
# driver.get("https://hub.docker.com")
# page_title = driver.title
#
# if page_title == "Docker Hub Container Image Library | App Containerization":
#     print("The title is correct: Docker Hub Container Image Library | App Containerization")
# else:
#     print(f"Title mismatch! Expected: 'Y Combinator', Got: '{page_title}'")