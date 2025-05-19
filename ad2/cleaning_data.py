import pandas as pd

#filename = "../ad1/csv/population_2020.csv"

#df = pd.read_csv(filename)

# print(df.head(10))

# print(df.info())

# print(df.describe(include="all"))

#df.rename(columns={"2020": "Кількість"}, inplace=True)

#missing_data = df[df.isnull().any(axis=1)]

def print_data(df):
    for column in df.columns.values.tolist():
        print(df[column].value_counts())
        print("")

#print_data(missing_data)

#Пропущено два значення в "рядках про Крим та Севастополь"

#df = df.dropna()

#not_null_data = df.isnull();

#print_data(not_null_data)

#print(df.dtypes)

#negative_check = df.applymap(lambda x: str(x).strip().startswith("-") if pd.notna(x) else False)

#print(negative_check.any())

#Відʼємних даних немає

#df = df.astype({"Кількість": "int64"})

#print("\nТипи даних після зміни")
#print(df.dtypes)

#Додамо стовпець з інформацією про рік
#df["Рік"] = 2020

#print("\ndf після додавання нового стовпця")
#print(df)

#print(df["Рік"].dtypes)

#df.to_csv('cleaned_population_data_2020.csv', index=False)

#----------------------------------------------------------------------------

#filename = "../ad1/csv/population_2021.csv"

#df = pd.read_csv(filename)

#df.rename(columns={"2021": "Кількість"}, inplace=True)

#print(df.head())

#missing_data = df[df.isnull().any(axis=1)]

#print_data(missing_data)

#df = df.dropna()

#not_null_data = df.isnull();

#print_data(not_null_data)

#print(df.dtypes)

#df = df.astype({"Кількість": "int64"})

#print("\nТипи даних після зміни")
#print(df.dtypes)

#Додамо стовпець з інформацією про рік
#df["Рік"] = 2021

#print(df["Рік"].dtypes)

#df.to_csv('cleaned_population_data_2021.csv', index=False)

#----------------------------------------------------------------------------

# filename = "../ad1/csv/cancer_disease_and_death_2020.csv"

# df = pd.read_csv(filename, sep=";", decimal=',')

#print(df.head(10))

#print(df.info())

#print(df.columns)

# regions_to_remove = ["АР Крим", "м. Севастополь"]

# df = df[~df['Регіон'].isin(regions_to_remove)]

#missing_data = df[df.isna().any(axis=1)]

#print(missing_data)

def print_missed_columns(data):
    for index, row in data.iterrows():
        missing_columns = row.index[row.isna()].tolist()
        print(f"Регіон: {row['Регіон']}, Відсутні дані: {missing_columns}")

#print_missed_columns(missing_data)

#-----------------------

# donetsk_population_2020 = 4103159
# luhansk_population_2020 = 2124020

# donetsk_disease_cases = df[df["Регіон"].isin(['Донецька'])]['Кількість зареєстрованих випадків захворювання'].iloc[0]
# donetsk_death_cases = df[df["Регіон"].isin(['Донецька'])]['Кількість зареєстрованих смертей'].iloc[0]

# luhansk_disease_cases = df[df["Регіон"].isin(['Луганська'])]['Кількість зареєстрованих випадків захворювання'].iloc[0]
# luhansk_death_cases = df[df["Регіон"].isin(['Луганська'])]['Кількість зареєстрованих смертей'].iloc[0]

def count_rate(population, cases):
    return cases * 100000 / population

# donetsk_death_rate = count_rate(donetsk_population_2020, donetsk_death_cases).round(1)
# donetsk_disease_rate = count_rate(donetsk_population_2020, donetsk_disease_cases).round(1)

# luhansk_death_rate = count_rate(luhansk_population_2020, luhansk_death_cases).round(1)
# luhansk_disease_rate = count_rate(luhansk_population_2020, luhansk_disease_cases).round(1)

#print(donetsk_death_rate, donetsk_disease_rate)
#print(luhansk_death_rate, luhansk_disease_rate)

