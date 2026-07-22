from password_analyzer import analyze_password
from password_generator import generate_password
from reuse_checker import (
    is_password_reused,
    save_new_password
)
from database import create_database


def analyze_password_menu():

    print("\n" + "=" * 45)
    print("         PASSWORD ANALYSIS")
    print("=" * 45)

    password = input("Enter password to analyze: ")

    result = analyze_password(password)

    print("\nPassword Length:",
          len(password))

    print("Length Evaluation:",
          result["length_strength"])

    print("\nComplexity Score:",
          result["complexity_score"], "/ 40")

    print("\nFeatures Detected:")

    for feature in result["features"]:

        print("✓", feature)

    print("\nUniqueness Score:",
          result["uniqueness_score"], "/ 30")

    if result["warnings"]:

        print("\nWarnings:")

        for warning in result["warnings"]:

            print("⚠", warning)

    print("\n" + "-" * 45)

    print("TOTAL SCORE:",
          result["total_score"], "/ 100")

    print("FINAL STRENGTH:",
          result["strength"])

    print("-" * 45)


def generate_password_menu():

    print("\n" + "=" * 45)
    print("       STRONG PASSWORD GENERATOR")
    print("=" * 45)

    try:

        length = int(
            input("Enter password length: ")
        )

        if length < 8:

            print(
                "\nPassword length should be at least 8."
            )

            return

        password = generate_password(length)

        print("\nGenerated Password:")

        print(password)

    except ValueError:

        print("\nPlease enter a valid number.")


def password_reuse_menu():

    print("\n" + "=" * 45)
    print("       PASSWORD REUSE CHECKER")
    print("=" * 45)

    user_id = input("Enter User ID: ")

    password = input(
        "Enter password to check: "
    )

    if is_password_reused(
        user_id,
        password
    ):

        print("\n⚠ PASSWORD REUSE DETECTED")

        print(
            "This password has been used previously."
        )

    else:

        save_new_password(
            user_id,
            password
        )

        print(
            "\n✓ Password is new."
        )

        print(
            "Password saved securely."
        )


def main():

    create_database()

    while True:

        print("\n\n")

        print("=" * 50)

        print(
            "        PASSWORD SECURITY TOOL"
        )

        print("=" * 50)

        print("\n1. Analyze Password")

        print(
            "2. Generate Strong Password"
        )

        print(
            "3. Check Password Reuse"
        )

        print("4. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            analyze_password_menu()

        elif choice == "2":

            generate_password_menu()

        elif choice == "3":

            password_reuse_menu()

        elif choice == "4":

            print(
                "\nThank you for using the tool!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


if __name__ == "__main__":

    main()