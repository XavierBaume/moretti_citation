#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
file_path = 'year_compiled.csv'
data = pd.read_csv(file_path)

# Nettoyer et préparer les données
# Vérifier les valeurs manquantes dans la colonne "Année de publication"
data = data.dropna(subset=['Année de publication'])

# Convertir la colonne "Année de publication" en entier
data['Année de publication'] = data['Année de publication'].astype(int)

# Compter les publications par année
publications_per_year = data['Année de publication'].value_counts().sort_index()

# Tracer le graphique
plt.figure(figsize=(10, 6))
plt.plot(publications_per_year.index, publications_per_year.values, marker='o')
plt.title("Évolution du nombre de publications par année", fontsize=16, fontweight='bold', loc='center')
plt.xlabel("Année")
plt.ylabel("Nombre de publications")
plt.ylim(0, 500)
plt.grid(True)
plt.show()


# In[ ]:




