import requests

BASE_URL = "https://rest.ensembl.org"


def get_gene_location(symbol: str):

    url = (
        f"{BASE_URL}/lookup/symbol/homo_sapiens/"
        f"{symbol}?content-type=application/json"
    )

    response = requests.get(url)

    return response.json()