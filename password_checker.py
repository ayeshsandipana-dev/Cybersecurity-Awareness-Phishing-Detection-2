import re


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin123",
    "letmein",
    "welcome123",
}


def check_password_strength(password):

    if not isinstance(password, str):
        raise TypeError("Password must be text")

    if not password:
        return {
            "score": 0,
            "strength": "INVALID",
            "feedback": ["Password cannot be empty"]
        }

    score = 0
    feedback = []

    # Password length
    if len(password) >= 16:
        score += 40

    elif len(password) >= 12:
        score += 30

    elif len(password) >= 8:
        score += 15

    else:
        feedback.append(
            "Use a longer password (at least 12 characters)"
        )

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Consider adding uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Consider adding lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Consider adding numbers")

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Consider adding special characters")

    # Common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append(
            "This password is commonly used and unsafe"
        )

    # Repeated characters
    if re.search(r"(.)\1{3,}", password):
        score = max(0, score - 20)
        feedback.append(
            "Avoid repeating the same character"
        )

    score = min(score, 100)

    if score >= 80:
        strength = "STRONG"

    elif score >= 50:
        strength = "MEDIUM"

    else:
        strength = "WEAK"

    if not feedback:
        feedback.append(
            "Password passes the selected strength checks"
        )

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


if __name__ == "__main__":

    test_passwords = [
        "123456",
        "password123",
        "MySecurePassword2026!",
    ]

    for password in test_passwords:

        result = check_password_strength(password)

        print("\nStrength:", result["strength"])
        print("Score:", result["score"])
        print("Feedback:", result["feedback"])