#--------------------------
# df.loc[df["Регіон"] == "Донецька", "Звичайний показник смертності на 100 тис. населення"] = donetsk_death_rate
# df.loc[df["Регіон"] == "Донецька", "Грубий показник захворюваності на 100 тис. населення"] = donetsk_disease_rate
# df.loc[df["Регіон"] == "Луганська", "Звичайний показник смертності на 100 тис. населення"] = luhansk_death_rate
# df.loc[df["Регіон"] == "Луганська", "Грубий показник захворюваності на 100 тис. населення"] = luhansk_disease_rate

#missing_data = df[df.isna().any(axis=1)]

#print_missed_columns(missing_data)

def count_all_cases(df, column):
    return df[column].sum()

# total_disease = count_all_cases(df, 'Кількість зареєстрованих випадків захворювання').astype(int)
# total_death = count_all_cases(df, 'Кількість зареєстрованих смертей').astype(int)

#print(total_disease, total_death)

# df.loc[df["Регіон"] == "Україна", "Кількість зареєстрованих випадків захворювання"] = total_disease
# df.loc[df["Регіон"] == "Україна", "Кількість зареєстрованих смертей"] = total_death

# missing_data = df[df.isna().any(axis=1)]

# print_missed_columns(missing_data)

# print(df.dtypes)

# df = df.astype({"Кількість зареєстрованих випадків захворювання": "int64",
#                "Кількість зареєстрованих смертей": "int64",
#                "Грубий показник захворюваності на 100 тис. населення": "float",
#                "Звичайний показник смертності на 100 тис. населення": "float"})

# print(df.dtypes)

# df["Рік"] = 2020

# df.to_csv('cleaned_cancer_disease_and_death_data_2020.csv', index=False)

#-----------------------------------------------

# filename = "../ad1/csv/cancer_disease_and_death_2021.csv"

# df = pd.read_csv(filename, sep=";", decimal=',')

# #print(df.head(10))

# #print(df.info())

# regions_to_remove = ["АР Крим", "м. Севастополь"]

# df = df[~df['Регіон'].isin(regions_to_remove)]

# missing_data = df[df.isna().any(axis=1)]

# print(missing_data)

# print_missed_columns(missing_data)

# selected_regions=["Дніпропетровська", "Запорізька", "Луганська", "Харківська"]

# donetsk_disease_cases = df[df["Регіон"].isin(selected_regions)]["Кількість зареєстрованих випадків захворювання"].mean().astype(int)

# donetsk_death_cases = df[df["Регіон"].isin(selected_regions)]["Кількість зареєстрованих смертей"].mean().astype(int)

# print(donetsk_death_cases, donetsk_disease_cases)

# df.loc[df["Регіон"] == "Донецька", "Кількість зареєстрованих випадків захворювання"] = donetsk_disease_cases
# df.loc[df["Регіон"] == "Донецька", "Кількість зареєстрованих смертей"] = donetsk_death_cases

# missing_data = df[df.isna().any(axis=1)]

# print_missed_columns(missing_data)

# total_disease = count_all_cases(df, 'Кількість зареєстрованих випадків захворювання').astype(int)
# total_death = count_all_cases(df, 'Кількість зареєстрованих смертей').astype(int)

# print(total_disease, total_death)

# df.loc[df["Регіон"] == "Україна", "Кількість зареєстрованих випадків захворювання"] = total_disease
# df.loc[df["Регіон"] == "Україна", "Кількість зареєстрованих смертей"] = total_death

# missing_data = df[df.isna().any(axis=1)]

# print_missed_columns(missing_data)

# donetsk_population_2021 = 4066941
# luhansk_population_2021 = 2107525

# donetsk_disease_cases = df[df["Регіон"].isin(['Донецька'])]['Кількість зареєстрованих випадків захворювання'].iloc[0]
# donetsk_death_cases = df[df["Регіон"].isin(['Донецька'])]['Кількість зареєстрованих смертей'].iloc[0]

