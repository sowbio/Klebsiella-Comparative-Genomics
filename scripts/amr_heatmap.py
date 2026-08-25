import pandas as pd
import matplotlib.pyplot as plt

# Lire la matrice AMR
df = pd.read_csv(
    "12_statistics/amr_presence_absence.csv",
    index_col=0
)

# Figure
plt.figure(figsize=(10, 12))

plt.imshow(
    df.values,
    aspect="auto",
    interpolation="nearest"
)

# Axes
plt.xticks(
    range(len(df.columns)),
    df.columns,
    rotation=45,
    ha="right",
    fontsize=10
)

plt.yticks(
    range(len(df.index)),
    df.index,
    fontsize=8
)

plt.xlabel("Isolate")
plt.ylabel("AMR determinant")

plt.title(
    "AMR determinant presence/absence in Klebsiella pneumoniae isolates",
    fontsize=14
)

# Ajouter les valeurs 0/1
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        plt.text(
            j,
            i,
            str(df.iloc[i, j]),
            ha="center",
            va="center",
            fontsize=6
        )

plt.tight_layout()

plt.savefig(
    "figures/amr_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figures/amr_heatmap.pdf",
    bbox_inches="tight"
)

plt.close()

print("Heatmap créée :")
print("figures/amr_heatmap.png")
print("figures/amr_heatmap.pdf")