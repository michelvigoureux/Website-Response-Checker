import requests
import time
import csv

# Ouvrir le fichier urls.txt pour lire les URL
with open('urls.txt', 'r') as file:
    urls = file.readlines()

# Créer ou ouvrir un fichier CSV pour écrire les résultats
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['URL', 'Response Time (ms)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for url in urls:
        url = url.strip()  # Supprimer les espaces et les sauts de ligne
        
        try:
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()

            response_time = (end_time - start_time) * 1000
            writer.writerow({'URL': url, 'Response Time (ms)': round(response_time, 2)})
            
        except requests.RequestException:
            # Gestion d'erreur pour une URL invalide ou d'autres problèmes de réseau
            writer.writerow({'URL': url, 'Response Time (ms)': 'ERROR'})

print("Les résultats ont été enregistrés dans results.csv")
