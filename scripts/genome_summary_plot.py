import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. Lecture des données
# ==============================

df = pd.read_csv("12_statistics/genome_summary.csv")

# Conversion bp -> Mb
df["Genome_size_Mb"] = df["bases"] / 1_000_000

# ==============================
# 2. Figure : taille des génomes
# ==============================

plt.figure(figsize=(9, 6))

bars = plt.bar(
    df["Sample"],
    df["Genome_size_Mb"]
)

plt.ylabel("Genome size (Mb)", fontsize=12)
plt.xlabel("Isolate", fontsize=12)

plt.title(
    "Genome size comparison of Klebsiella pneumoniae isolates",
    fontsize=14,
    fontweight="bold"
)

# Ajouter les valeurs sur les barres
for bar, value in zip(bars, df["Genome_size_Mb"]):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.03,
        f"{value:.2f}",
        ha="center",
        fontsize=11
    )

# Indiquer les ST sous les isolats
labels = [
    f"{sample}\nST{st}"
    for sample, st in zip(df["Sample"], df["ST"])
]

plt.xticks(
    range(len(df)),
    labels,
    fontsize=10
)

plt.ylim(0, max(df["Genome_size_Mb"]) * 1.15)

plt.tight_layout()

# ==============================
# 3. Sauvegarde
# ==============================

plt.savefig(
    "figures/genome_size_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figures/genome_size_comparison.pdf",
    bbox_inches="tight"
)

print("Figures créées :")
print("figures/genome_size_comparison.png")
print("figures/genome_size_comparison.pdf")
