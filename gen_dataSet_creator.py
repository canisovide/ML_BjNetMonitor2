"""
Création de DataFrames à partir de datasets

Ce fichier contient des fonctions pour créer des DataFrames à partir de datasets.

Auteur:
    Votre Nom <votre@email.com>

Licence:
    [Type de licence, par exemple : MIT]

Fonctions:
    - create_dataframe_from_csv(dataset_path)
    - create_dataframe_from_excel(dataset_path)
    - ...

Exemple:
    df = create_dataframe_from_csv('chemin/vers/mon_dataset.csv')
"""
import pandas as pd

from code.modules.create_dataframe import create_full_dataframe_origin

# Les listes des colonnes des données tirées sur les tests de types down et up
# columns_list_down = []
# columns_list_up = []

columns_list = []
with open("./documentations/dataFrame_columns.txt", 'r') as fillin:
    for col in fillin:
        columns_list.append(col.strip())

        # Stratégie utiliser pour former les listes des colonnes des données de types down et up
        # if "_up" in col:
        #     columns_list_up.append(col.strip())
        # else:
        #     columns_list_down.append(col.strip())

keys = list(range(269))
my_columns_dict = dict(zip(keys, columns_list))

# Dataframe formation
path = "./datasets"
list_dataF = create_full_dataframe_origin(path, index_status=True)
dataF = pd.concat(list_dataF, axis=0, ignore_index=True)
dataF.rename(columns=my_columns_dict, inplace=True)
dataF.to_csv("./inputs/BjNetMonitor.csv")
