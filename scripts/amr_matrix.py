import pandas as pd
import glob
import os

files = glob.glob("08_amr_virulence/*_amrfinder.tsv")

all_genes = {}

for file in files:

    sample = os.path.basename(file).replace("_amrfinder.tsv", "")

    df = pd.read_csv(file, sep="\t")

    gene_col = "Element symbol"

    if gene_col not in df.columns:
        print(f"ERREUR : colonne '{gene_col}' absente dans {file}")
        print("Colonnes disponibles :", list(df.columns))
        continue

    genes = (
        df[gene_col]
        .dropna()
        .astype(str)
        .str.strip()
    )

    genes = genes[genes != ""]

    all_genes[sample] = set(genes)

print("\n=== ISOLATS DÉTECTÉS ===")

for sample, genes in all_genes.items():
    print(f"{sample}: {len(genes)} déterminants")

genes_union = sorted(set().union(*all_genes.values()))

matrix = pd.DataFrame(
    {
        sample: [
            1 if gene in genes else 0
            for gene in genes_union
        ]
        for sample, genes in all_genes.items()
    },
    index=genes_union
)

matrix.index.name = "Gene"

order = [
    "KP1766",
    "KP1768",
    "NJST258_1",
    "NR5632",
    "SRR7345603"
]

matrix = matrix[
    [sample for sample in order if sample in matrix.columns]
]

matrix.to_csv(
    "12_statistics/amr_presence_absence.csv"
)

print("\n=== MATRICE AMR ===\n")
print(matrix.to_string())

print("\n=== NOMBRE DE DÉTERMINANTS PAR ISOLAT ===")
print(matrix.sum(axis=0))

print("\nFichier créé :")
print("12_statistics/amr_presence_absence.csv")