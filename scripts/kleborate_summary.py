import pandas as pd
import os

samples = [
    "KP1766",
    "KP1768",
    "NJST258_1",
    "NR5632",
    "SRR7345603"
]

rows = []

for sample in samples:

    if sample == "SRR7345603":
        file = (
            "08_amr_virulence/"
            "SRR7345603_kleborate.tsv/"
            "klebsiella_pneumo_complex_output.txt"
        )
    else:
        file = (
            f"08_amr_virulence/"
            f"{sample}_kleborate/"
            "enterobacterales__species_output.txt"
        )

    if not os.path.exists(file):
        print(f"Fichier absent pour {sample} : {file}")
        continue

    df = pd.read_csv(file, sep="\t")
    r = df.iloc[0]

    def get_value(column):
        if column in r.index:
            return r[column]
        return "-"

    row = {
        "Isolate": sample,

        "Species":
            get_value(
                "enterobacterales__species__species"
            ),

        "ST":
            get_value(
                "klebsiella_pneumo_complex__mlst__ST"
            ),

        "Yersiniabactin":
            get_value(
                "klebsiella__ybst__Yersiniabactin"
            ),

        "Colibactin":
            get_value(
                "klebsiella__cbst__Colibactin"
            ),

        "Aerobactin":
            get_value(
                "klebsiella__abst__Aerobactin"
            ),

        "Salmochelin":
            get_value(
                "klebsiella__smst__Salmochelin"
            ),

        "RmpADC":
            get_value(
                "klebsiella__rmst__RmpADC"
            ),

        "rmpA2":
            get_value(
                "klebsiella__rmpa2__rmpA2"
            ),

        "Virulence_score":
            get_value(
                "klebsiella_pneumo_complex__virulence_score__virulence_score"
            ),

        "Resistance_score":
            get_value(
                "klebsiella_pneumo_complex__resistance_score__resistance_score"
            ),

        "Resistance_gene_count":
            get_value(
                "klebsiella_pneumo_complex__resistance_gene_count__num_resistance_genes"
            ),

        "K_locus":
            get_value(
                "klebsiella_pneumo_complex__kaptive__K_locus"
            ),

        "K_type":
            get_value(
                "klebsiella_pneumo_complex__kaptive__K_type"
            ),

        "O_locus":
            get_value(
                "klebsiella_pneumo_complex__kaptive__O_locus"
            ),

        "O_type":
            get_value(
                "klebsiella_pneumo_complex__kaptive__O_type"
            ),
    }

    rows.append(row)

result = pd.DataFrame(rows)

output = "12_statistics/kleborate_summary.csv"

result.to_csv(output, index=False)

print("\n=== RÉSUMÉ KLEBORATE ===\n")
print(result.to_string(index=False))

print("\nFichier créé :")
print(output)