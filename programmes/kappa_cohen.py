"""
@author AUGUSTYN Patricia

Pour lancer ce script, vous pouvez copier cette ligne de commande :
    - python3 kappa_cohen.py

Pensez à installer les librairies (dans un environnement virtuel)
avec les commandes : 
    - pip install -U scikit-learn
    - pip install pandas
    - pip install matplotlib

"""

import pandas as pd
from sklearn.metrics import cohen_kappa_score
import matplotlib.pyplot as plt

data = pd.read_csv("../datas/niveau3_2.csv")

# On supprime les lignes qui n'ont aucune valeur
data.dropna(inplace=True)

# On prend les colonnes de chaque annotateur
lise = data["Lise"]
solomiia = data["Solomiia"]
patricia = data["Patricia"]


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
plt.title("Kappa de Cohen entre chaque paire d'annotateurs : Niveau 3_2")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# On enregistre le graphique dans le dossier graphiques et on l'affiche
plt.savefig('../graphiques/kappa_cohen_niv3_2.png')

plt.show()
