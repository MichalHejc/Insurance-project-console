class Client:

    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        """
        Variables 'max_len' and 'char_counter' serves to align the content of the string (adds desired number of free spaces between name and age).
        """
        max_len = 25
        char_counter = len(f'{self.name} {self.surname}')
        string = f'{self.name} {self.surname} {(max_len - char_counter) * " "}{self.age}        {self.phone_number}'
        return string

class InsuranceSystem:
    
    def __init__(self, list_of_clients = None):
        self.list_of_clients = list_of_clients or []
    
    def create_client(self):
        name = input("Zadejte jméno pojištěného: \n")
        surname = input("Zadejte příjmení pojištěného: \n")
        age = input("Zadejte věk pojištěného: \n")
        phone_number = input("Zadejte telefonní číslo pojištěného: \n")

    def validate_input(self, input):
        pass


mich = Client("Michal", "Hejč", 32, 722353499)
kac = Client("Kateřina", "Sojková", 25, 766541256)
dlouhy = Client("Blablalbalba", "hafaen", 25, 654123574)

isys = InsuranceSystem()
print(isys.list_of_clients)
isys.create_client()