#fleiss_kappa_niv2_500.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Solomiia Korol
"""

import csv
from fleiss import fleissKappa

# Define the full path to the CSV file
csv_file_path = "/home/miya/OneDrive_solomia/Документи/Навчання/2 semestre/Enrichissement de corpus/annotation_sante_niv2_1000.csv"

# Initialize a list to store the transformed data
transformed_data = []

# Open the CSV file using the full path
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
        
    # Iterate over each row in the CSV file
    for row in reader:
        # Initialize counters for each category
        symptome_count = 0
        traitement_count = 0
        diagnostique_count = 0
        
        # Count the occurrences of each category in the current row
        for category in row:
            if category == 'symptome':
                symptome_count += 1
            elif category == 'traitement':
                traitement_count += 1
            elif category == 'diagnostique':
                diagnostique_count += 1
        
        # Append the counts to the transformed data list
        transformed_data.append([symptome_count, traitement_count, diagnostique_count])

# Call the fleissKappa function with the transformed data and the number of raters
result = fleissKappa(transformed_data, 3)
#print(transformed_data)
print(result)