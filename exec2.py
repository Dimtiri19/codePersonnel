import subprocess

# Spécifie le chemin du dossier contenant le fichier search.sh
dossier_search = r"C:\Users\dimit\OneDrive\Bureau\projetDev\codePersonnel\search"

# Spécifie le chemin complet du fichier search.sh
chemin_search_sh = fr"{dossier_search}\search.sh"

# Ouvre le fichier search.sh et récupère le chemin initial
with open(chemin_search_sh, 'r') as file:
    contenu_initial = file.read()

# Demande à l'utilisateur de saisir un nouveau chemin
nouveau_repertoire = input("Veuillez saisir le nouveau chemin : ")

# Échappe les caractères spéciaux du chemin pour le formatage shell
nouveau_repertoire_escaped = nouveau_repertoire.replace("\\", "\\\\")

# Ouvre le fichier search.sh et remplace le chemin
with open(chemin_search_sh, 'r') as file:
    contenu = file.read()
    contenu_modifie = contenu.replace(f'repertoire="{contenu_initial}"', f'repertoire="{nouveau_repertoire_escaped}"')

# Écrit le fichier search.sh modifié
with open(chemin_search_sh, 'w') as file:
    file.write(contenu_modifie)

# Exécute le script avec le nouveau chemin
commande = fr"{chemin_search_sh}"

try:
    subprocess.run(commande, shell=True)
except subprocess.CalledProcessError as e:
    print(f"L'exécution de la commande a échoué avec le code de sortie {e.returncode}.")

# Restaure l'ancien chemin à la fin
with open(chemin_search_sh, 'w') as file:
    file.write(contenu_initial)

# Attend une entrée de l'utilisateur avant de se terminer
input("Appuyez sur Entrée pour quitter...")
