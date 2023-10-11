"""
ML_BjNetMonitor

Ce projet est un projet de machine Learning qui vise à se baser sur les données de
la plateforme BjnetMonitor de l'entreprise EMES SARL pour faire des prédictions sur
les performances de l'internet dans un réseau WAN. Il permettra de faire des analyses
sur les performances du réseau.

Ce projet vise à aider les administrateurs réseau et les utilisateurs
à connaitre l'état de leurs réseaux et à proposer des solutions sur comment
optimiser leurs réseaux wan.


Auteur:
    Votre Nom <votre@email.com>
    Ronald SOVIDE ronald.sovide@gmail.com
    Didier ESSOU
Licence:


Usage:
    [Instructions pour exécuter ou utiliser le projet]

Modules:

Version : 1.1
"""
import numpy as np
import pandas as pd

bjnetmonitor_data = pd.read_csv("./inputs/BjNetMonitor.csv")
np.random.seed(0)
bjnetmonitor_data_cp = bjnetmonitor_data.copy()


bjnetmonitor_data_cp_1 = bjnetmonitor_data_cp.loc[(bjnetmonitor_data_cp["Minimum RTT"] != 0)
                                                  | (bjnetmonitor_data_cp['Maximum RTT'] != 0)]

new_column = pd.Series( pd.to_datetime(bjnetmonitor_data_cp_1['category'],
                                                       format="mixed", dayfirst=True),
                        name="Date_parsed"
                        )
bjnetmonitor_data_cp_2 = pd.concat([bjnetmonitor_data_cp_1, new_column], axis=1)
print(bjnetmonitor_data_cp_2['Date_parsed'].head())

print("Hello world")




