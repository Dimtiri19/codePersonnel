#!/bin/bash

# Définir le répertoire à parcourir
repertoire="c:/Users/dimit/OneDrive/Bureau"

# Tableau associatif pour stocker les extensions des fichiers sans la chaîne de caractères
declare -A extensions_sans_chaine

# Itérer sur tous les fichiers du répertoire
for fichier in "$repertoire"/*; do
    # Vérifier si l'élément est un fichier
    if [ -f "$fichier" ]; then
        # Utiliser grep pour rechercher la chaîne de caractères dans le fichier
        if ! grep -q "Dimitri Meeus" "$fichier"; then
            # La chaîne de caractères n'a pas été trouvée dans le fichier
            # Récupérer l'extension du fichier et l'ajouter au tableau associatif
            extension=$(echo "$fichier" | awk -F. '{print $NF}')
            extensions_sans_chaine["$extension"]=1
        fi
    fi
done

# Afficher les extensions des fichiers sans la chaîne de caractères
if [ ${#extensions_sans_chaine[@]} -eq 0 ]; then
    echo "La chaîne de caractères a été trouvée dans tous les fichiers du répertoire."
else
    echo "Les extensions des fichiers sans la chaîne de caractères sont : ${!extensions_sans_chaine[@]}"
fi

# Attendre une entrée de l'utilisateur avant de fermer la console
read -p "Appuyez sur Entrée pour quitter..."
