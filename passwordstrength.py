def check_pass_strength(password):
    strength = 0
    
    
    if len(password) >= 8:
        strength += 1
        
    
    if any(char.isupper() for char in password):
        strength += 1
        
    
    if any(char.islower() for char in password):
        strength += 1
        
    
    if any(char.isdigit() for char in password):
        strength += 1
        
    
    special_chars = "!@#$%&*"
    if any(char in special_chars for char in password):
        strength += 1

    
    if strength <= 2:
        return "Weak Password "
    elif strength == 3 or strength == 4:
        return "Medium Password "
    else:
        return "Strong Password "



password = input("Enter your password: ")
print(check_pass_strength(password))