import pandas as pd
from sqlalchemy import create_engine
import logging
import psycopg2

logging.basicConfig(
    filename='etl_process.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

db_params = {
    'dbname': 'cancer_analysis',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}")
