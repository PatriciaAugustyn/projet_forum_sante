import csv

# N'OUBLIEZ PAS INSERER LE CHEMIN CORRECT
csv_file = "/home/miya/OneDrive_solomia/Документи/Навчання/2 semestre/Enrichissement de corpus/projet_annotation_sante.csv"

# dictionnaire pour tranformer les catégories aux valeurs numériques
# on peut remplacer et ajouter beaucoup d'autres
category_mapping = {
    'partage_experience': 1,
    'recherche_information': 2,
    'fonction_phatique': 3
}

# voila la transformation
data = []
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # Ignorer les lignes vides 
        if not any(row):
            continue
        numeric_row = []
        for category in row:
            # Vérifier si la cellule est vide
            if category.strip():
                numeric_row.append(category_mapping.get(category, 0))
            else:  
                break
        else:
            data.append(numeric_row)

def fleiss_kappa(data):
    n = len(data)  # combien de lignes
    k = len(data[0])  # combien de categories
    N = n * k  # total

    p_i = [0] * k
    for annotations in data:
        for j, category in enumerate(annotations):
            p_i[j] += category

    for j in range(k):
        p_i[j] /= N

    P_i = [0] * n
    for i, annotations in enumerate(data):
        P_i[i] = sum([(annotations[j] / k) ** 2 for j in range(k)])

    # Calcule P_bar and P_e
    P_bar = sum(P_i) / n
    P_e = sum(p_i[j] ** 2 for j in range(k))

    # Calculate Fleiss' Kappa (la formule de Wikipedia, j'espere vivement que c'est bien)
    kappa = (P_bar - P_e) / (1 - P_e)
    return kappa

kappa = fleiss_kappa(data)
print("Fleiss' Kappa:", kappa) 
