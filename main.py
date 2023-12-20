import os
import argparse

def update_files(folder_path, extension, first_name, last_name):
    # Liste tous les fichiers du dossier avec l'extension spécifiée
    ''' 
    PRE: extension, first_name et last_name doivent etre des strings
    POST: insertion sous forme de commentaire de first_name et last_name au début de chaque fichier
          ayant l'extension donné avec 2 retour à la lignes. 
    '''
    files = [f for f in os.listdir(folder_path) if f.endswith(extension)]

        # Vérifie si des fichiers ont été trouvés
    if not files:
        print(f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier.")
        exit()

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Lit le contenu du fichier
        with open(file_path, 'r') as file:
            content = file.read()

        # Ajoute des commentaires spécifiques en fonction de l'extension
        if extension in ('js', 'c'):
            comment1 = '// '
            comment2 = ''
        elif extension in ('py', 'sh', 'bash'):
            comment1 = '# '
            comment2 = ''
        elif extension == 'html':
            comment1 = '<!-- '
            comment2 = ' -->'
        elif extension == 'css':
            comment1 = '/* '
            comment2 = ' */'
        elif extension in ('txt', 'doc', 'docx', 'pdf'):
            comment1 = ''
            comment2 = ''
        else:
            print('je ne connais pas encore cette extention')
            exit()

        # Ajoute le nom et le prénom à la première ligne avec un retour à la ligne
        updated_content = f"{comment1}{first_name} {last_name}{comment2}\n\n{content}"

        # Écrit le contenu mis à jour dans le fichier
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f"Mise à jour de {file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mettre à jour les fichiers dans un dossier avec un nom et un prénom.")
    parser.add_argument("folder_path", help="Chemin vers le dossier contenant les fichiers")
    parser.add_argument("extension", help="Extension des fichiers à mettre à jour")
    parser.add_argument("first_name", help="Votre prénom")
    parser.add_argument("last_name", help="Votre nom de famille")

    args = parser.parse_args()

    update_files(args.folder_path, args.extension, args.first_name, args.last_name)