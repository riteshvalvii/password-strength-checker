from database import (
    create_database,
    get_password_history,
    save_password_hash
)

from security import (
    hash_password,
    verify_password
)


def is_password_reused(user_id, password):

    password_history = get_password_history(user_id)

    for stored_hash in password_history:

        stored_hash = stored_hash[0]

        if verify_password(password, stored_hash):

            return True

    return False


def save_new_password(user_id, password):

    hashed_password = hash_password(password)

    save_password_hash(
        user_id,
        hashed_password
    )


if __name__ == "__main__":

    create_database()

    user_id = input("Enter User ID: ")

    password = input("Enter New Password: ")

    if is_password_reused(user_id, password):

        print("\n⚠ PASSWORD REUSE DETECTED")

        print("This password was used previously.")

    else:

        save_new_password(user_id, password)

        print("\n✓ New password saved successfully.")