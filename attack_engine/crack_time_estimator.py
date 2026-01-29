import math
import string


def estimate_crack_time(password):

    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += 32

    # total combinations
    combinations = charset ** len(password)

    # assume attacker can try 1 BILLION passwords/sec
    guesses_per_second = 1_000_000_000

    seconds = combinations / guesses_per_second

    return seconds

def format_time(seconds):

    if seconds < 60:
        return f"{seconds:.2f} seconds"

    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.2f} minutes"

    hours = minutes / 60
    if hours < 24:
        return f"{hours:.2f} hours"

    days = hours / 24
    if days < 365:
        return f"{days:.2f} days"

    years = days / 365
    return f"{years:.2f} years"

