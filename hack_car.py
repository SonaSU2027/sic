import pandas as pd
import datetime
import matplotlib.pyplot as plt

# --- Load Data (Replace with your actual file paths) ---
try:
    customers = pd.read_csv('customer_data.csv')
    services = pd.read_csv('service_data.csv')
    transactions = pd.read_csv('transaction_data.csv')
except FileNotFoundError as e:
    print(f"Error loading files.  Please make sure the files are in the correct location. Error: {e}")
    exit()

# --- Data Cleaning ---
transactions['date'] = pd.to_datetime(transactions['date'])

# --- Data Merging ---
merged_data = pd.merge(transactions, customers, on='customer_id')
merged_data = pd.merge(merged_data, services, on='service_id')

# --- a. Month for Discounts ---
merged_data['month'] = merged_data['date'].dt.month
monthly_sales = merged_data.groupby('month')['price'].sum()
min_sales_month = monthly_sales.idxmin()
print(f"Recommended month for discounts: {min_sales_month}")

# --- b. Month for Surcharge ---
max_sales_month = monthly_sales.idxmax()
print(f"Recommended month for surcharge: {max_sales_month}")

# --- c. Valuable Customers for Coupons ---
customer_spending = merged_data.groupby('customer_id')['price'].sum()
valuable_customer_threshold = customer_spending.quantile(0.9)
valuable_customers = customer_spending[customer_spending >= valuable_customer_threshold].index
two_months_ago = datetime.datetime.now() - pd.DateOffset(months=2)
last_transaction = merged_data.groupby('customer_id')['date'].max()
inactive_valuable_customers = last_transaction[(last_transaction < two_months_ago) & (last_transaction.index.isin(valuable_customers))]
coupon_customers = customers[customers['customer_id'].isin(inactive_valuable_customers.index)]
print("\nCustomers to send coupons to:")
print(coupon_customers[['customer_id', 'name', 'phone number']])

# --- d. Monthly Sales for a Year ---
year = int(input("Enter the year for monthly sales: "))
yearly_data = merged_data[merged_data['date'].dt.year == year]
monthly_sales = yearly_data.groupby(yearly_data['date'].dt.month)['price'].sum()
print(f"\nMonthly Sales for {year}:\n{monthly_sales}")
monthly_sales.plot(kind='bar', title=f'Monthly Sales for {year}')
plt.show()


# --- e. Sales by Time of Day ---
def get_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 24:
        return 'Evening'
    else:
        return 'Night'

merged_data['hour'] = merged_data['date'].dt.hour
merged_data['time_of_day'] = merged_data['hour'].apply(get_time_of_day)
sales_by_time = merged_data.groupby('time_of_day')['price'].sum()
sales_by_time.plot(kind='pie', title='Sales by Time of Day', autopct='%1.1f%%')
plt.show()