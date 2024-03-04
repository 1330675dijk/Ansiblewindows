import csv

# Define the column headers
headers = ["Voornaam", "Achternaam", "Adres", "Postcode", "Plaatsnaam", "Gebruikersnaam"]

# Prompt the user for input
data = []
for header in headers[:-1]:  # Exclude Gebruikersnaam from user input
    value = input(f"Enter {header}: ")
    if header == "Achternaam":
        # Replace spaces with dots in the last name
        value = value.replace(" ", ".")
    data.append(value)

# Create Gebruikersnaam by combining Voornaam and Achternaam with a dot and converting to lowercase
gebruikersnaam = (data[0] + "." + data[1]).lower()
data.append(gebruikersnaam)

# Specify the CSV file name
csv_filename = "gegevens.csv"

# Check if the file already exists
file_exists = False
try:
    with open(csv_filename, 'r') as file:
        file_exists = True
except FileNotFoundError:
    pass

# Write to CSV
with open(csv_filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write headers if the file is new
    if not file_exists:
        writer.writerow(headers)
    
    # Write user input data
    writer.writerow(data)

print(f"Data (with spaces replaced with dots in Achternaam, Gebruikersnaam added in lowercase) appended to CSV file '{csv_filename}' successfully.")
