from app.clients.uniprot import get_protein_data

data = get_protein_data("BRCA1")

print(data)