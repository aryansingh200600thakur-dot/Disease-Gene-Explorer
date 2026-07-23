from fastapi import APIRouter, HTTPException

from app.services.gene_service import (
    get_disease_genes
)

router = APIRouter()


@router.get("/diseases")
def search_disease(q: str):

    try:

        return get_disease_genes(q)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )