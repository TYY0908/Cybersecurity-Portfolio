import getpass
import re


COMMON_PASSWORDS = {
    "password",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "letmein",
    "welcome",
    "iloveyou",
}


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters; 12 or more is better.")

    checks = {
        "lowercase letter": r"[a-z]",
        "uppercase letter": r"[A-Z]",
        "number": r"\d",
        "symbol": r"[^A-Za-z0-9]",
    }

    for label, pattern in checks.items():
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(f"Add at least one {label}.")

    normalized = password.lower()
    if normalized in COMMON_PASSWORDS:
        score = 0
        feedback.append("Avoid common passwords.")

    if re.search(r"(.)\1{2,}", password):
        score -= 1
        feedback.append("Avoid repeated characters like aaa or 111.")

    if re.search(r"(1234|abcd|qwer|password)", normalized):
        score -= 1
        feedback.append("Avoid predictable sequences or words.")

    score = max(score, 0)

    if score >= 6:
        rating = "Strong"
    elif score >= 4:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, score, feedback


def main():
    password = getpass.getpass("Enter a password to check: ")
    rating, score, feedback = check_password_strength(password)

    print(f"\nStrength: {rating} ({score}/6)")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("No major issues found.")


if __name__ == "__main__":
    main()
