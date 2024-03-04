import csv

# Define the column headers
headers = ["Voornaam", "Achternaam", "Adres", "Postcode", "Plaatsnaam"]

# Prompt the user for input
data = []
for header in headers:
    value = input(f"Enter {header}: ")
    # Remove spaces from the entered value
    value = value.replace(" ", "")
    data.append(value)

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

print(f"Data (with spaces removed) appended to CSV file '{csv_filename}' successfully.")
