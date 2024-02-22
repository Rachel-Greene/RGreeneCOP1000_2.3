# Furniture.py - This program calculates profits and sales prices for a furniture company

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
profit = retailPrice - wholesalePrice
salePercentage = 25/100
# SalePercentage defined so the sale amount can change easily as the owner needs 
salePrice = retailPrice * (1- salePercentage)
saleProfit = salePrice - wholesalePrice


print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))