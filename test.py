import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from code.modules.create_dataframe import create_month_dataframe

december_2021 = create_month_dataframe(my_path="./datasets/2021/decembre/*.csv")
december_2021_data = december_2021.copy()
december_2021_data = december_2021_data.loc[(december_2021_data["Minimum RTT"] != 0)
                                            | (december_2021_data["Maximum RTT"] != 0)]
new_column = pd.Series(pd.to_datetime(december_2021_data['category'],
                                      format="mixed", dayfirst=True),
                       name="Date_parsed"
                       )
december_2021_data = pd.concat([december_2021_data, new_column], axis=1)
december_2021_data.set_index("Date_parsed")
december_2021_data.drop("category", axis=1)

d = {'col1': [1, 2, 1.2, 23, 4, 2], 'col2': [3, 4, 34, 2, 0, 3.14]}
dataF = pd.DataFrame(data=d)


# Remplacer is_categorical_dtype par isinstance(dtype, CategoricalDtype)


plt.figure(figsize=(14, 6))
plt.title("Test")
sns.lineplot(data=dataF, x='col1', y='col2',)  # Passer is_categorical à l'argument hue
plt.show()
