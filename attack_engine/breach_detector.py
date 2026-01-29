def check_breach(password, breach_file="breached_passwords.txt"):

    try:
        with open(breach_file, "r", encoding="utf-8", errors="ignore") as file:
            breached = {line.strip() for line in file}

        if password in breached:
            return True
        else:
            return False

    except FileNotFoundError:
        print("Breach dataset not found!")
        return False
