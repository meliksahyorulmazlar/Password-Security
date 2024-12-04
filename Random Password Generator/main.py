import random
import string
import pyperclip
from typing import List, Tuple

def main() -> None:
    """
    Generates a random password based on user input specifying the number of different character types
    (lowercase letters, uppercase letters, numbers, punctuation marks) to include in the password.
    The password is then printed and copied to the clipboard.
    """
    print("Welcome to the password generator")

    # List of tuples containing the count and corresponding character set
    char_types: List[Tuple[int, str]] = [
        (int(input(f"How many {type_} would you like in your password?\n")), chars)
        for type_, chars in [
            ("lower case letters", string.ascii_lowercase),
            ("upper case letters", string.ascii_uppercase),
            ("numbers", string.digits),
            ("punctuation marks", string.punctuation)
        ]
    ]

    password_list: List[str] = [random.choice(chars) for count, chars in char_types for _ in range(count)]
    random.shuffle(password_list)

    # Join the list into a string and print the password
    password: str = ''.join(password_list)
    print(password)
    pyperclip.copy(password)

if __name__ == "__main__":
    main()
