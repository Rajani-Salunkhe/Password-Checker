#Password strength checker
import re
#password strength checker conditions
#(minimum 8 characters, uppercase letter, Lowercase letter, digit, special character)

def check_password_strength(password):
    if len(password)<8:
        return "Weak: Password must be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit"
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak: Password must contain lowercase letter"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Medium: Password must contain at least one special character"
    
    return "Strong: Your Password is secured!"    

def password_checker():
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower()== "exit":
            print("Thank you for using this tool!")
            break
        result=check_password_strength(password)
        print(result)

#Run the password checker
if __name__ == "__main__":
    password_checker()

    
