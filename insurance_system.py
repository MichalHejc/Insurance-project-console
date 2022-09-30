from client import Client

class InsuranceSystem:
    # Initialization of insurance system creates empty list_of_clients.
    def __init__(self, list_of_clients = None):
        self.list_of_clients = list_of_clients or []

    # Method for client creation. Next 3 internal methods (get_name, get_age and get_phone_number) serves for input validation.
    def create_client(self):
        name = self._get_name("jméno")
        surname = self._get_name("příjmení")
        age = self._get_age()
        phone_number = self._get_phone_number()
        client = Client(name, surname, age, phone_number)
        self.list_of_clients.append(client)
        print("\nData byla uložena.\n")
    
    # Validates input name and surname - must contain only letters.
    def _get_name(self, input_type):
        while True:
            name = input(f"Zadejte {input_type} pojištěného: \n").capitalize()
            if name.isalpha():
                return name
            else:
                print("\nJméno nesmí obsahovat čísla ani speciální znaky.")
    
    # Validates input age - must be number (integer) higher than 0.
    def _get_age(self):
        while True:
            try:
                age = int(input("Zadejte věk pojištěného: \n"))
                if age > 0:
                    return age
                else:
                    print("\nVěk nemůže být záporná hodnota.")
            except ValueError:
                print("\nVěk musí obsahovat pouze celá čísla.")
    
    # Validates input phone number - must be number equal or longer than 9 digits, can contain "+" or empty spaces, which will be both removed in validation process.
    def _get_phone_number(self):
        while True:
            phone_number = input("Zadejte telefonní číslo pojištěného: \n")
            if " " in phone_number or "+" in phone_number:
                phone_number = "".join([i for i in phone_number if i not in (" +")])
            if len(phone_number) >= 9:
                if phone_number.isdecimal():
                    return phone_number
                else:
                    print("\nTelefonní číslo nemůže obsahovat písmena ani speciální znaky.")
            else:
                print("\nZadané telefonní číslo je příliš krátké.")

    # Prints list of all clients.
    def print_all_clients(self):
        print("\nPOJIŠTĚNÝ", " " * 15, "VĚK", " " * 5, "TEL. ČÍSLO")
        for client in self.list_of_clients:
            print(client)
        print()

    # Search of client based on first name and surname. Accepts names in lowercase too. Returns client object and its index in list_of_clients.
    def search_client(self):
        name = input("Zadejte křestní jméno pojištěného:\n").capitalize()
        surname = input("Zadejte příjmení pojištěného:\n").capitalize()

        in_database = False
        for index, client in enumerate(self.list_of_clients):
            if name == client.name and surname == client.surname:
                print("\nPOJIŠTĚNÝ", " " * 15, "VĚK", " " * 5, "TEL. ČÍSLO")
                print(client, "\n")
                in_database = True
                return index, client
        if not in_database:
            print("\nTento pojištěný v databázi není.\n")
    
    # Delete client method uses "search_client" method to find client first. Than deletes client with its index returned from "search_client" method.
    def delete_client(self):
        print("\nMAZÁNÍ POJIŠTĚNÉHO")
        try:
            index, client = self.search_client()
        except TypeError:
            return
        confirmation = input("\nOpravdu chcete pojištěného smazat? (ano/ne): ").lower()
        if confirmation == "ano":
            del self.list_of_clients[index]
            print(f"\nPojištěný {client.name} {client.surname} ({client.age}) byl smazán z databáze.\n")

    # Allows to edit clients data, based on users input choice (name,surname,age or phone number).
    def edit_client(self):
        print("\nÚPRAVA POJIŠTĚNÉHO")
        try:
            index, client = self.search_client()
        except TypeError:
            return
        
        while True:
            edit = input("Který údaj chcete upravit?\n1 - Jméno\n2 - Příjmení\n3 - Věk\n4 - Telefonní číslo\n5 - Žádný (zpět)\n")
            if edit == "1":
                self.list_of_clients[index].name = self._get_name("jméno")
                print("Jméno pojištěného upraveno.\n")
                break
            elif edit == "2":
                self.list_of_clients[index].surname = self._get_name("příjmení")
                print("Příjmení pojištěného upraveno.\n")
                break
            elif edit == "3":
                self.list_of_clients[index].age = self._get_age()
                print("Věk pojištěného upraven.\n")
                break
            elif edit == "4":
                self.list_of_clients[index].phone_number = self._get_phone_number()
                print("Telefonní číslo pojištěného upraveno.\n")
                break
            elif edit == "5":
                break
            else:
                print("Tato možnost není v nabídce.")

    # This method starts insurance program. Takes action based on users input choice.
    def start_insurance_system(self):
        while True:
            print("\n---------------------\nEvidence pojištěných\n---------------------")
            choice = input("Vyberte akci:\n1 - Vypsat všechny pojištěné\n2 - Přidat nového pojištěného\n3 - Vyhledat pojištěného\n4 - Upravit pojištěného\n5 - Smazat pojištěného\n6 - Ukončit program\n")
            if choice == "1":
                self.print_all_clients()
            elif choice == "2":
                self.create_client()
            elif choice == "3":
                self.search_client()
            elif choice == "4":
                self.edit_client()
            elif choice == "5":
                self.delete_client()
            elif choice == "6":
                break
            else:
                print("Tato možnost není v nabídce.")
            input("Pokračujte stisknutím klávesy enter.")

        print("\nProgram ukončen. Hezký den.")