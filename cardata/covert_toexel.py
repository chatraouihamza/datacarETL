import pandas as pd

# Charger le fichier CSV en tant que DataFrame
df = pd.read_csv("link_price.csv")

# Enregistrer le DataFrame dans un fichier Excel
df.to_excel("link_pricesexel.xlsx", index=False)

print("Conversion du fichier CSV en fichier Excel terminée.")
