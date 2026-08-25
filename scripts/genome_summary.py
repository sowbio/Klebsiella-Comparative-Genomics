import pandas as pd
from pathlib import Path

samples = ["KP1766", "KP1768", "NJST258_1", "NR5632", "SRR7345603"]

st = {
    "KP1766": 307,
    "KP1768": 307,
    "NJST258_1": 258,
    "NR5632": 307,
    "SRR7345603": 307
}

rows = []

for sample in samples:
    file = Path(f"10_pangenome/annotations/{sample}/{sample}.txt")

    data = {
        "Sample": sample,
        "ST": st[sample]
    }

    with open(file) as f:
        for line in f:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                data[key.strip()] = value.strip()

    rows.append(data)

df = pd.DataFrame(rows)

wanted = [
    "Sample",
    "ST",
    "contigs",
    "bases",
    "CDS",
    "rRNA",
    "tRNA",
    "tmRNA"
]

df = df[wanted]

df.to_csv(
    "12_statistics/genome_summary.csv",
    index=False
)

print("\n=== COMPARAISON DES 5 GENOMES ===\n")
print(df.to_string(index=False))

print("\nFichier créé : 12_statistics/genome_summary.csv")
