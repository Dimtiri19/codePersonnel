import os
import subprocess
from colorama import Fore, Style, init
import shutil  # Ajout de l'importation pour la copie de sauvegarde

# Initialise colorama
init(autoreset=True)

def valider_chemin(chemin):
    if os.path.exists(chemin) and os.path.isdir(chemin):
        return True
    else:
        print("Le chemin spécifié n'est pas valide.")
        return False

def sauvegarder_fichier(chemin):
    try:
        shutil.copy(chemin, f"{chemin}.backup")  # Créer une copie de sauvegarde
        print(f"Une copie de sauvegarde a été créée : {chemin}.backup")
    except Exception as e:
        print(f"Erreur lors de la création de la copie de sauvegarde : {e}")

def modifier_fichier_sh(chemin_fichier_sh, nouveau_repertoire):
    # Sauvegarder le fichier avant de le modifier
    sauvegarder_fichier(chemin_fichier_sh)

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

    # Demander à l'utilisateur de fournir le nouveau répertoire avec une couleur
    nouveau_repertoire = input(Fore.BLUE + "Veuillez entrer le nouveau chemin du répertoire : " + Style.RESET_ALL)

    # Valider le chemin d'entrée
    if valider_chemin(nouveau_repertoire):
        # Modifier le fichier sh
        modifier_fichier_sh(chemin_fichier_sh, nouveau_repertoire)
        print(f"La modification du fichier {chemin_fichier_sh} a été effectuée avec succès.")

        # Exécuter le fichier sh à la fin
        commande = fr"{chemin_fichier_sh}"

        try:
            subprocess.run(commande, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"L'exécution de la commande a échoué avec le code de sortie {e.returncode}.")
            print(f"Sortie de la commande : {e.output.decode()}")
