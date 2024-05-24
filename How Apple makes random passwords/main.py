#How Apple makes random passwords

#There are 2 types of passwords that apple makes

#one is known as easy to type
#which in total has 20 characters
#It always consists of:
#One upper case letter
#Sixteen lower cases
#Two hyphens, one on the 7th positon and another one on the 14th position
#One number that is left or right of the hyphen or the last character of the password


#The other one is known as no special characters which has a length of 15 characters
#this one does not have any punctuation it only consists of lower,upper case letters and numbers
#It can consist of 1 to 6 numbers
#It can consist of 1 to 11 upper case letters (from my data I have found 1 to 10 upper case letters.However, I believe that if i have more passwords the upper case letters can consist of 1 to 11 upper case letters)
#It can consist of 1 to 11 lower case letters
#Which will add up to a total of 15 characters
import random,pyperclip

class ApplePassword:
    def __init__(self):
        self.lower_cases:list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.upper_cases:list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.numbers:list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    def EasyToType(self)->None:
        password_list:list = [random.choice(self.lower_cases) for i in range(20)]


        password_list[6] = "-"
        password_list[13] = "-"

        random_number: str = str(random.randint(0, 9))
        possible_number_positions = [5,7,12,14,19]
        number_position = random.choice(possible_number_positions)
        password_list[number_position] = random_number


        upper_letter = random.choice(self.upper_cases)
        possible_upper_positions = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19]
        possible_upper_positions.remove(number_position)
        upper_position = random.choice(possible_upper_positions)
        password_list[upper_position] = upper_letter

        password = "".join(password_list)

        print(password)
        # The following line of code will copy the password for you to your clipboard
        pyperclip.copy(password)




    def NoSpecialCharacters(self)->None:

        lower_case_count:int = random.randint(1,11)
        upper_case_count:int = random.randint(1,(11-lower_case_count+1))
        numbers:int = 15 - (lower_case_count+upper_case_count)

        password_list = []

        for i in range(lower_case_count):
            password_list.append(random.choice(self.lower_cases))
        for j in range(upper_case_count):
            password_list.append(random.choice(self.upper_cases))
        for k in range(numbers):
            password_list.append(random.choice(self.numbers))

        random.shuffle(password_list)
        password:str = ''.join(password_list)


        print(password)
        #The following line of code will copy the password for you to your clipboard
        pyperclip.copy(password)


if __name__ == "__main__":
    password = ApplePassword()
    type = input("Do you want an easy password or password with no special characters?\n")
    if type == "easy":
        password.EasyToType()
    else:
        password.NoSpecialCharacters()