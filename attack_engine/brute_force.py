import itertools
import string
import time


def brute_force_attack(target_password, max_length=4):
    
    characters = string.ascii_lowercase + string.digits
    start_time = time.time()

    attempts = 0

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            
            attempts += 1
            guessed_password = ''.join(guess)

            if guessed_password == target_password:
                
                end_time = time.time()
                
                return {
                    "password_found": guessed_password,
                    "attempts": attempts,
                    "time_taken": round(end_time - start_time, 2)
                }

    return None
