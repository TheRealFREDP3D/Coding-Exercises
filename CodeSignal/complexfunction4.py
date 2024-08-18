# Adjusted function to consider both budget and cost preference.
def choose_countries(budget, cost_threshold, costs):
    total_cost = 0
    chosen_countries = []
    for country, cost in costs.items():
        # TODO: Modify the condition below to also reject countries whose cost exceeds the cost_threshold
        if total_cost + cost > budget or cost > cost_threshold:
            continue
        total_cost += cost
        chosen_countries.append(country)
    return chosen_countries

def calculate_cost(countries, costs):
    total_cost = 0
    for country in countries:
        total_cost += costs[country]
    return total_cost

# Assuming sample data for budget, cost threshold, and costs for demonstration
travel_budget = 5000
cost_threshold = 1000  # New cost preference limit
country_costs = {'France': 1200, 'Italy': 1500, 'Spain': 800, 'Germany': 900, 'Greece': 1100}

chosen_countries = choose_countries(travel_budget, cost_threshold, country_costs)
trip_cost = calculate_cost(chosen_countries, country_costs)

print(f"The countries selected within budget and cost preference are: {chosen_countries}")
print(f"The total cost of the trip is: ${trip_cost}")