# luhansk_disease_cases = df[df["Регіон"].isin(['Луганська'])]['Кількість зареєстрованих випадків захворювання'].iloc[0]
# luhansk_death_cases = df[df["Регіон"].isin(['Луганська'])]['Кількість зареєстрованих смертей'].iloc[0]

# donetsk_death_rate = count_rate(donetsk_population_2021, donetsk_death_cases).round(1)
# donetsk_disease_rate = count_rate(donetsk_population_2021, donetsk_disease_cases).round(1)

# luhansk_death_rate = count_rate(luhansk_population_2021, luhansk_death_cases).round(1)
# luhansk_disease_rate = count_rate(luhansk_population_2021, luhansk_disease_cases).round(1)

# print(donetsk_death_rate, donetsk_disease_rate)
# print(luhansk_death_rate, luhansk_disease_rate)

# df.loc[df["Регіон"] == "Донецька", "Звичайний показник смертності на 100 тис. населення"] = donetsk_death_rate
# df.loc[df["Регіон"] == "Донецька", "Грубий показник захворюваності на 100 тис. населення"] = donetsk_disease_rate
# df.loc[df["Регіон"] == "Луганська", "Звичайний показник смертності на 100 тис. населення"] = luhansk_death_rate
# df.loc[df["Регіон"] == "Луганська", "Грубий показник захворюваності на 100 тис. населення"] = luhansk_disease_rate

#missing_data = df[df.isna().any(axis=1)]

#print_missed_columns(missing_data)

#print(df.dtypes)

# df = df.astype({"Кількість зареєстрованих випадків захворювання": "int64",
#                "Кількість зареєстрованих смертей": "int64",
#                "Грубий показник захворюваності на 100 тис. населення": "float",
#                "Звичайний показник смертності на 100 тис. населення": "float"})

#print(df.dtypes)

#df["Рік"] = 2021

#df.to_csv('cleaned_cancer_disease_and_death_data_2021.csv', index=False)

#---------------------------------------------------
# filename = "../ad1/csv/pollution_data_2020.csv"

# df = pd.read_csv(filename)

# regions_to_remove = ["Автономна Республіка Крим", "Севастополь"]

# df = df[~df['Територіальний розріз'].isin(regions_to_remove)]

# df.rename(columns={"2020": "Кількість"}, inplace=True)

# missing_data = df[df.isna().any(axis=1)]

def pollution_print_missed_columns(data):
    for index, row in data.iterrows():
        missing_columns = row.index[row.isna()].tolist()
        print(f"Регіон: {row['Територіальний розріз']}, Відсутні дані: {missing_columns}")

# pollution_print_missed_columns(missing_data)

# print(df.dtypes)

# df.loc[df['Джерело забруднення'] == 'Стаціонарні джерела', 'Кількість'] = df.loc[df['Джерело забруднення'] == 'Стаціонарні джерела', 'Кількість'] * 1000

# print(df[['Територіальний розріз', 'Джерело забруднення', 'Кількість']])

# df["Рік"] = 2020

# df.to_csv('pollution_data_2020.csv', float_format='%.2f', index=False)

#-------------------

# filename = "../ad1/csv/pollution_data_2021.csv"

# df = pd.read_csv(filename)

# regions_to_remove = ["Автономна Республіка Крим", "Севастополь"]

# df = df[~df['Територіальний розріз'].isin(regions_to_remove)]

# df.rename(columns={"2021": "Кількість"}, inplace=True)

# missing_data = df[df.isna().any(axis=1)]

# pollution_print_missed_columns(missing_data)

# print(df.dtypes)

# df.loc[df['Джерело забруднення'] == 'Стаціонарні джерела', 'Кількість'] = df.loc[df['Джерело забруднення'] == 'Стаціонарні джерела', 'Кількість'] * 1000

# print(df[['Територіальний розріз', 'Джерело забруднення', 'Кількість']])

# df["Рік"] = 2021

# df.to_csv('pollution_data_2021.csv', float_format='%.2f', index=False)