from Bio import Phylo
import matplotlib.pyplot as plt

# Lire l'arbre IQ-TREE
tree = Phylo.read(
    "11_phylogeny/Klebsiella_core.treefile",
    "newick"
)

# Ajouter les ST dans les noms affichés
labels = {
    "KP1766": "KP1766  [ST307]",
    "KP1768": "KP1768  [ST307]",
    "NR5632": "NR5632  [ST307]",
    "SRR7345603": "SRR7345603  [ST307]",
    "NJST258_1": "NJST258_1  [ST258]"
}

for terminal in tree.get_terminals():
    if terminal.name in labels:
        terminal.name = labels[terminal.name]

# Figure
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)

# Dessin de l'arbre
Phylo.draw(
    tree,
    axes=ax,
    do_show=False,
    show_confidence=True,
    branch_labels=lambda c: (
        f"{int(c.confidence)}"
        if c.confidence is not None
        else None
    )
)

# Titre
ax.set_title(
    "Core-genome phylogeny of Klebsiella pneumoniae",
    fontsize=16,
    pad=20
)

# Axe X
ax.set_xlabel(
    "Genetic distance (substitutions per site)",
    fontsize=11
)

# On enlève l'axe Y inutile
ax.set_ylabel("")
ax.set_yticks([])

# Nettoyage des bordures
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Taille des textes
for text in ax.texts:
    text.set_fontsize(10)

# Annotation méthodologique
fig.text(
    0.5,
    0.03,
    "Maximum-likelihood phylogeny inferred from the Panaroo filtered core-genome alignment "
    "using IQ-TREE with 1000 ultrafast bootstrap replicates.",
    ha="center",
    fontsize=9
)

plt.tight_layout(rect=[0, 0.06, 1, 1])

# Sauvegarde PNG
plt.savefig(
    "figures/Klebsiella_core_tree_pretty.png",
    dpi=300,
    bbox_inches="tight"
)

# Sauvegarde PDF vectorielle
plt.savefig(
    "figures/Klebsiella_core_tree_pretty.pdf",
    bbox_inches="tight"
)

plt.close()

print("Figures créées :")
print("figures/Klebsiella_core_tree_pretty.png")
print("figures/Klebsiella_core_tree_pretty.pdf")from Bio import Phylo
import matplotlib.pyplot as plt

tree = Phylo.read(
    "11_phylogeny/Klebsiella_core.treefile",
    "newick"
)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

Phylo.draw(
    tree,
    axes=ax,
    do_show=False,
    show_confidence=True
)

plt.title("Core-genome phylogeny of Klebsiella pneumoniae")
plt.xlabel("Genetic distance (substitutions/site)")
plt.tight_layout()

plt.savefig(
    "figures/Klebsiella_core_tree.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Figure créée : figures/Klebsiella_core_tree.png")
