# Define a function called calculate_souvenir_budget
# The function should take two parameters: countries (a list of countries) and souvenir_costs (a dictionary with countries as keys and costs as values)
def calculate_souvenir_budget(countries, souvenir_costs):

    # Inside the function, create a variable to hold the total budget and set it to 0
    total_budget = 0
    # Use a for loop to iterate through the list of countries
    for country in countries:
        # For each country, add the corresponding souvenir cost to the total budget
        total_budget += souvenir_costs[country]
    #The function should return the total budget
    return total_budget
# Assuming the countries you'll visit and the average souvenir costs
countries = ['France', 'Italy', 'Spain']
souvenir_costs = {'France': 150, 'Italy': 100, 'Spain': 75}

# Call the function
total_souvenir_budget = calculate_souvenir_budget(countries, souvenir_costs)
print(f"The total souvenir budget for the trip is: ${total_souvenir_budget}")