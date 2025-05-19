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

def load_dim_region_data():
    query = "SELECT DISTINCT region_name FROM stage.population WHERE region_name IS NOT NULL"
    df_regions = pd.read_sql(query, engine)
    
    query_existing = "SELECT region_name FROM main.dim_region_data"
    df_existing = pd.read_sql(query_existing, engine)
    
    df_new = df_regions.merge(df_existing, on='region_name', how='left', indicator=True)
    df_new = df_new[df_new['_merge'] == 'left_only'][['region_name']]
    
    if not df_new.empty:
        df_new.to_sql('dim_region_data', schema='main', con=engine, if_exists='append', index=False)
        print(f"Додано {len(df_new)} нових регіонів до main.dim_region_data.")
    else:
        print("Нових регіонів для додавання немає.")

load_dim_region_data()

def load_dim_pollution():
    query = """
        SELECT DISTINCT source_of_pollution AS source_name,
                        source_category_name AS category_name,
                        pollutant_type_name
        FROM stage.pollution_data
        WHERE source_of_pollution IS NOT NULL
        AND source_category_name IS NOT NULL 
        AND pollutant_type_name IS NOT NULL
    """

    df_pollution = pd.read_sql(query, engine)

    query_existing = "SELECT source_name, category_name, pollutant_type_name FROM main.dim_pollution"
    df_existing = pd.read_sql(query_existing, engine)

    df_new = df_pollution.merge(df_existing, on=['source_name', 'category_name', 'pollutant_type_name'], how='left', indicator=True)
    df_new = df_new[df_new['_merge'] == 'left_only'][['source_name', 'category_name', 'pollutant_type_name']]
    
    if not df_new.empty:
        df_new.to_sql('dim_pollution', schema='main', con=engine, if_exists='append', index=False)
        print(f"Додано {len(df_new)} нових даних про забруднення до main.dim_pollution.")
    else:
        print("Нових даних про забруднення для додавання немає.")

load_dim_pollution()

def load_dim_year():
    query = """
        SELECT DISTINCT year FROM stage.population
        UNION
        SELECT DISTINCT year FROM stage.pollution_data
        UNION
        SELECT DISTINCT year FROM stage.cancer_disease_and_death
    """
    df_years = pd.read_sql(query, engine)
    
    query_existing = "SELECT year FROM main.dim_year"
    df_existing = pd.read_sql(query_existing, engine)
    
    df_new = df_years.merge(df_existing, on='year', how='left', indicator=True)
    df_new = df_new[df_new['_merge'] == 'left_only'][['year']]
    
    if not df_new.empty:
        df_new.to_sql('dim_year', schema='main', con=engine, if_exists='append', index=False)
        print(f"Додано {len(df_new)} нових років до main.dim_year.")
    else:
        print("Нових років для додавання немає.")

load_dim_year()

def load_cancer_analysis():
    query_cancer = """
    SELECT region_name, year, 
           SUM(death_case_count) AS death_case_count, 
           SUM(disease_case_count) AS disease_case_count,
           AVG(incidence_rate) AS crude_disease_rate, 
           AVG(death_rate) AS crude_death_rate
    FROM stage.cancer_disease_and_death
    WHERE disease_case_count IS NOT NULL AND death_case_count IS NOT NULL
    GROUP BY region_name, year
    """
    df_cancer = pd.read_sql(query_cancer, engine)
    print("Дані про рак:", df_cancer)

    query_pollution = """
    SELECT region_name, year, pollution_count, source_of_pollution, 
           source_category_name, pollutant_type_name
    FROM stage.pollution_data
    WHERE pollution_count IS NOT NULL
    """
    df_pollution = pd.read_sql(query_pollution, engine)
    print("Дані про забруднення:", df_pollution[['region_name', 'year']].drop_duplicates())
    
    query_population = """
    SELECT region_name, year, population_count
    FROM stage.population
    WHERE population_count IS NOT NULL
    """
    df_population = pd.read_sql(query_population, engine)
    print("Дані про населення:", df_population[['region_name', 'year']].drop_duplicates())
    
    df_regions = pd.read_sql("SELECT region_id, region_name FROM main.dim_region_data", engine)
    df_years = pd.read_sql("SELECT year_id, year FROM main.dim_year", engine)
    df_pollution_dim = pd.read_sql("SELECT pollution_id, source_name, category_name, pollutant_type_name FROM main.dim_pollution", engine)
    
    df_merged = df_cancer.merge(df_pollution, on=['region_name', 'year'], how='inner')
    df_merged = df_merged.merge(df_population, on=['region_name', 'year'], how='inner')
    df_merged = df_merged.merge(df_regions, on='region_name', how='inner')
    df_merged = df_merged.merge(df_years, on='year', how='inner')
    df_merged = df_merged.merge(df_pollution_dim, 
                               left_on=['source_of_pollution', 'source_category_name', 'pollutant_type_name'],
                               right_on=['source_name', 'category_name', 'pollutant_type_name'], 
                               how='inner')

    df_final = pd.DataFrame({
        'region_info': df_merged['region_id'],
        'population_count': df_merged['population_count'].astype(int),
        'year_info': df_merged['year_id'],
        'death_cases_count': df_merged['death_case_count'].astype(int),
        'disease_cases_count': df_merged['disease_case_count'].astype(int),
        'crude_death_rate': df_merged['crude_death_rate'].round(2),
        'crude_disease_rate': df_merged['crude_disease_rate'].round(2),
        'pollution_info': df_merged['pollution_id'],
        'pollution_count': df_merged['pollution_count'].round(2)
    })
    
    query_existing = """
    SELECT region_info, year_info, pollution_info
    FROM main.cancer_analysis
    """
    df_existing = pd.read_sql(query_existing, engine)
    
    df_final['key'] = df_final['region_info'].astype(str) + '|' + df_final['year_info'].astype(str) + '|' + df_final['pollution_info'].astype(str)
    df_existing['key'] = df_existing['region_info'].astype(str) + '|' + df_existing['year_info'].astype(str) + '|' + df_existing['pollution_info'].astype(str)
    
    df_new = df_final.merge(df_existing[['key']], on='key', how='left', indicator=True)
    df_new = df_new[df_new['_merge'] == 'left_only'].drop(columns=['key', '_merge'])
    
    if not df_new.empty:
        df_new.to_sql('cancer_analysis', schema='main', con=engine, if_exists='append', index=False)
        print(f"Додано {len(df_new)} нових записів до main.cancer_analysis.")
    else:
        print("Нових записів для додавання немає.")

load_cancer_analysis()