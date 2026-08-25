import pandas as pd
from pathlib import Path

# ============================
# Fichiers
# ============================

input_file = Path(
    "10_pangenome/panaroo_results/gene_presence_absence.csv"
)

output_dir = Path("12_statistics")
output_dir.mkdir(exist_ok=True)

# ============================
# Lecture du fichier Panaroo
# ============================

df = pd.read_csv(input_file)

print("\n=== FICHIER PANAROO ===")
print("Nombre de familles de gènes :", len(df))
print("Nombre de colonnes :", len(df.columns))

print("\nColonnes détectées :")
for col in df.columns:
    print(" -", col)

# ============================
# Colonnes correspondant aux génomes
# ============================

genomes = [
    "KP1766",
    "KP1768",
    "NJST258_1",
    "NR5632",
    "SRR7345603"
]

# Vérification
missing = [g for g in genomes if g not in df.columns]

if missing:
    print("\nATTENTION : colonnes non trouvées :", missing)
    raise SystemExit

# ============================
# Conversion en présence/absence
# ============================

matrix = df[genomes].notna().astype(int)

matrix.insert(0, "Gene", df["Gene"])

# Nombre de génomes possédant chaque gène
matrix["Number_of_genomes"] = matrix[genomes].sum(axis=1)

# ============================
# Classification
# ============================

def classify(n):
    if n == 5:
        return "Core"
    elif n == 1:
        return "Unique"
    else:
        return "Accessory"

matrix["Category"] = matrix["Number_of_genomes"].apply(classify)

# ============================
# Sauvegarde
# ============================

output_file = output_dir / "pangenome_presence_absence.csv"

matrix.to_csv(output_file, index=False)

# ============================
# Résumé
# ============================

print("\n=== RÉSUMÉ DU PANGÉNOME ===")

print(matrix["Category"].value_counts())

print("\nNombre total de familles :", len(matrix))

print("\n=== GÈNES UNIQUES PAR SOUCHE ===")

for genome in genomes:

    unique = matrix[
        (matrix[genome] == 1) &
        (matrix["Number_of_genomes"] == 1)
    ]

    print(f"{genome}: {len(unique)}")

