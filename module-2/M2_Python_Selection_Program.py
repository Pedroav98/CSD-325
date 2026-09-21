def calculate_cost(feet_of_cable):
    if feet_of_cable > 500:
        cost_of_cable = feet_of_cable * 0.50
    elif feet_of_cable > 250:
        cost_of_cable = feet_of_cable * 0.70
    elif feet_of_cable > 100:
        cost_of_cable = feet_of_cable * 0.80
    else:
        cost_of_cable = feet_of_cable * 0.87

    return cost_of_cable


print("Welcome to Pedro's Fiber Optic Cable Company!")

feet_of_cable = float(
    input("Please enter the number of feet of fiber optic cable: ")
)

cost_of_cable = calculate_cost(feet_of_cable)

message = f'The cost is {cost_of_cable} for installing {feet_of_cable} feet of cable.'

print(message)
