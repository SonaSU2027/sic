total_land = 80  
segments = 5  
segment_size = total_land / segments  
yields = {
    'tomatoes': [0.3 * 10, 0.7 * 12], 
    'potatoes': 10,
    'cabbage': 14,
    'sunflower': 0.7,
    'sugarcane': 45
}
prices = {
    'tomatoes': 7,
    'potatoes': 20,
    'cabbage': 24,
    'sunflower': 200,
    'sugarcane': 4000
}
sales_tomatoes = (yields['tomatoes'][0] + yields['tomatoes'][1]) * segment_size * prices['tomatoes'] * 1000  
sales_potatoes = yields['potatoes'] * segment_size * prices['potatoes'] * 1000  
sales_sunflower = yields['sunflower'] * segment_size * prices['sunflower'] * 1000  
sales_sugarcane = yields['sugarcane'] * segment_size * prices['sugarcane']

total_sales = sales_tomatoes + sales_potatoes + sales_cabbage + sales_sunflower + sales_sugarcane
print(f"Overall sales achieved by Mahesh: Rs. {total_sales}")
chemical_free_sales = sales_tomatoes + sales_potatoes + sales_cabbage + sales_sunflower
print(f"Sales realization from chemical-free farming at the end of 11 months: Rs. {chemical_free_sales}")
print('*' * 50)