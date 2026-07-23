from app.clients.ncbi import get_gene_summary

data = get_gene_summary("672")

gene = data["result"]["672"]

print("Name:", gene["name"])
print("Description:", gene["description"])
print("Chromosome:", gene["chromosome"])