# Extraction et traitement des publications citant l'ouvrage "Distant reading" de F. Moretti (2013) à partir de Google Scholar

## Trois scripts utilisés pour visualiser le nombre de publications citant l'ouvrage entre 2013 et 2024
(1) Extraction
(2) Concaténation et suppression des doublons
(3) Création de graphe temporel

## Remarques

La méthode utilisée pour identifier les publications citant explicitement l’ouvrage Distant Reading de Franco Moretti (2013) repose sur l’utilisation de la bibliothèque Python scholarly, qui permet d’interroger Google Scholar. Cependant, cette approche présente plusieurs limitations. Tout d’abord, bien que la requête textuelle permette de retrouver des publications mentionnant cet ouvrage dans des champs analysés par Google Scholar (tels que le titre, le résumé ou les métadonnées), elle ne garantit pas que ces résultats proviennent exclusivement de la fonctionnalité "Cité par", propre à l’interface web de Google Scholar. Par ailleurs, les publications citant l’ouvrage uniquement dans leur bibliographie, sans mention explicite dans les champs indexés, pourraient ne pas être incluses dans les résultats. De plus, la bibliothèque scholarly fonctionne via un mécanisme de scraping léger, soumis aux restrictions et variations de l’interface de Google Scholar, ce qui peut entraîner des résultats incomplets ou imprécis. Enfin, l’automatisation complète de la collecte des données directement depuis la fonctionnalité "Cité par" n’est actuellement pas possible en raison de l’absence d’une API officielle pour Google Scholar et des limitations légales liées à l’extraction automatisée de données. 
