import pandas as pd
from sqlalchemy import create_engine
import psycopg2

db_params = {
    'dbname': 'cancer_analysis',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}")

#=====Loading population data=====

# filename_population2020 = "../ad2/cleaned_population_data_2020.csv"

# df1 = pd.read_csv(filename_population2020)

# df1.rename(columns={
#     "Показник": "indicator",
#     "Територіальний розріз": "region_name",
#     "Періодичність": "periodicity",
#     "Кількість": "population_count",
#     "Рік": "year"
# }, inplace=True)

# df1.to_sql('population', schema='stage', con=engine, if_exists='append', index=False)
# print("Population data saved into schema")

# filename_population2021 = "../ad2/cleaned_population_data_2021.csv"

# df2 = pd.read_csv(filename_population2021)

# df2.rename(columns={
#     "Показник": "indicator",
#     "Територіальний розріз": "region_name",
#     "Періодичність": "periodicity",
#     "Кількість": "population_count",
#     "Рік": "year"
#  }, inplace=True)

# df2.to_sql('population', schema='stage', con=engine, if_exists='append', index=False)
# print("Population data saved into schema")


#=====Loading pollution data=====
# filename_pollution2020 = "../ad2/cleaned_pollution_data_2020.csv"

# df3 = pd.read_csv(filename_pollution2020)

# df3.rename(columns={
#       "Показник": "indicator",
#       "Територіальний розріз": "region_name",
#       "Джерело забруднення": "source_of_pollution",
#       "Вид забруднюючої речовини": "pollutant_type_name",
#       "Категорія джерела забруднення": "source_category_name",
#       "Періодичність": "periodicity",
#       "Кількість": "pollution_count",
#       "Рік": "year"
#   }, inplace=True)

# df3.to_sql('pollution_data', schema='stage', con=engine, if_exists='append', index=False)
# print("Pollution data saved into schema")


# filename_pollution2021 = "../ad2/cleaned_pollution_data_2021.csv"

# df4 = pd.read_csv(filename_pollution2021)

# df4.rename(columns={
#       "Показник": "indicator",
#       "Територіальний розріз": "region_name",
#       "Джерело забруднення": "source_of_pollution",
#       "Вид забруднюючої речовини": "pollutant_type_name",
#       "Категорія джерела забруднення": "source_category_name",
#       "Періодичність": "periodicity",
#       "Кількість": "pollution_count",
#       "Рік": "year"
#   }, inplace=True)

# df4.to_sql('pollution_data', schema='stage', con=engine, if_exists='append', index=False)
# print("Pollution data saved into schema")

#=====Loading cancer data=====
# filename_cancer2020 = "../ad2/cleaned_cancer_disease_and_death_data_2020.csv"

# df5 = pd.read_csv(filename_cancer2020)

# df5.rename(columns={
#     "Регіон": "region_name",
#     "Кількість зареєстрованих випадків захворювання": "disease_case_count",
#     "Грубий показник захворюваності на 100 тис. населення": "incidence_rate",
#     "Кількість зареєстрованих смертей": "death_case_count",
#     "Звичайний показник смертності на 100 тис. населення": "death_rate",
#     "Рік": "year"
# }, inplace=True)

# df5.to_sql('cancer_disease_and_death', schema='stage', con=engine, if_exists='append', index=False)
# print("Cancer data uploaded")

# filename_cancer2021 = "../ad2/cleaned_cancer_disease_and_death_data_2021.csv"

# df6 = pd.read_csv(filename_cancer2021)

# df6.rename(columns={
#     "Регіон": "region_name",
#     "Кількість зареєстрованих випадків захворювання": "disease_case_count",
#     "Грубий показник захворюваності на 100 тис. населення": "incidence_rate",
#     "Кількість зареєстрованих смертей": "death_case_count",
#     "Звичайний показник смертності на 100 тис. населення": "death_rate",
#     "Рік": "year"
# }, inplace=True)

# df6.to_sql('cancer_disease_and_death', schema='stage', con=engine, if_exists='append', index=False)
# print("Cancer data uploaded")