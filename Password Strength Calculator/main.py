import math


lower_case_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

upper_case_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


def main():
    print("Welcome to the password entropy/strength calculator")
    password:str = input("What is your password\n")
    length:int = len(password)
    character_set_size = 0
    dict = {"lower":0,"upper":0,"numbers":0,"punctuation":0}
    for character in password:
        if character in lower_case_letters:
            dict["lower"] = 26
        elif character in upper_case_letters:
            dict["upper"] = 26
        elif character in numbers:
            dict["numbers"] = 10
        elif character in punctuation:
            dict["punctuation"] = 32
    for key,value in dict.items():
        character_set_size += value
    print(character_set_size)

    password_entropy:float = length * math.log(character_set_size,2)

    print(f"Your password has an entropy of {password_entropy} bits")
    t = pow(character_set_size,length)/(2 * (1e9)) /(86400*365.25)

    print(f"It would take {t:.6f} years to crack your password with a billion guesses per second if there aren't any common words in your password")

if __name__ == "__main__":
    main()













