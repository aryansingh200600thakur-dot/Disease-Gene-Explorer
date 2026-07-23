from app.clients.ncbi import (
    search_genes_by_disease,
    get_gene_summary
)

from app.cache.memory_cache import cache


def get_disease_genes(disease: str):

    disease = disease.lower()

    if disease in cache:

        print("CACHE HIT")

        return cache[disease]

    print("NCBI FETCH")

    search_data = search_genes_by_disease(disease)

    ids = search_data["esearchresult"]["idlist"]

    genes = []

    for gene_id in ids:

        summary = get_gene_summary(gene_id)

        gene = summary["result"][gene_id]

        genes.append(
            {
                "gene_id": gene_id,
                "symbol": gene.get("name"),
                "description": gene.get("description"),
                "chromosome": gene.get("chromosome"),
                "source":
                    f"https://www.ncbi.nlm.nih.gov/gene/{gene_id}"
            }
        )

    result = {
        "disease": disease,
        "genes": genes
    }

    cache[disease] = result

    return result