import csv
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the output file path
output_file = 'fake_people.csv'

# Open the CSV file and write data
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Name", "Address", "Email"])
    
    # Write 100 rows of fake data
    for _ in range(100):
        name = fake.name()
        address = fake.address().replace('\n', ', ')  # Replace line breaks in addresses
        email = fake.email()
        writer.writerow([name, address, email])

print(f"CSV file 'fake_people.csv' has been created.")