# Define a list named chosen_countries with countries selected for the road trip

chosen_countries = [
    "Canada",
    "USA",
    "Mexico",
    "France",
    "Spain"
]
# Define a dictionary named country_fuel_costs with fuel costs for countries

country_fuel_costs = {
    "Canada": 1.50,
    "USA": 1.30,
    "Mexico": 1.25,
    "France": 3.00,
    "Spain": 3.25
}

# Initialize a variable total_fuel_cost to 0

total_fuel_cost = 0

# Use a for loop to add up the fuel cost for each chosen country

for country, fuel_cost in country_fuel_costs.items():
    if country in chosen_countries:
        total_fuel_cost += fuel_cost

# Calculate the average fuel cost per country

average_fuel_cost = total_fuel_cost / len(chosen_countries)

# Print the total fuel cost for the road trip

print(total_fuel_cost)

# Print the average fuel cost per country

print(average_fuel_cost)
