import customtkinter as ctk

from password_analyzer import analyze_password
from password_generator import generate_password

from reuse_checker import (
    is_password_reused,
    save_new_password
)

from database import create_database


# -----------------------------
# APPEARANCE
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def toggle_password():

    if password_entry.cget("show") == "*":

        # Currently hidden → show password
        password_entry.configure(show="")

        show_button.configure(
            text="Hide"
        )

    else:

        # Currently visible → hide password
        password_entry.configure(show="*")

        show_button.configure(
            text="Show"
        )

def display_analysis(password):

    result = analyze_password(password)

    score = result["total_score"]

    strength_bar.set(score / 100)

    output = ""

    output += f"Length: {len(password)} characters\n"

    output += (
        f"Length Evaluation: "
        f"{result['length_strength']}\n\n"
    )

    output += (
        f"Complexity Score: "
        f"{result['complexity_score']}/40\n"
    )

    output += (
        f"Uniqueness Score: "
        f"{result['uniqueness_score']}/30\n"
    )

    output += (
        f"Total Score: "
        f"{score}/100\n\n"
    )

    output += (
        f"FINAL STRENGTH: "
        f"{result['strength']}\n"
    )

    if result["warnings"]:

        output += "\nWARNINGS:\n"

        for warning in result["warnings"]:

            output += "⚠ " + warning + "\n"

    output += "\nSUGGESTIONS:\n"

    if len(password) < 12:

        output += (
            "→ Use at least 12 characters.\n"
        )

    if result["complexity_score"] < 40:

        output += (
            "→ Use uppercase, lowercase, numbers "
            "and special characters.\n"
        )

    if result["uniqueness_score"] < 30:

        output += (
            "→ Avoid common words and predictable patterns.\n"
        )

    if (
        len(password) >= 12
        and result["complexity_score"] == 40
        and result["uniqueness_score"] == 30
    ):

        output += (
            "✓ Password meets all basic criteria.\n"
        )

    result_label.configure(
        text=output
    )

def analyze_password_gui():

    password = password_entry.get()

    if password == "":

        result_label.configure(
            text="Please enter a password."
        )

        strength_bar.set(0)

        return

    display_analysis(password)

def generate_password_gui():

    password = generate_password(16)

    password_entry.delete(
        0,
        "end"
    )

    password_entry.insert(
        0,
        password
    )

    display_analysis(password)

def check_reuse_gui():

    user_id = user_id_entry.get()

    password = password_entry.get()

    if user_id == "":

        result_label.configure(
            text="Please enter a User ID."
        )

        return

    if password == "":

        result_label.configure(
            text="Please enter a password."
        )

        return

    if is_password_reused(
        user_id,
        password
    ):

        result_label.configure(

            text=(
                "⚠ PASSWORD REUSE DETECTED\n\n"
                "This password was previously used."
            )

        )

    else:

        save_new_password(
            user_id,
            password
        )

        result_label.configure(

            text=(
                "✓ PASSWORD ACCEPTED\n\n"
                "This is a new password.\n"
                "Password hash saved securely."
            )

        )


create_database()

app = ctk.CTk()

app.title(
    "Password Strength Checker"
)

app.geometry(
    "850x850"
)

title_label = ctk.CTkLabel(

    app,

    text="PASSWORD STRENGTH CHECKER",

    font=("Arial", 28, "bold")

)

title_label.pack(
    pady=20
)

user_id_entry = ctk.CTkEntry(

    app,

    width=500,

    height=40,

    placeholder_text="Enter User ID"

)

user_id_entry.pack(
    pady=10
)

input_frame = ctk.CTkFrame(
    app
)

input_frame.pack(
    pady=10
)


password_entry = ctk.CTkEntry(

    input_frame,

    width=500,

    height=45,

    placeholder_text="Enter password",

    show="*"

)

password_entry.grid(

    row=0,

    column=0,

    padx=10

)


show_button = ctk.CTkButton(

    input_frame,

    text="Show",

    width=80,

    command=toggle_password

)

show_button.grid(

    row=0,

    column=1,

    padx=10

)

analyze_button = ctk.CTkButton(

    app,

    text="ANALYZE PASSWORD",

    width=300,

    height=40,

    command=analyze_password_gui

)

analyze_button.pack(
    pady=10
)


generate_button = ctk.CTkButton(

    app,

    text="GENERATE STRONG PASSWORD",

    width=300,

    height=40,

    command=generate_password_gui

)

generate_button.pack(
    pady=10
)


reuse_button = ctk.CTkButton(

    app,

    text="CHECK PASSWORD REUSE",

    width=300,

    height=40,

    command=check_reuse_gui

)

reuse_button.pack(
    pady=10
)

strength_bar = ctk.CTkProgressBar(

    app,

    width=500,

    height=20

)

strength_bar.pack(
    pady=15
)

strength_bar.set(0)

result_label = ctk.CTkLabel(

    app,

    text="Enter a password to begin.",

    font=("Arial", 16),

    justify="left"

)
result_label.pack(
    pady=20
)

app.mainloop()