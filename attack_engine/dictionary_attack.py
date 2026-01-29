import time

def dictionary_attack(target_password, password_file="common_passwords.txt"):

    start_time = time.time()
    attempts = 0

    try:
        with open(password_file, "r", encoding="utf-8") as file:
            for line in file:
                attempts += 1
                guessed_password = line.strip()

                if guessed_password == target_password:
                    end_time = time.time()

                    return {
                        "password_found": guessed_password,
                        "attempts": attempts,
                        "time_taken": round(end_time - start_time, 4),
                        "attack_type": "Dictionary Attack"
                    }

    except FileNotFoundError:
        print("Password file not found!")
        return None

    return {
        "message": "Password not found in dictionary.",
        "attempts": attempts,
        "attack_type": "Dictionary Attack"
    }
