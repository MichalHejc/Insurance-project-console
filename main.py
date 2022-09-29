class Client:

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

class InsuranceSystem:
    # Initialization of insurance system creates empty list_of_clients.
    def __init__(self, list_of_clients = None):
        self.list_of_clients = list_of_clients or []

    # Method for client creation. Next 3 methods (get_name, get_age and get_phone_number) serves for input validation.
    def create_client(self):
        name = self.get_name("jméno")
        surname = self.get_name("příjmení")
        age = self.get_age()
        phone_number = self.get_phone_number()
        client = Client(name, surname, age, phone_number)
        self.list_of_clients.append(client)
        print("Data byla uložena.\n")
    
    # Validates input name and surname - must contain only letters.
    def get_name(self, input_type):
        while True:
            name = input(f"Zadejte {input_type} pojištěného: \n").capitalize()
            if name.isalpha():
                return name
            else:
                print("Jméno nesmí obsahovat čísla ani speciální znaky.")
    
    # Validates input age - must be number (integer) higher than 0.
    def get_age(self):
        while True:
            try:
                age = int(input("Zadejte věk pojištěného: \n"))
                if age > 0:
                    return age
                else:
                    print("Věk nemůže být záporná hodnota.")
            except:
                print("Věk musí obsahovat pouze celá čísla.")
    
    # Validates input phone number - must be number longer than 9 digits, can contain "+" or empty spaces, which will be both removed in validation process.
    def get_phone_number(self):
        while True:
            phone_number = input("Zadejte telefonní číslo pojištěného: \n")
            if " " in phone_number or "+" in phone_number:
                phone_number = "".join([i for i in phone_number if i not in (" +")])
            if len(phone_number) >= 9:
                if phone_number.isdecimal():
                    return phone_number
                else:
                    print("Telefonní číslo nemůže obsahovat písmena ani speciální znaky.")
            else:
                print("Zadané telefonní číslo je příliš krátké.")
    
                


mich = Client("Michal", "Hejč", 32, 722353499)
kac = Client("Kateřina", "Sojková", 25, 766541256)
dlouhy = Client("Blablalbalba", "hafaen", 25, 654123574)

isys = InsuranceSystem()

isys.create_client()