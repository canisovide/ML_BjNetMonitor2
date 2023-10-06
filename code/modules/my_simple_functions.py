import os


def get_subdirectories(my_path):
    # Utilisez la fonction os.listdir() pour obtenir la liste de tous les fichiers et dossiers dans le chemin donné.
    # Ensuite, utilisez une liste en compréhension pour filtrer seulement les dossiers.
    subdirectories = [d for d in os.listdir(my_path) if os.path.isdir(os.path.join(my_path, d))]
    return subdirectories
