cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit: ", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss: ", loss)
else:    print("No profit, no loss.")
