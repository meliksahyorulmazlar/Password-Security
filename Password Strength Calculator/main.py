import math
import string

CHAR_SETS: dict = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "numbers": string.digits,
    "punctuation": string.punctuation,
}

CHAR_SIZES: dict = {
    "lower": 26,
    "upper": 26,
    "numbers": 10,
    "punctuation": 32,
}

def main() -> None:
    print("Welcome to the password entropy/strength calculator")
    password: str = input("What is your password?\n")
    length: int = len(password)

    character_set_size: int = sum(
        CHAR_SIZES[key] for key, chars in CHAR_SETS.items() if any(c in chars for c in password)
    )

    print(character_set_size)
    password_entropy: float = length * math.log(character_set_size, 2)
    print(f"Your password has an entropy of {password_entropy:.2f} bits")

    crack_time: float = pow(character_set_size, length) / (2 * 1e9) / (86400 * 365.25)
    print(f"It would take {crack_time:.6f} years to crack your password at a billion guesses per second.")

if __name__ == "__main__":
    main()
