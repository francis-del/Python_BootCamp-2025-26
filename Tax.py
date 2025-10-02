# Price of one item (in USD)
item_price = 25.50

# Number of items bought
quantity = 3

# Sales tax rate (8%)
tax_rate = 0.08

# Calculate subtotal
subtotal = item_price * quantity

# Calculate tax
tax = subtotal * tax_rate

# Calculate total cost
total_cost = subtotal + tax

# Display results (simple beginner-friendly printing)
print("Price per item: $", round(item_price, 2))
print("Quantity:", quantity)
print("Subtotal: $", round(subtotal, 2))
print("Tax (8%): $", round(tax, 2))
print("Total cost: $", round(total_cost, 2))