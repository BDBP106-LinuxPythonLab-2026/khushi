# 10. Inventory and Billing System
# Concepts: dictionary of tuples, nested data, while loop, if validation, string formatting
# with ljust()/rjust()/f-strings
# inventory = {
# "pen": (10.0, 50), # (price, quantity in stock)
# "notebook": (45.0, 20),
# "eraser": (5.0, 100),
#
# "marker": (30.0, 15),
# }
# Let the customer keep entering item quantity (for example pen 3) until they type done.
# For each entry:
# • reject unknown items and quantities that aren't valid numbers
# • reject the order if there isn't enough stock
# • otherwise, add it to a cart dictionary (merging repeated items) and reduce the
# stock (tuples can't be changed, so replace the tuple)
# At the end, print an aligned receipt with the item, quantity, unit price and line total.
# Apply a 10% discount if the subtotal is over ₹500. Then print the updated inventory, and
# mark items with fewer than 10 left as LOW STOCK.

inventory = {
    "pen": (10.0, 50),
    "notebook": (45.0, 20),
    "eraser": (5.0, 100),
    "marker": (30.0, 15)
}

cart = {}

while True:
    item = input("Enter item name (or 'done' to finish): ").lower().strip()

    if item == "done":
        break

    if item not in inventory:
        print("Invalid item! Please try again.")
        continue

    try:
        qty = int(input("Enter quantity: "))

        if qty <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Invalid quantity! Enter a valid number.")
        continue

    price, stock = inventory[item]

    if qty > stock:
        print("Insufficient stock! Available quantity:", stock)
        continue

    # Add item to cart or merge with existing quantity
    cart[item] = cart.get(item, 0) + qty

    # Update inventory (tuples are immutable)
    inventory[item] = (price, stock - qty)

    print("Item added to cart successfully!")

# Print receipt
print("\n" + "=" * 60)
print(" " * 22 + "RECEIPT")
print("=" * 60)

print(f"{'Item'.ljust(15)}{'Qty'.rjust(6)}"
      f"{'Unit Price'.rjust(15)}{'Line Total'.rjust(15)}")
print("-" * 60)

subtotal = 0

for item, qty in cart.items():
    price, stock = inventory[item]
    line_total = price * qty
    subtotal += line_total

    print(f"{item.ljust(15)}{str(qty).rjust(6)}"
          f"{price:>15.2f}{line_total:>15.2f}")

print("-" * 60)
print(f"{'Subtotal:'.rjust(45)} ₹{subtotal:.2f}")

discount = 0

if subtotal > 500:
    discount = subtotal * 0.10
    print(f"{'Discount (10%):'.rjust(45)} ₹{discount:.2f}")

total = subtotal - discount

print(f"{'Final Amount:'.rjust(45)} ₹{total:.2f}")
print("=" * 60)

# Display updated inventory
print("\nUPDATED INVENTORY")
print("-" * 50)
print(f"{'Item'.ljust(15)}{'Price'.rjust(10)}"
      f"{'Stock'.rjust(10)}{'Status'.rjust(15)}")
print("-" * 50)

for item, (price, stock) in inventory.items():
    if stock < 10:
        status = "LOW STOCK"
    else:
        status = "Available"

    print(f"{item.ljust(15)}{price:>10.2f}"
          f"{stock:>10}{status:>15}")

