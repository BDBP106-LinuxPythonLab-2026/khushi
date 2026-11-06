# 5. Shopping List Manager
# Concepts: lists, while loop menu, append(), remove(), in, sort(), enumerate()
# Build a menu-driven program that keeps running until the user picks Quit:
# 1. Add item 2. Remove item 3. View list 4. Sort list 5. Quit
# Don't add duplicates (check case-insensitively). Print a friendly message when the user
# tries to remove an item that isn't on the list. Show the list numbered from 1.


items = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Sort list")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")

        if item.lower() in [x.lower() for x in items]:
            print("Item already exists!")
        else:
            items.append(item)
            print("Item added successfully!")

    elif choice == "2":
        item = input("Enter item to remove: ")

        for x in items:
            if x.lower() == item.lower():
                items.remove(x)
                print("Item removed successfully!")
                break
        else:
            print("Item not found in the shopping list!")

    elif choice == "3":
        if not items:
            print("Shopping list is empty!")
        else:
            print("\nShopping List:")
            for i, item in enumerate(items, start=1):
                print(i, ".", item)

    elif choice == "4":
        items.sort(key=str.lower)
        print("Shopping list sorted successfully!")

    elif choice == "5":
        print("Thank you for using Shopping List Manager!")
        break

    else:
        print("Invalid choice! Please select 1-5.")