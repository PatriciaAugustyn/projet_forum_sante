"""
@author AUGUSTYN Patricia

Ce script montre la distribution des étiquettes annotées par nous :
- chaque barre représente une annotation
- la hauteur de la barre représente le nombre de phrases annotées avec cette annotation
- la graphique est triés du plus fréquent au moins fréquent


Pour lancer ce script, vous devez seulement copier cette ligne de commande :
    - python3 graphique.py
    
Pensez à installer les librairies (dans un environnement virtuel)
avec les commandes : 
    - pip install numpy
    - pip install pandas
    - pip install matplotlib

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# On va lire nos 3 fichiers avec nos 3 annotations
file_paths = ["../datas/1000_annotation_finale.csv"]
annotations = []

# On parcourt chaque fichier CSV --> liste de dataframes dans notre liste avec chacune de nos annotations
for file_path in file_paths:
    annotations.append(pd.read_csv(file_path)) #On lit le contenu de chaque fichier CSV en tant que DataFrame

annotate = []  # On stocke les annotations dans un format acceptable pour NLTK
for annotator_index, annotator_df in enumerate(annotations):
    annotator = []  # On sstocke les annotations d'un annotateur
    for index, row in annotator_df.iterrows():

        # On va joindre les niveaux en une seule chaîne séparée par une pipe
        annotation = "|".join([str(row['niveau1']), str(row['niveau2']),
                               str(row['niveau3_1']), str(row['niveau3_2'])]) # Le nom de nos colonnes

        # On ajoute les informations de l'annotateur, de la phrase et de l'annotation à la liste
        annotator.append((annotator_index, row['ID'], annotation))

    annotate.extend(annotator)  # O n étend la liste  avec les annotations de cet annotateur

# Distribution des annotations
annotations_count = {}  # Initialise un dictionnaire pour compter les occurrences de chaque annotation
for annotator_index, sentence, annotation in annotate:

    if annotation not in annotations_count:
        # On initialise le compteur à zéro pour une nouvelle annotation
        # Exemple : nan|nan|nan|nan --> liens, ponctuations etc...
        annotations_count[annotation] = 0

    annotations_count[annotation] += 1  # Incrémente le compteur pour cette annotation

# Trier les annotations par fréquence
sorted_annotations_count = dict(sorted(annotations_count.items(), key=lambda item: item[1], reverse=True))

# Création du graphique
plt.figure(figsize=(14, 8))
bar_colors = plt.cm.viridis(np.linspace(0, 1, len(sorted_annotations_count)))  # Collection de couleur selon la fréquence
bar_positions = np.arange(len(sorted_annotations_count))  # Positionnement des barres
plt.bar(bar_positions, list(sorted_annotations_count.values()), align='center', color=bar_colors)
plt.xticks(bar_positions, list(sorted_annotations_count.keys()), rotation=45, ha='right')  # Alignement à droite
plt.xlabel("Etiquettes")
plt.ylabel("Nombre de phrases annotées")
plt.title("Distribution des étiquettes")

plt.tight_layout()

# On enregistre l'image dans notre dossier graphiques
plt.savefig("../graphiques/distribution_etiquette_finale.png")

plt.show()

