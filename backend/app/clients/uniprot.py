import requests

BASE_URL = "https://rest.uniprot.org"


def get_protein_data(gene_symbol: str):

    url = (
        f"{BASE_URL}/uniprotkb/search"
        f"?query=gene:{gene_symbol}+AND+organism_id:9606"
        f"&format=json"
        f"&size=1"
    )

    response = requests.get(url)

    return response.json()