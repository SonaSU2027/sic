import my_part_hackathon_project_flights as fl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def menu():
    print("Select an analysis to perform:")
    print("1. Seasonal Pattern in Cargo Transportation")
    print("2. Months with Peak Passenger Traffic")
    print("3. Efficiency of Available Tonne-Kilometers")
    print("4. Exit")

def run_analysis(df):
    while True:
        menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        match choice:
            case '1':
                fl.seasonal_pattern_in_cargo(df)
            case '2':
                fl.peak_passenger_traffic(df)
            case '3':
                fl.efficiency_of_tonne_kilometers(df)
            case '4':
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again.")

df =pd.read_csv('DGCA_DATA.csv')
menu()
run_analysis(df)
