# 
# def wallet_balance():
#   balance = 10000

#   if  balance > 0:
#     print("you have money")
#   else:
#     print("your wallet is empty")

# wallet_balance()

# balance = 50000
# if balance == 50000:
#     print("balance is exactly #50,000.")
# if balance >= 50000:
#     print("balance meet the minimun")
# balance = 3000
# if balance < 50000:
#     print("balance is below #50,000")
# def conditions_that_check_pricess():
#     price = 5000
#     if price > 3000:
#         print(f"price is greater than #3000")
#     if price < 10000:
#         print("price is less than #1000")
#     if price == 5000:
#         print("price is exactly #5000")
#     if price != 2000:
#         print("price is not #2000")
        
# conditions_that_check_pricess()

 

 #practice 1 .and 2...

# balance = float(input("balance:"))
# if balance == 1000 and balance > 0:
#     print("you  have money")
# else:
#     print("your walletis empty")

#practice 3............
# balance = 75000
# balance = float(input("balance:"))
# if balance > 100000:
#     print("High balance")
# elif balance > 50000:
#     print("Medium balance")
# elif balance > 0:
#     print("Low balance")
# else:
#     print("Empty wallet")

# score = float(input("score:"))

# if score >= 90:
#     print("Excellent")
# elif score >= 70:
#     print("Good")
# elif score >= 50:
#     print("Pass")
# else:
#     print("Fail")

# balance = 80000

# if balance > 100000:
#     print("A")
# elif balance > 50000:
#     print("B")
# elif balance > 10000:
#     print("C")
# else:
#     print("D")

#practice 6.....
# payment_method = input("Payment method ")
# if payment_method == "cash" or payment_method == "card":
#    print("Payment method accepted.")


#    Let's build a store discount system. practice  7 .......

# ```python
# total = float(input("Enter total: "))

# if total >= 100000:
#     print("Large purchase")
# elif total >= 50000:
#     print("Medium purchase")
# elif total >= 10000:
#     print("Small purchase")
# else:
#     print("Very small purchase")

#practice 8........
# order = float(input("order"))
# order  == 2000000
# if order >= 100000:
#     print("large order")
# if order >= 50000:
#     print("medium order")
# if order >= 10000:
#     print("small order")
# else:
#     print("basic order")

#practice9 ........
# balance = 50000
# withdraw = 20000
# if balance > withdraw:
#    print("can withdraw")
# if withdraw <= balance:
#    print("can withdraw")
# else:
#     print("invalid transaction")
# acqual vavuel for balance is 50000
# acqual valve for withdraw is 20000
# balance is equal to 50000
# withdraw is equal to 20000
# the final balance after withdrawal is 30000
# withdraw can only happen when, withdraw is less than the avialable ballance
# if the withdraw is higher than the  avialable balance withdraw will Fail
# the bollean result that the expresion roduce is true because the condision given to the program is true
# product_name = "phone"
# price = 100000
# quantity = 10
# sub_total = price * quantity
# discount = 0.1 * price
# if sub_total >= 100000:
#     print(discount)
#     discount = 0.05 * sub_total
# if sub_total >= 50000:
#     print(discount)
#     total = sub_total - discount - discount
#     print(total)
# if sub_total <= 0:
#     otherwise = 0
#     print(otherwise)

#practice....10
 # Simple Store Discount Calculator

# Ask the user for information
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

# Calculate subtotal
subtotal = price * quantity

# Determine discount
if subtotal >= 100000:
    discount_rate = 0.10
elif subtotal >= 50000:
    discount_rate = 0.05
else:
    discount_rate = 0.00

# Calculate discount amount
discount = subtotal * discount_rate

# Calculate final total
total = subtotal - discount

# Display receipt
print("\n========== RECEIPT ==========")
print(f"Product:  {product_name}")
print(f"Price:    ₦{price:,.2f}")
print(f"Quantity: {quantity}")
print("-----------------------------")
print(f"Subtotal: ₦{subtotal:,.2f}")
print(f"Discount: ₦{discount:,.2f}")
print(f"Total:    ₦{total:,.2f}")
print("=============================")
print("Thank you for shopping!")