import { useState } from "react";

function App() {
  const [disease, setDisease] = useState("");
  const [results, setResults] = useState<any>(null);
  const [selectedGene, setSelectedGene] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const searchDisease = async () => {
    try {
      setLoading(true);

      const response = await fetch(
        `http://127.0.0.1:8000/diseases?q=${encodeURIComponent(disease)}`
      );

      const data = await response.json();

      setResults(data);
      setSelectedGene(null);
    } catch (error) {
      console.error(error);
      alert("Search failed");
    } finally {
      setLoading(false);
    }
  };

  const loadGeneDetails = async (geneId: string) => {
    try {
      setLoading(true);

      const response = await fetch(
        `http://127.0.0.1:8000/genes/${geneId}`
      );

      const data = await response.json();

      setSelectedGene(data);
    } catch (error) {
      console.error(error);
      alert("Failed to load gene details");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "1100px",
        margin: "0 auto",
        padding: "30px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1
  style={{
    textAlign: "center",
    fontSize: "3rem",
    marginBottom: "10px"
  }}
>
  🧬 Disease Gene Explorer
</h1>

      <p style={{ textAlign: "center", color: "#666" }}>
        Explore disease-associated genes using NCBI,
        Ensembl and UniProt.
      </p>

      <div
        style={{
          display: "flex",
          gap: "10px",
          justifyContent: "center",
          marginTop: "20px",
        }}
      >
        <input
          type="text"
          placeholder="Enter disease name..."
          value={disease}
          onChange={(e) => setDisease(e.target.value)}
          style={{
            padding: "12px",
            width: "350px",
            borderRadius: "8px",
            border: "1px solid #ccc",
          }}
        />

        <button
          onClick={searchDisease}
          style={{
            padding: "12px 20px",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
          }}
        >
          Search
        </button>
      </div>

      {loading && (
        <h3 style={{ textAlign: "center", marginTop: "20px" }}>
          Loading...
        </h3>
      )}

      {results && (
        <>
          <h2 style={{ marginTop: "30px" }}>
            Genes Found ({results.genes?.length})
          </h2>

          <div
            style={{
              display: "grid",
              gridTemplateColumns:
                "repeat(auto-fit, minmax(300px, 1fr))",
              gap: "15px",
            }}
          >
            {results.genes?.map((gene: any) => (
              <div
                key={gene.gene_id}
                style={{
                  border: "1px solid #ddd",
                  borderRadius: "10px",
                  padding: "15px",
                  boxShadow:
                    "0 2px 8px rgba(0,0,0,0.1)",
                }}
              >
                <h3>{gene.symbol}</h3>

                <p>{gene.description}</p>

                <button
                  onClick={() =>
                    loadGeneDetails(gene.gene_id)
                  }
                >
                  View Details
                </button>
              </div>
            ))}
          </div>
        </>
      )}

      {selectedGene && (
        <div
          style={{
            marginTop: "40px",
            border: "2px solid #444",
            borderRadius: "10px",
            padding: "20px",
          }}
        >
          <h2>
            🧬 {selectedGene.symbol}
          </h2>

          <p>
            <strong>Description:</strong>{" "}
            {selectedGene.description}
          </p>

          <p>
            <strong>Chromosome:</strong>{" "}
            {selectedGene.chromosome}
          </p>

          <p>
            <strong>Coordinates:</strong>{" "}
            {selectedGene.start} - {selectedGene.end}
          </p>

          <p>
            <strong>Protein:</strong>{" "}
            {selectedGene.protein_name}
          </p>

          <p>
            <strong>Ensembl ID:</strong>{" "}
            {selectedGene.ensembl_id}
          </p>

          <p>
            <strong>UniProt ID:</strong>{" "}
            {selectedGene.uniprot_id}
          </p>

          <hr />

          <h3>External Resources</h3>

          <p>
            <a
              href={selectedGene.source.ncbi}
              target="_blank"
              rel="noreferrer"
            >
              NCBI Gene
            </a>
          </p>

          <p>
            <a
              href={selectedGene.source.ensembl}
              target="_blank"
              rel="noreferrer"
            >
              Ensembl
            </a>
          </p>

          <p>
            <a
              href={selectedGene.source.uniprot}
              target="_blank"
              rel="noreferrer"
            >
              UniProt
            </a>
          </p>
        </div>
      )}
    </div>
  );
}

export default App;