
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 170
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:", ", ".join(stock_prices.keys()))

num_stocks = int(input("\nHow many stocks do you want to add? "))

for i in range(num_stocks):
    stock_name = input(f"\nEnter Stock {i+1} Name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Invalid stock name! Skipping...")

print("\n===== PORTFOLIO SUMMARY =====")
print("{:<10} {:<10} {:<10} {:<10}".format(
    "Stock", "Price", "Quantity", "Value"
))

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value

    print("{:<10} {:<10} {:<10} {:<10}".format(
        stock, price, quantity, value
    ))

print("\n----------------------------------")
print("Total Portfolio Value: ₹", total_value)

save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock} | Price: ₹{price} | "
                f"Quantity: {quantity} | Value: ₹{value}\n"
            )

        file.write(f"\nTotal Portfolio Value: ₹{total_value}")

    print("Report saved successfully as 'portfolio_report.txt'")
else:
    print("Report not saved.")