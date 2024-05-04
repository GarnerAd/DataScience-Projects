# Create a list of menu items
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Create a dictionary of stock for each menu item
stock = {
    "Coffee": 100,
    "Tea": 80,
    "Sandwich": 50,
    "Cake": 20
}

# Create a dictionary of prices for each menu item
price = {
    "Coffee": 2.50,
    "Tea": 2.00,
    "Sandwich": 5.00,
    "Cake": 3.50
}

# Calculate the total stock worth in the café
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Print out the result
print("Total stock worth in the café: £", total_stock_worth)
