from app.clients.ncbi import search_genes_by_disease

result = search_genes_by_disease("breast cancer")

print(result)