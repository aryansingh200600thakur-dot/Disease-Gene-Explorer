from app.clients.ensembl import get_gene_location

from fastapi import APIRouter

from app.clients.ncbi import get_gene_summary
from app.clients.ensembl import get_gene_location

router = APIRouter()


@router.get("/genes/{gene_id}")
def get_gene(gene_id: str):

    data = get_gene_summary(gene_id)

    gene = data["result"][gene_id]

    symbol = gene.get("name")

    ensembl_data = get_gene_location(symbol)

    return {
        "gene_id": gene_id,
        "symbol": symbol,
        "description": gene.get("description"),
        "chromosome": gene.get("chromosome"),

        "start": ensembl_data.get("start"),
        "end": ensembl_data.get("end"),
        "ensembl_id": ensembl_data.get("id"),

        "source": {
            "ncbi": f"https://www.ncbi.nlm.nih.gov/gene/{gene_id}",
            "ensembl": (
                "https://www.ensembl.org/"
                f"Homo_sapiens/Gene/Summary?g={ensembl_data.get('id')}"
            )
        }
    }