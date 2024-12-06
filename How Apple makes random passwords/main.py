import random
import string
import pyperclip
from typing import List


class ApplePassword:
    """
    A class to generate passwords following Apple's password creation rules.

    Apple generates two types of passwords:

    1. **Easy-to-Type Password (20 characters)**:
       - One uppercase letter.
       - Sixteen lowercase letters.
       - Two hyphens: one on the 7th position and another on the 14th position.
       - One number placed either left or right of the hyphen or at the last position of the password.

    2. **No Special Characters Password (15 characters)**:
       - This password does not contain any punctuation and consists only of:
         - Lowercase letters.
         - Uppercase letters.
         - Numbers.
       - Number of characters:
         - 1 to 6 numbers.
         - 1 to 11 uppercase letters (based on observed data, 1 to 10 uppercase letters is typical, but further analysis may allow up to 11).
         - 1 to 11 lowercase letters.
       - The total length is always 15 characters.

    Methods:
    --------
    easy_to_type() -> None:
        Generates a random "easy-to-type" password based on Apple's rules.

    no_special_characters() -> None:
        Generates a random password with no special characters, based on the second rule.
    """

    def __init__(self) -> None:
        self.lower_cases: str = string.ascii_lowercase
        self.upper_cases: str = string.ascii_uppercase
        self.numbers: str = string.digits

    def easy_to_type(self) -> None:
        # Create base password with placeholders for hyphens
        password_list: List[str] = [random.choice(self.lower_cases) for _ in range(20)]
        password_list[6], password_list[13] = "-", "-"

        # Insert number
        number_pos: int = random.choice([5, 7, 12, 14, 19])
        password_list[number_pos] = random.choice(self.numbers)

        # Insert uppercase letter
        upper_pos: int = random.choice([i for i in range(20) if i not in {6, 13, number_pos}])
        password_list[upper_pos] = random.choice(self.upper_cases)

        # Generate and copy password
        generated_password: str = "".join(password_list)
        print(generated_password)
        pyperclip.copy(generated_password)

    def no_special_characters(self) -> None:
        # Randomly distribute characters
        lower_case_count: int = random.randint(1, 11)
        upper_case_count: int = random.randint(1, 11 - lower_case_count + 1)
        numbers_count: int = 15 - (lower_case_count + upper_case_count)

        password_list: List[str] = (
            [random.choice(self.lower_cases) for _ in range(lower_case_count)] +
            [random.choice(self.upper_cases) for _ in range(upper_case_count)] +
            [random.choice(self.numbers) for _ in range(numbers_count)]
        )

        random.shuffle(password_list)
        generated_password: str = "".join(password_list)

        print(generated_password)
        pyperclip.copy(generated_password)


if __name__ == "__main__":
    password: ApplePassword = ApplePassword()
    password_type: str = input("Password type ('easy' for simple, anything else for no special characters):\n").lower()

    match password_type:
        case "easy":
            password.easy_to_type()
        case _:
            password.no_special_characters()
