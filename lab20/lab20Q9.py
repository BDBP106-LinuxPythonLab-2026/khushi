# 9. Password Validator
# Concepts: "until" loop, for over characters, isupper()/islower()/isdigit(), a set of special
# characters, flags
# Keep asking for a password until it meets all of these rules:
# • at least 8 characters
# • at least one uppercase letter, one lowercase letter and one digit
# • at least one special character from {"!", "@", "#", "$", "%", "&", "*"}
# • no spaces
# • doesn't contain the word "password" in any case
# After each failed attempt, list every rule that was broken, not just the first one.

special_chars = {"!", "@", "#", "$", "%", "&", "*"}

while True:
    password = input("Enter a password: ")
    errors = []

    # Check length
    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    # Flags
    upper = False
    lower = False
    digit = False
    special = False
    space = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True

        if ch in special_chars:
            special = True

        if ch == " ":
            space = True

    # Check all rules
    if not upper:
        errors.append("Password must contain at least one uppercase letter.")

    if not lower:
        errors.append("Password must contain at least one lowercase letter.")

    if not digit:
        errors.append("Password must contain at least one digit.")

    if not special:
        errors.append("Password must contain at least one special character.")

    if space:
        errors.append("Password must not contain spaces.")

    if "password" in password.lower():
        errors.append("Password must not contain the word 'password'.")

    # Display results
    if len(errors) == 0:
        print("Password is valid!")
        break
    else:
        print("Invalid password. Please fix the following errors:")
        for error in errors:
            print("-", error)