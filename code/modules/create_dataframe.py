import glob
import pandas as pd

from code.modules.my_simple_functions import get_subdirectories


def create_month_dataframe(my_path=None, index_status=False):
    """
    Crée le dataframe pour un mois donné.
    Cette fonction rassemble les différents fichiers csv des paramêtres TCP
    du mois stocké dans un dossier donné pour produire une dataset final pour le mois
    en question et enfin convertir ce datasets en dataFrame.
    :arg
        my_month_path : le chemin d'accès aux fichiers du mois.
        index_status : cette variable permet de supprimer l'index des datasets avant de les concatener
                  avec celui du mois pour former le dataset mensuel.
    :return: Le dataframe du mois.
    """

    datasets_files = glob.glob(my_path)
    # classement par ordre alphabetique des fichiers.
    datasets_files.sort()
    # création d'une liste pour stocker les DataFrames des fichiers dans le dossier
    df_list = []
    # itération sur la liste de fichiers csv dans le dossier
    for enum, file in enumerate(datasets_files):
        if "_up" not in file:
            df_temp = pd.read_csv(file)

            if enum != 0:
                df_temp = df_temp.drop("category", axis=1)
            df_list.append(df_temp)

    # Concaténer horizontalement les DataFrames du dossier actuel
    df_month = pd.concat(df_list, axis=1, ignore_index=index_status)

    return df_month


def create_year_dataframe(my_path, index_status=False):
    df_annee_list = []
    month_folders = get_subdirectories(my_path)
    for month_folder in month_folders:
        path = my_path + "/" + month_folder + "/*.csv"
        df_annee_list.append(create_month_dataframe(path, index_status))
    return df_annee_list


def create_full_dataframe(my_path, index_status=True):
    df_full = []
    year_folders = get_subdirectories(my_path)
    for year_folder in year_folders:
        path = my_path + '/' + year_folder
        month_folders = get_subdirectories(path)
        for month_folder in month_folders:
            new_path = path + '/' + month_folder + '/*.csv'
            df_full.append(create_month_dataframe(new_path, index_status))
    return df_full


# Les fonctions de formations des datasets de type upload

def create_month_dataframe_up(my_path=None, index_status=False):
    """
    Crée le dataframe pour un mois donné.
    Cette fonction rassemble les différents fichiers csv des paramêtres TCP
    du mois stocké dans un dossier donné pour produire une dataset final pour le mois
    en question et enfin convertir ce datasets en dataFrame.
    :arg
        my_month_path : le chemin d'accès aux fichiers du mois.
        index_status : cette variable permet de supprimer l'index des datasets avant de les concatener
                  avec celui du mois pour former le dataset mensuel.
    :return: Le dataframe du mois.
    """

    datasets_files = glob.glob(my_path)
    # classement par ordre alphabetique des fichiers.
    datasets_files.sort()
    # création d'une liste pour stocker les DataFrames des fichiers dans le dossier
    df_list = []
    # itération sur la liste de fichiers csv dans le dossier
    for enum, file in enumerate(datasets_files):
        if "_up" in file:

            df_temp = pd.read_csv(file)
            if enum != 0:
                df_temp = df_temp.drop("category", axis=1)
            df_temp.columns = [col + "_up" for col in df_temp.columns]
            df_list.append(df_temp)

    # Concaténer horizontalement les DataFrames du dossier actuel
    df_month = pd.concat(df_list, axis=1, ignore_index=index_status)

    return df_month


def create_year_dataframe_up(my_path, index_status=False):
    df_annee_list = []
    month_folders = get_subdirectories(my_path)
    for month_folder in month_folders:
        path = my_path + "/" + month_folder + "/*.csv"
        df_annee_list.append(create_month_dataframe_up(path, index_status))
    return df_annee_list


def create_full_dataframe_up(my_path, index_status=True):
    df_full = []
    year_folders = get_subdirectories(my_path)
    for year_folder in year_folders:
        path = my_path + '/' + year_folder
        month_folders = get_subdirectories(path)
        for month_folder in month_folders:
            new_path = path + '/' + month_folder + '/*.csv'
            df_full.append(create_month_dataframe_up(new_path, index_status))
    return df_full


# datasets des fichiers en conservant le format d'origine.

def create_month_dataframe_origin(my_path=None, index_status=False):
    """
    Crée le dataframe pour un mois donné.
    Cette fonction rassemble les différents fichiers csv des paramêtres TCP
    du mois stocké dans un dossier donné pour produire une dataset final pour le mois
    en question et enfin convertir ce datasets en dataFrame.
    :arg
        my_month_path : le chemin d'accès aux fichiers du mois.
        index_status : cette variable permet de supprimer l'index des datasets avant de les concatener
                  avec celui du mois pour former le dataset mensuel.
    :return: Le dataframe du mois.
    """

    datasets_files = glob.glob(my_path)
    # classement par ordre alphabetique des fichiers.
    datasets_files.sort()
    # création d'une liste pour stocker les DataFrames des fichiers dans le dossier
    df_list = []
    # itération sur la liste de fichiers csv dans le dossier
    for enum, file in enumerate(datasets_files):
        df_temp = pd.read_csv(file)
        if enum != 0:
            df_temp = df_temp.drop("category", axis=1)

        if "_up" in file:
            df_temp.columns = [col + "_up" for col in df_temp.columns]
        df_list.append(df_temp)

    # Concaténer horizontalement les DataFrames du dossier actuel
    df_month = pd.concat(df_list, axis=1, ignore_index=index_status)

    return df_month


def create_year_dataframe_origin(my_path, index_status=False):
    df_annee_list = []
    month_folders = get_subdirectories(my_path)
    for month_folder in month_folders:
        path = my_path + "/" + month_folder + "/*.csv"
        df_annee_list.append(create_month_dataframe_origin(path, index_status))
    return df_annee_list


def create_full_dataframe_origin(my_path, index_status=True):
    df_full = []
    year_folders = get_subdirectories(my_path)
    for year_folder in year_folders:
        path = my_path + '/' + year_folder
        month_folders = get_subdirectories(path)
        for month_folder in month_folders:
            new_path = path + '/' + month_folder + '/*.csv'
            df_full.append(create_month_dataframe_origin(new_path, index_status))
    return df_full
