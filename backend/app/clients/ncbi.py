import requests

BASE_URL = (
    "https://eutils.ncbi.nlm.nih.gov/"
    "entrez/eutils/esearch.fcgi"
)

def search_genes_by_disease(disease: str):

    params = {
        "db": "gene",
        "term": disease,
        "retmode": "json",
        "retmax": 10
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def get_gene_summary(gene_id: str):

    url = (
        "https://eutils.ncbi.nlm.nih.gov/"
        "entrez/eutils/esummary.fcgi"
    )

    params = {
        "db": "gene",
        "id": gene_id,
        "retmode": "json"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()