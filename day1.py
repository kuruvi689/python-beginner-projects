cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price * 100) if cost_price != 0 else 0
    print("Profit: ", profit)
    print("Profit Percentage: ", profit_percentage, "%")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price * 100) if cost_price != 0 else 0
    print("Loss: ", loss)
    print("Loss Percentage: ", loss_percentage, "%")
else:    print("No profit, no loss.")
