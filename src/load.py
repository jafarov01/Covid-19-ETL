import pandas as pd
from sqlalchemy import create_engine

def load_data_to_sqlite(df, database_filename):
    """Load the DataFrame into a SQLite database."""
    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('covid_data', con=engine, if_exists='replace', index=False)

def main():
    # Load the transformed data
    transformed_data = pd.read_csv('transformed_covid_data.csv')
    
    # Load data into SQLite database
    load_data_to_sqlite(transformed_data, 'covid_data.db')

if __name__ == '__main__':
    main()