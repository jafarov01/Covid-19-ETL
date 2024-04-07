import requests
import pandas as pd

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "new_cases": data["todayCases"],
            "total_cases": data["cases"],
            "deaths": data["deaths"],
            "recoveries": data["recovered"],
            "active_cases": data["active"]
        }
    else:
        print(f"Failed to fetch data: status code {response.status_code}")
        return {}

def main():
    covid_data = fetch_covid_data()
    df = pd.DataFrame([covid_data])
    print(df)
    df.to_csv("../data/raw/covid_data.csv", index=False)

if __name__ == "__main__":
    main()
