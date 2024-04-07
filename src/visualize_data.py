import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_rates(df):
    sns.set_style("whitegrid")
    df[['mortality_rate', 'recovery_rate']].plot(kind='bar', figsize=(10, 6))
    plt.title('COVID-19 Mortality and Recovery Rates')
    plt.ylabel('Rates (%)')
    plt.xlabel('Data Points')
    plt.xticks([])
    plt.legend(loc='upper right')
    plt.show()

def main():
    df = load_data('../data/processed/transformed_covid_data.csv')
    plot_rates(df)

if __name__ == "__main__":
    main()
