from client import Client
from insurance_system import InsuranceSystem

# Create test clients
novotny = Client("Petr", "Novotný", 32, 765432123)
vesela = Client("Marie", "Veselá", 25, 702701700)
stehlik = Client("Jan", "Stehlík", 42, 543111222)

# Create insurance system instance and append clients to "list_of_clients" database
isys = InsuranceSystem()
isys.list_of_clients.append(novotny)
isys.list_of_clients.append(vesela)
isys.list_of_clients.append(stehlik)

# Start of the program
isys.start_insurance_system()