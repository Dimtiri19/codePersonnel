import unittest
import tempfile
import shutil
import os
from main import update_files

class TestUpdateFiles(unittest.TestCase):

    def setUp(self):
        # Crée un dossier temporaire pour les tests
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Supprime le dossier temporaire après les tests
        shutil.rmtree(self.test_dir)

    def test_update_files_js(self):
        # Crée un fichier JS temporaire
        file_content = "console.log('Hello, world!');"
        file_path = os.path.join(self.test_dir, "test_file.js")
        with open(file_path, "w") as file:
            file.write(file_content)

        # Exécute la fonction update_files
        update_files(self.test_dir, "js", "John", "Doe")

        # Vérifie que le fichier a été mis à jour correctement
        with open(file_path, "r") as updated_file:
            updated_content = updated_file.read()
            expected_content = "// John Doe\n\n" + file_content
            self.assertEqual(updated_content, expected_content)

    def test_update_files_html(self):
        # Crée un fichier HTML temporaire
        file_content = "<html><body>Hello, world!</body></html>"
        file_path = os.path.join(self.test_dir, "test_file.html")
        with open(file_path, "w") as file:
            file.write(file_content)

        # Exécute la fonction update_files
        update_files(self.test_dir, "html", "John", "Doe")

        # Vérifie que le fichier a été mis à jour correctement
        with open(file_path, "r") as updated_file:
            updated_content = updated_file.read()
            expected_content = "<!-- John Doe -->\n\n" + file_content
            self.assertEqual(updated_content, expected_content)

    def test_update_files_css(self):
        # Crée un fichier CSS temporaire
        file_content = "body { color: red; }"
        file_path = os.path.join(self.test_dir, "test_file.css")
        with open(file_path, "w") as file:
            file.write(file_content)

        # Exécute la fonction update_files
        update_files(self.test_dir, "css", "John", "Doe")

        # Vérifie que le fichier a été mis à jour correctement
        with open(file_path, "r") as updated_file:
            updated_content = updated_file.read()
            expected_content = "/* John Doe */\n\n" + file_content
            self.assertEqual(updated_content, expected_content)

    def test_update_files_sh(self):
        # Crée un fichier SH temporaire
        file_content = "#!/bin/bash\necho 'Hello, world!'"
        file_path = os.path.join(self.test_dir, "test_file.sh")
        with open(file_path, "w") as file:
            file.write(file_content)

        # Exécute la fonction update_files
        update_files(self.test_dir, "sh", "John", "Doe")

        # Vérifie que le fichier a été mis à jour correctement
        with open(file_path, "r") as updated_file:
            updated_content = updated_file.read()
            expected_content = "# John Doe\n\n" + file_content
            self.assertEqual(updated_content, expected_content)
    
    def test_update_files_txt(self):
        # Crée un fichier TXT temporaire
        file_content = "Hello, world!\nThis is a test file."
        file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(file_path, "w") as file:
            file.write(file_content)

        # Exécute la fonction update_files
        update_files(self.test_dir, "txt", "John", "Doe")

        # Vérifie que le fichier a été mis à jour correctement
        with open(file_path, "r") as updated_file:
            updated_content = updated_file.read()
            expected_content = "John Doe\n\n" + file_content
            self.assertEqual(updated_content, expected_content)

    def test_update_files_unknown_extension(self):
        # Crée un fichier avec une extension inconnue temporaire
        file_content = "Hello, world!"
        file_path = os.path.join(self.test_dir, "test_file.unknown")
        with open(file_path, "w") as file:
            file.write(file_content)

        # Exécute la fonction update_files avec une extension inconnue
        with self.assertRaises(ValueError) as context:
            update_files(self.test_dir, "unknown", "John", "Doe")

        # Vérifie que l'erreur a été correctement générée
        self.assertIn("Extension inconnue", str(context.exception))

if __name__ == "__main__":
    unittest.main()
