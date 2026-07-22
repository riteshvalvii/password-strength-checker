import bcrypt


def hash_password(password):

    password_bytes = password.encode("utf-8")

    return bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )


def verify_password(password, hashed_password):

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )