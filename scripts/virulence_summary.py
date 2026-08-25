import pandas as pd
import os

# ==============================
# Fichier Kleborate
# ==============================

input_file = (
    "08_amr_virulence/"
    "SRR7345603_kleborate.tsv/"
    "Klebsiella_pneumo_complex_output.txt"
)

# Dossier de sortie
output_dir = "12_statistics"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(
    output_dir,
    "SRR7345603_virulence_summary.csv"
)

# ==============================
# Lecture du fichier
# ==============================

df = pd.read_csv(input_file, sep="\t")

# ==============================
# Colonnes importantes
# ==============================

columns = {
    "strain": "Isolate",

    "klebsiella_pneumo_complex__mlst__ST":
        "ST",

    "klebsiella__ybst__Yersiniabactin":
        "Yersiniabactin",

    "klebsiella__cbst__Colibactin":
        "Colibactin",

    "klebsiella__abst__Aerobactin":
        "Aerobactin",

    "klebsiella__smst__Salmochelin":
        "Salmochelin",

    "klebsiella__rmst__RmpADC":
        "RmpADC",

    "klebsiella__rmpa2__rmpA2":
        "rmpA2",

    "klebsiella_pneumo_complex__virulence_score__virulence_score":
        "Virulence_score"
}

# Sélection + renommage
result = df[list(columns.keys())].rename(columns=columns)

# Remplacer le nom "contigs" par le vrai nom de l'isolat
result["Isolate"] = "SRR7345603"

# ==============================
# Enregistrement
# ==============================

result.to_csv(output_file, index=False)

print("\n=== RÉSUMÉ DE VIRULENCE ===\n")
print(result.to_string(index=False))

print("\nFichier créé :")
print(output_file)