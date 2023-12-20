import subprocess

def modifier_fichier_sh(chemin_fichier_sh, nouveau_repertoire):
    # Lire le contenu du fichier sh
    with open(chemin_fichier_sh, 'r') as fichier:
        lignes = fichier.readlines()

    # Modifier la ligne 4 avec le nouveau répertoire
    if len(lignes) >= 4:
        lignes[3] = f'repertoire="{nouveau_repertoire}"\n'
    else:
        print("Le fichier sh ne contient pas assez de lignes.")

    # Écrire le contenu modifié dans le fichier sh
    with open(chemin_fichier_sh, 'w') as fichier:
        fichier.writelines(lignes)

if __name__ == "__main__":
    # Chemin vers le fichier sh
    chemin_fichier_sh = 'search.sh'  # Remplacez cela par le chemin réel de votre fichier sh

    # Demander à l'utilisateur de fournir le nouveau répertoire
    nouveau_repertoire = input("Veuillez entrer le nouveau chemin du répertoire : ")

    # Appeler la fonction pour effectuer la modification
    modifier_fichier_sh(chemin_fichier_sh, nouveau_repertoire)

    print(f"La modification du fichier {chemin_fichier_sh} a été effectuée avec succès.")

    # Exécuter le fichier sh à la fin
    commande = fr"{chemin_fichier_sh}"

    try:
        subprocess.run(commande, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"L'exécution de la commande a échoué avec le code de sortie {e.returncode}.")
