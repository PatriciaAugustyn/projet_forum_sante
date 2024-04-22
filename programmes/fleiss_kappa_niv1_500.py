#fleiss_kappa_niv1_500.py
import csv
from fleiss import fleissKappa

# Define the full path to the CSV file
csv_file_path = "/home/miya/OneDrive_solomia/Документи/Навчання/2 semestre/Enrichissement de corpus/annotation_sante_niv_1.csv"

# Initialize a list to store the transformed data
transformed_data = []

# Open the CSV file using the full path
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
        
    # Iterate over each row in the CSV file
    for row in reader:
        # Initialize counters for each category
        fonction_phatique_count = 0
        partage_experience_count = 0
        recherche_information_count = 0
        
        # Count the occurrences of each category in the current row
        for category in row:
            if category == 'fonction_phatique':
                fonction_phatique_count += 1
            elif category == 'partage_experience':
                partage_experience_count += 1
            elif category == 'recherche_information':
                recherche_information_count += 1
        
        # Append the counts to the transformed data list
        transformed_data.append([fonction_phatique_count, partage_experience_count, recherche_information_count])

# Call the fleissKappa function with the transformed data and the number of raters
result = fleissKappa(transformed_data, 3)
print(result)
