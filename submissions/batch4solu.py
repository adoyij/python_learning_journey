# balance = 10000
# deposit = 5000
# withdraw = 2000
# fee = 500
# balance_after_deposit = balance + deposit
# balance_after_withdraw = balance + deposit - withdraw
# balance_after_fee = balance + deposit - withdraw - fee
# print(balance_after_deposit)
# print(balance_after_withdraw)
# print(balance_after_fee)

# balance = 10000
# deposit = 5000
# withdraw = 2000
# fee = 500
# balance += deposit
# balance -= withdraw
# balance -= fee

# print(f'balance after deposit {balance}')
# print(f'balance after withdraw {balance}')
# print(f'balance fter fee {balance}')


# balance = 10000
# deposit = 5000
# withdraw = 2000
# fee = 500
# balance += deposit -withdraw - fee
# can_withdraw = withdraw <= balance
# print(can_withdraw)
# print(balance)

product_price = 100000
quantity = 10
discount = 20
total = 999980
subtotal = 1000000
valid_quantity = quantity > 0
valid_total = total > 0
valid_discount = discount <= subtotal
subtotal = product_price * quantity
total = subtotal - discount
print(valid_quantity)
print(valid_discount)
print(valid_total)
print(subtotal)
print(total)
