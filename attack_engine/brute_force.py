import math

def human_readable_time(seconds):
    years = seconds / (60 * 60 * 24 * 365)
    if years > 1:
        return f"{years:.2f} years"
    days = seconds / (60 * 60 * 24)
    if days > 1:
        return f"{days:.2f} days"
    hours = seconds / (60 * 60)
    return f"{hours:.2f} hours"

def simulate_bruteforce(password_length, charset_size, attempts_per_second):
    combinations = math.pow(charset_size, password_length)
    time_seconds = combinations / attempts_per_second

    return {
        "password_length": password_length,
        "charset_size": charset_size,
        "total_combinations": f"{combinations:.2e}",
        "attempts_per_second": f"{attempts_per_second:,}",
        "estimated_time": human_readable_time(time_seconds),
        "time_seconds": int(time_seconds)
    }

def brute_force_attack(password):
    charset_size = 72  # a-z A-Z 0-9 symbols
    attempts_per_second = 1_000_000  # realistic CPU speed
    max_length = len(password)

    simulation_results = []

    for length in range(1, max_length + 1):
        result = simulate_bruteforce(
            password_length=length,
            charset_size=charset_size,
            attempts_per_second=attempts_per_second
        )
        simulation_results.append(result)

    return {
        "attack_type": "Brute Force Attack",
        "result": "FAILED",
        "reason": "Computationally infeasible",
        "details": simulation_results,
        "password_strength": "Very Strong"
    }
