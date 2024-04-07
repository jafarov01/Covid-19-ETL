import pandas as pd

def load_data(file_path):
    """ Load data from a CSV file """
    return pd.read_csv(file_path)

def calculate_rates(df):
    """ Calculate mortality and recovery rates """
    df['mortality_rate'] = (df['deaths'] / df['total_cases']) * 100
    df['recovery_rate'] = (df['recoveries'] / df['total_cases']) * 100
    return df

def handle_outliers(df):
    df = df[df['new_cases'] >= 0]
    return df

def transform_data(file_path):
    df = load_data(file_path)
    df = calculate_rates(df)
    df = handle_outliers(df)
    return df

def main():
    input_file = "../data/raw/covid_data.csv"
    transformed_data = transform_data(input_file)
    print(transformed_data)
    transformed_data.to_csv("../data/processed/transformed_covid_data.csv", index=False)

if __name__ == "__main__":
    main()
