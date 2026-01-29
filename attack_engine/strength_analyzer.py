import string


def analyze_password_strength(password):

    score = 0
    feedback = []

    length = len(password)

    # 🔹 Length Check (MOST IMPORTANT)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    else:
        feedback.append("Use at least 8 characters.")

    # 🔹 Uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # 🔹 Numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include numbers.")

    # 🔹 Special Characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # 🔹 Strength Rating
    if score <= 2:
        strength = "WEAK"
        risk = "HIGH RISK"
    elif score <= 4:
        strength = "MODERATE"
        risk = "MEDIUM RISK"
    else:
        strength = "STRONG"
        risk = "LOW RISK"

    return {
        "password": password,
        "length": length,
        "score": score,
        "strength": strength,
        "risk_level": risk,
        "feedback": feedback
    }
