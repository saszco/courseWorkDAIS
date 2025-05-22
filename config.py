from sqlalchemy import create_engine

db_params = {
    'dbname': 'cancer_analysis',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}")