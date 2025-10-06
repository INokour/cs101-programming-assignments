print("Registration Form")

in_progress = True

errors = []
warnings = []
message_data = {}

if in_progress:
    errors = []
    first_name = input("First name: ").strip()

    if first_name == "":
        errors.append("First Name not entered. You must enter a first name!")
    elif len(first_name) < 2:
        errors.append("First Name entered is too short (<2 Characters).")
    elif len(first_name) > 30:
        errors.append("First Name entered unusually long (<2 Characters).")
    elif not first_name.replace("-", "").replace("'", "").isalpha():
        errors.append("First name contains invalid characters")
        first_name_valid = False
    else:
        first_name_valid = True
        message_data["first_name"] = first_name.title()

    last_name = input("Last name: ").strip()

    if last_name == "":
        errors.append("First Name not entered. You must enter a first name!")
    elif len(last_name) < 2:
        errors.append("Last Name entered is too short (<2 Characters).")
    elif len(last_name) > 30:
        errors.append("Last Name entered unusually long (<2 Characters).")
    elif not last_name.replace("-", "").replace("'", "").isalpha():
        errors.append("Last name contains invalid characters")
        first_name_valid = False
    else:
        first_name_valid = True
        message_data["last_name"] = last_name.title()

    email = input("Email address: ").strip().lower()
    email_valid = True
    if email == "":
        errors.append("Email is required")
        email_valid = False
    elif " " in email:
        errors.append("Email cannot contain spaces")
        email_valid = False
    elif email.count("@") != 1:
        errors.append("Email must contain exactly one @ symbol")
        email_valid = False
    else:
        
        # Split email into parts
        parts = email.split("@")
        local = parts[0]
        domain = parts[1]

        # Check local part (before @)
        if len(local) == 0:
            errors.append("Email missing username before @")
            email_valid = False
        elif local[0] == "." or local[-1] == ".":
            errors.append("Email username cannot start or end with period")
            email_valid = False
        elif ".." in local:
            errors.append("Email username cannot have consecutive periods")
            email_valid = False
        # Check domain part (after @)
        if len(domain) < 3:
            errors.append("Email domain too short")
            email_valid = False
        elif "." not in domain:
            errors.append("Email domain must contain a period")
            email_valid = False
        elif domain[0] == "." or domain[-1] == ".":
            errors.append("Email domain cannot start or end with period")
            email_valid = False

        elif ".." in domain:
            errors.append("Email domain cannot have consecutive periods")
            email_valid = False
        else:
            # Check for common typos
            common_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
            domain_lower = domain.lower()
        if domain_lower in ["gmail", "yahoo", "hotmail"]:
            warnings.append(f"Did you mean {domain_lower}.com?")
            message_data["email"] = email
    subject = input("Enter Subject: ")
    if len(subject) > 100:
        errors.append("Subject is greater than 100 characters.")

    message_data["subject"] = subject
    
    message = input("Enter Message: ")
    if len(message) < 10:
        errors.append("Message is too short! Must be 10+ characters.")
    elif len(message) > 500:
        errors.append("Message is too long! Must be <500 characters.")
    message_data["message"] = message
    
    if len(errors) > 0:
        print("You have errors, message cannot be sent.")
        for error in errors:
            print(error)
            in_progress = True
    else:
        print("Message sent!")
        print(message_data)