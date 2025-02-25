import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Analysis 6: Seasonal pattern in cargo transportation
def seasonal_pattern_in_cargo(df):
    if 'Month' in df.columns and 'Freight TON KM Performed' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Month', y='Freight TON KM Performed', data=df)
        plt.title('Seasonal Pattern in Cargo Transportation')
        plt.xlabel('Month')
        plt.ylabel('Freight TON KM Performed')
        plt.tight_layout()
        plt.show()
    else:
        print("Error: 'Month' or 'Freight TON KM Performed' column not found. Check Dataset.")

# Analysis 8: Months with Peak Passenger Traffic
def peak_passenger_traffic(df):
    if 'No Carried(P)' in df.columns and 'Month' in df.columns:
        peak_month = df.loc[df['No Carried(P)'].idxmax()]
        print(f"Month with Peak Passenger Traffic: {peak_month['Month']}")
    else:
        print("Error: 'No Carried(P)' or 'Month' column not found. Check dataset.")

# Analysis 9: Efficiency of Available Tonne-Kilometers
def efficiency_of_tonne_kilometers(df):
    if 'Avail TONNE KMS (Millions)' in df.columns and 'Total TON KMS Performed' in df.columns and 'Month' in df.columns:
        df['Efficiency'] = (df['Total TON KMS Performed'] / df['Avail TONNE KMS (Millions)']) * 100
        plt.figure(figsize=(10, 6))
        plt.plot(df['Month'], df['Efficiency'], marker='o')
        plt.title('Efficiency of Available Tonne-Kilometers')
        plt.xlabel('Month')
        plt.ylabel('Efficiency (%)')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Error: Either 'Avail TONNE KMS (Millions)', 'Total TON KMS Performed', or 'Month' column not found. Check dataset.")


df = pd.read_csv('sic\hackathon\DGCA_DATA.csv')
