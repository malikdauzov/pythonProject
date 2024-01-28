# Дан файл california_housing_train.csv.
# Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.
# import pandas as pd
# df = pd.read_csv('california_housing_train.csv')
# data_frame = ['population' < 500['median_house_value']]
# avg = data_frame
# print(avg)


import pandas as pd
df = pd.read_csv('california_housing_train.csv')
max_households_in_min_population = df [df['min_population'].min, ['households'].max]
print(max_households_in_min_population)
