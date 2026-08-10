
stock_prices = {"AAPL": 180, "TSLA": 250}

portfolio = {}
total_investment = 0

print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty


print("\n--- Investment Summary ---")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: save to file
save = input("\nSave to file? (y/n): ").lower()
if save == "y":
    with open("investment_summary.txt", "w") as f:
        f.write("Investment Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print("Saved to investment_summary.txt")