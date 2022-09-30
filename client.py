class Client:
    # Create client with name, surname, age and phone_number
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        # Variables 'max_len' and 'char_counter' serves to align the content of the string (adds desired number of free spaces between name and age).
        max_len = 25
        char_counter = len(f'{self.name} {self.surname}')
        string = f'{self.name} {self.surname} {(max_len - char_counter) * " "}{self.age}        {self.phone_number}'
        return string