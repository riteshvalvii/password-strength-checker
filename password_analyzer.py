import string


def check_length(password):

    length = len(password)

    if length < 8:
        return 0, "Very Weak"

    elif length < 12:
        return 15, "Weak"

    elif length < 16:
        return 25, "Strong"

    else:
        return 30, "Very Strong"


def check_complexity(password):

    score = 0
    features = []

    if any(char.islower() for char in password):
        score += 10
        features.append("Lowercase letters")

    if any(char.isupper() for char in password):
        score += 10
        features.append("Uppercase letters")

    if any(char.isdigit() for char in password):
        score += 10
        features.append("Numbers")

    if any(char in string.punctuation for char in password):
        score += 10
        features.append("Special characters")

    return score, features


def check_uniqueness(password):

    common_passwords = [
        "password",
        "password123",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "letmein",
        "welcome"
    ]

    score = 30
    warnings = []

    password_lower = password.lower()

    if password_lower in common_passwords:

        score = 0

        warnings.append(
            "This is a commonly used password"
        )

    if len(set(password)) <= 3:

        score -= 15

        warnings.append(
            "Too many repeated characters"
        )

    if "123" in password or "abc" in password.lower():

        score -= 10

        warnings.append(
            "Contains a predictable sequence"
        )

    return max(score, 0), warnings


def analyze_password(password):

    length_score, length_strength = \
        check_length(password)

    complexity_score, features = \
        check_complexity(password)

    uniqueness_score, warnings = \
        check_uniqueness(password)

    total_score = (
        length_score
        + complexity_score
        + uniqueness_score
    )

    if total_score < 30:

        strength = "Very Weak"

    elif total_score < 50:

        strength = "Weak"

    elif total_score < 70:

        strength = "Moderate"

    elif total_score < 85:

        strength = "Strong"

    else:

        strength = "Very Strong"

    return {

        "length_score": length_score,

        "length_strength": length_strength,

        "complexity_score": complexity_score,

        "features": features,

        "uniqueness_score": uniqueness_score,

        "warnings": warnings,

        "total_score": total_score,

        "strength": strength

    }