from app.clients.ensembl import get_gene_location

data = get_gene_location("BRCA1")

print(data)