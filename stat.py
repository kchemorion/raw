from Bio import Entrez

# Always set your email when using Entrez
Entrez.email = "your-email@example.com"  # Replace with your actual email

# Retrieve detailed information about a specific database (e.g., 'pubmed')
handle = Entrez.einfo(db="pubmed")
record = Entrez.read(handle)
handle.close()

# Print database description
print(f"Database: {record['DbInfo']['DbName']}")
print(f"Description: {record['DbInfo']['Description']}")
print(f"Last Update: {record['DbInfo']['LastUpdate']}")
print("Available Fields:")
for field in record['DbInfo']['FieldList']:
    print(f" - {field['Name']}: {field['Description']}")
