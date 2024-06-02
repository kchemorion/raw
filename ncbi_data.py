# ncbi_data.py

from Bio import Entrez

# Define NCBI API settings
Entrez.email = "your-email@example.com"

# Function to search NCBI
def search_ncbi(query, database="pubmed"):
    handle = Entrez.esearch(db=database, term=query, retmax=10)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

# Function to fetch NCBI data
def fetch_ncbi_data(ids, database="pubmed"):
    handle = Entrez.efetch(db=database, id=ids, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    return records
