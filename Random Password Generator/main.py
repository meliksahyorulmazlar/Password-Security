import random,pyperclip

lower_case_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

upper_case_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def main():
    print("Welcome to the password generator")
    password_list:list = []
    lower_cases:int = int(input("How many lower case letters would you like in your password?\n"))
    upper_cases:int = int(input("How many upper case letters would you like in your password?\n"))
    nums:int = int(input("How many numbers would you like in your password?\n"))
    punctuation_marks:int = int(input("How many punctuation marks would you like in your password?\n"))
    for i in range(lower_cases):
        password_list.append(random.choice(lower_case_letters))
    for j in range(upper_cases):
        password_list.append(random.choice(upper_case_letters))
    for k in range(nums):
        password_list.append(random.choice(numbers))
    for l in range(punctuation_marks):
        password_list.append(random.choice(punctuation))
    random.shuffle(password_list)
    password:str = "".join(password_list)
    print(password)
    pyperclip.copy(password)


if __name__ == "__main__":
    main()
