# Design a login and signup authentication system.


import os

def signup():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    
    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()
    
    print("Signup successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if not os.path.exists("users.txt"):
        print("No users found. Please sign up first.")
        return
        
    file = open("users.txt", "r")
    lines = file.readlines()
    file.close()
    
    for line in lines:
        stored_user, stored_pass = line.strip().split(",")
        if username == stored_user and password == stored_pass:
            print("Login successful! Welcome, " + username)
            return
            
    print("Invalid username or password.")

def main():
    while True:
        print("\n--- Authentication System ---")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()