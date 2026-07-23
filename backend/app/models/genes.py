from pydantic import BaseModel


class Gene(BaseModel):
    gene_id: str
    symbol: str | None = None
    description: str | None = None
    chromosome: str | None = None
    source: str


class DiseaseResponse(BaseModel):
    disease: str
    genes: list[Gene]