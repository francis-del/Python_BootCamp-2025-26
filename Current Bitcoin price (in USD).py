# Current Bitcoin price (in USD)
bitcoin_price = 55000

# User's Bitcoin holdings
bitcoin_amount = 0.754

# Calculate portfolio value
portfolio_value = bitcoin_price * bitcoin_amount

# Print results 
print("Current Bitcoin price: $", round(bitcoin_price, 2))  
print("Your Bitcoin holdings:", round(bitcoin_amount, 5), "BTC")  
# round(bitcoin_amount, 5) → rounds the value to 5 decimal places
print("Portfolio value: $", round(portfolio_value, 3))