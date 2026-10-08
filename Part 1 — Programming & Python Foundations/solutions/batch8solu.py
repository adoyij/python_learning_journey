# for number in  range(5):
#     print("welcome")

# for number in range(1,11,3):
#     print(number)
# for transaction in range(6):
#     print(f"transactoin {transaction}")
# practice 3 ......
# prices = [ 2000, 3500, 1500, 5000, 2500]
# total = 0
# for price in prices:
#     total += price
#     print(f"total{total}")
# practice4..........
# price = [1000, 2500, 3000, 1500]
# total = 0
# for price in price:
#     total += price
#     print(total)
# count = 0
# for nunber in transaction (1, 6):
#     count += 1
#     print(count)

# tinyurl.com/otukpoarise

# Understand what the program needs to do.................
# Store equipment
# View all equipment
# Add new equipment
# Issue equipment to a fellow
# Accept returned equipment
# Search for equipment
# Track who currently has an item
# Show available/unavailable equipment
# Produce accurate reports
# Prevent invalid operations


# Learn2Earn Equipment Lending System..............

inventory = {
    1: {"name": "Laptop", "total": 10, "available": 10},
    2: {"name": "keyboard", "total": 5, "available": 5},
    3: {"name": "headset", "total": 3, "available": 3}
}

loans = []


def view_inventory():
    print("\n--- INVENTORY ---")
    for id, item in inventory.items():
        print(id, item["name"],
              "| Total:", item["total"],
              "| Available:", item["available"])


def issue_item():
    view_inventory()
    id = int(input("Enter equipment ID: "))
    qty = int(input("Enter quantity: "))
    borrower = input("Enter borrower name: ")

    if id in inventory and qty > 0:
        if qty <= inventory[id]["available"]:
            inventory[id]["available"] -= qty
            loans.append([id, borrower, qty])
            print("Equipment issued successfully.")
        else:
            print("Not enough equipment available.")
    else:
        print("Invalid equipment or quantity.")


def return_item():
    id = int(input("Enter equipment ID: "))
    borrower = input("Enter borrower name: ")
    qty = int(input("Enter quantity returned: "))

    for loan in loans:
        if loan[0] == id and loan[1].lower() == borrower.lower():
            if qty <= loan[2]:
                inventory[id]["available"] += qty
                loan[2] -= qty

                if loan[2] == 0:
                    loans.remove(loan)

                print("Equipment returned successfully.")
                return

    print("Loan record not found.")


def search_item():
    search = input("Search equipment: ").lower()

    for id, item in inventory.items():
        if search in item["name"].lower():
            print(id, item["name"],
                  "| Available:", item["available"])


def report():
    total = sum(item["total"] for item in inventory.values())
    available = sum(item["available"] for item in inventory.values())
    issued = total - available

    print("\n--- REPORT ---")
    print("Total items:", total)
    print("Available:", available)
    print("Issued:", issued)
    print("Active loans:", len(loans))


while True:
    print("\n===== LEARN2EARN =====")
    print("1. View Inventory")
    print("2. Issue Equipment")
    print("3. Return Equipment")
    print("4. Search Inventory")
    print("5. Report")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        issue_item()
    elif choice == "3":
        return_item()
    elif choice == "4":
        search_item()
    elif choice == "5":
        report()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")