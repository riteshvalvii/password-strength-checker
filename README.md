# Password Strength Checker

A Python-based password security tool that evaluates password strength based on password length, complexity, and uniqueness.

The application also generates strong passwords and helps prevent password reuse by securely storing password hashes using bcrypt and SQLite.

## Features

- Password length evaluation
- Password complexity analysis
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- Password uniqueness analysis
- Password strength score out of 100
- Strength classification
- Security warnings
- Password improvement suggestions
- Strong password generation
- Secure password hashing using bcrypt
- Password reuse prevention
- SQLite database integration
- Graphical user interface using CustomTkinter

## Technologies Used

- Python
- CustomTkinter
- SQLite
- bcrypt
- secrets module

## Project Structure

```text
Password_Strength_Checker/
│
├── .gitignore
├── README.md
├── requirements.txt
├── database.py
├── gui.py
├── main.py
├── password_analyzer.py
├── password_generator.py
├── reuse_checker.py
└── security.py

## Intern ID
CITS9061