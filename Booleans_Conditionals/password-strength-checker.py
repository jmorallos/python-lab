import re

password = "developer@123"

is_valid = password.strip() != "" and 6 < len(password) <= 16

if is_valid:
    has_number = any(char.isdigit() for char in password)
    strong_pattern = re.compile('[^a-zA-Z0-9]')
    
    weak_password = len(password) < 8
    medium_password = len(password) > 8 and has_number
    strong_passowrd = bool(medium_password) and bool(strong_pattern.search(password))
    
    if weak_password:
        print("Weak")
    if medium_password:
        print("medium")
    if strong_passowrd:
        print("strong")
else:
    print("Password is not valid")