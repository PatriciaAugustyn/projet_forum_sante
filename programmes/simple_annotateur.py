#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Solomiia Korol
"""

import csv

def get_etiquette(line):
    line_lower = line.lower()
    if any(word in line_lower for word in ["bonjour", "merci", "bon courage", "hello"]):
        return "fonction_phatique"
    elif any(word in line_lower for word in ["question", "peut-on", "pouvez-vous", "est-ce que quelqu'un pourrait", "pourriez-vous"]):
        return "recherche_information"
    elif any(word in line_lower for word in ["pendant", "depuis", "souffre", "je suis", "je me suis", "résultat", "conseil"]):
        return "partage_experience"
    else:
        return "non_spécifié"

def process_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for line in row:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Check if line is not empty
                    etiquette = get_etiquette(line)
                    print(f"Line: {line} | Etiquette: {etiquette}")

# Example usage:
filename = "projet_ann.csv"  # Replace with your CSV file path
process_csv(filename)
