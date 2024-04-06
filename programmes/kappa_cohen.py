"""
@author AUGUSTYN Patricia

Pour lancer ce script, vous pouvez copier cette ligne de commande :
python3 kappa_cohen.py

"""

import pandas as pd
from sklearn.metrics import cohen_kappa_score
import matplotlib.pyplot as plt

data = pd.read_csv("../annotation/niveau1.csv")

# On prend les colonnes de chaque annotateur
lise = data["Lise"]
solomiia = data["Solomiia"]
patricia = data["Patricia"]

# On supprime les lignes qui n'ont aucune valeur
lise.dropna(inplace=True)
solomiia.dropna(inplace=True)
patricia.dropna(inplace=True)

# On calcul le Kappa de Cohen entre paire d'annotateurs
kappa_lise_solomiia = cohen_kappa_score(lise, solomiia)
kappa_lise_patricia = cohen_kappa_score(lise, patricia)
kappa_solomiia_patricia = cohen_kappa_score(solomiia, patricia)

# On va créer un graphique pour afficher notre résultat
resultats = pd.DataFrame({
    "Annotateurs": ["Lise - Solomiia", "Lise - Patricia", "Solomiia - Patricia"],
    "Kappa de Cohen": [kappa_lise_solomiia, kappa_lise_patricia, kappa_solomiia_patricia]
})

# On définit les couleurs pour chaque annotateur
colors = ["thistle", "peachpuff", "skyblue"]

# 1 couleur = 1 annotateur
plt.figure(figsize=(8, 6))
plt.bar(resultats["Annotateurs"], resultats["Kappa de Cohen"], color=colors)
plt.xlabel("Paires d'annotateurs")
plt.ylabel("Kappa de Cohen")
plt.title("Kappa de Cohen entre chaque paire d'annotateurs")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# On enregistre le graphique dans le dossier graphiques et on l'affiche
plt.savefig('../graphiques/kappa_cohen.png')

plt.show()
