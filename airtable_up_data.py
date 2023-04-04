
import csv
from airtable import Airtable

# Configura tus credenciales de Airtable
API_KEY = 'keytvdDDYw0Jbmdk6'
BASE_ID = 'YOUR_BASE_ID'
TABLE_NAME = 'YOUR_TABLE_NAME'

# Inicializa el cliente de Airtable
airtable = Airtable(BASE_ID, TABLE_NAME, API_KEY)

# Función para leer un archivo CSV y devolver una lista de diccionarios
def read_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
    return rows

# Función para subir registros a Airtable
def upload_to_airtable(data):
    for row in data:
        airtable.insert(row)

# Ejemplo de uso
csv_file_path = 'your_data.csv'  # Reemplaza esto
