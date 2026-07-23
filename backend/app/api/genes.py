from fastapi import APIRouter

from app.clients.ncbi import get_gene_summary
from app.clients.ensembl import get_gene_location
from app.clients.uniprot import get_protein_data

router = APIRouter()


@router.get("/genes/{gene_id}")
def get_gene(gene_id: str):

    data = get_gene_summary(gene_id)

    gene = data["result"][gene_id]

    symbol = gene.get("name")

    # Ensembl data
    ensembl_data = get_gene_location(symbol)

    # UniProt data
    protein_data = get_protein_data(symbol)

    protein_results = protein_data.get("results", [])

    protein_name = None
    uniprot_id = None

    if protein_results:
        protein = protein_results[0]

        uniprot_id = protein.get("primaryAccession")

        protein_name = (
            protein
            .get("proteinDescription", {})
            .get("recommendedName", {})
            .get("fullName", {})
            .get("value")
        )

    return {
        "gene_id": gene_id,
        "symbol": symbol,
        "description": gene.get("description"),
        "chromosome": gene.get("chromosome"),

        "start": ensembl_data.get("start"),
        "end": ensembl_data.get("end"),
        "ensembl_id": ensembl_data.get("id"),

        "protein_name": protein_name,
        "uniprot_id": uniprot_id,

        "source": {
            "ncbi": f"https://www.ncbi.nlm.nih.gov/gene/{gene_id}",
            "ensembl": (
                f"https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={ensembl_data.get('id')}"
            ),
            "uniprot": (
                f"https://www.uniprot.org/uniprotkb/{uniprot_id}"
                if uniprot_id else None
            )
        }
    }