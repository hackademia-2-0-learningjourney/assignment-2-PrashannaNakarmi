'''
WAP that first gives 2 options: 
Sign up
Sign in

when 1 is pressed user needs to provide following information 
Username, 2. Password, 3. Mobile number
All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 


Do it using json files, save everything to json and load from json 
'''
import json

# file name
user_file = 'users.json'

#empty list if the file does not exist
try:
    with open(user_file, 'r') as file: #check if file exist
        users = json.load(file)
except:
    users = []

def save_users():
    with open(user_file, 'w') as file:
        json.dump(users, file, indent=4)

def sign_up():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    mobile_number = input("Enter mobile number: ").strip()

    # check if username exists
    for user in users:
        if user['username'] == username:
            print("Username already exists. Please choose a different username.")
            return

    # append new user
    users.append({
        'username': username,
        'password': password,
        'mobile_number': mobile_number
    })

    save_users()
    print("Sign up successful!")

def sign_in():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # check matching credentials
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Welcome! Your mobile number is: {user['mobile_number']}")
            return

    print("Incorrect username or password. Terminating the program.")
    exit()

print("1. Sign Up")
print("2. Sign In")

choice = input("Enter your choice 1 or 2: ").strip()

if choice == '1':
    sign_up()
elif choice == '2':
    sign_in()
else:
    print("Invalid choice. Please enter 1 or 2.")
