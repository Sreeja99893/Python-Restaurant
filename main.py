# Python Restaurant
# List containing the dictionary of menu items and prices
# Menu items with their prices
item = [
    {
        "soya cappuccino": "120",
        "cappuccino": "100",
        "hot velvet coffee": "150",
        "lemon green coffee": "100",
        "flat white": "50",
        "filter coffee": "100",
        "cafe mocha": "120"
    }
]

# Print welcome message
print("Welcome to Python Restaurant")

# Print the menu items one by one
for coffee, price in item[0].items():
    print(f"{coffee}: ₹{price}")
print("Do you want to order..?")

# Initialize variables
selected_items = []
total_amount = 0

# Ordering process
while True:
    user_response = input("Enter 'yes' if you want to order coffee, 'no' to finish: ")
    if user_response == 'yes':
        coffee_name = input("Please enter the coffee name: ")
        if coffee_name in item[0]:
            selected_items.append(coffee_name)
            total_amount += int(item[0][coffee_name])
            print(f"Added {coffee_name}. Current total is ₹{total_amount}.")
        else:
            print("Sorry, we don't have that item. Please select another item.")
    elif user_response == 'no':
        break
    else:
        print("Invalid input, please enter 'yes' or 'no'.")

# Print selected items and total amount
if selected_items:
    print(f"You selected items: {', '.join(selected_items)} and the total price is ₹{total_amount}.")
else:
    print("No items selected.")

print("Visit again :)")
