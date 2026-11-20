# Billing & Discount System
# A beginner-level command-line project using Python lists, loops, conditions,
# string methods, and basic calculations.

print("=" * 55)
print("             BILLING & DISCOUNT SYSTEM")
print("=" * 55)

# These lists store the details of each product.
product_names = []
prices = []
quantities = []
line_totals = []

print("\nEnter product details one by one.")
print("Type 'done' when you have added all products.\n")

# Collect product information.
while True:
    product_name = input("Product name: ").strip()

    if product_name.lower() == "done":
        break

    if product_name == "":
        print("Product name cannot be empty. Please try again.\n")
        continue

    # Validate the product price.
    while True:
        price_text = input("Price per item (Rs.): ").strip()

        if price_text.replace(".", "", 1).isdigit():
            price = float(price_text)

            if price > 0:
                break

        print("Enter a valid price greater than 0.\n")

    # Validate the product quantity.
    while True:
        quantity_text = input("Quantity: ").strip()

        if quantity_text.isdigit():
            quantity = int(quantity_text)

            if quantity > 0:
                break

        print("Enter a whole number greater than 0.\n")

    # Save the product details in their respective lists.
    product_names.append(product_name)
    prices.append(price)
    quantities.append(quantity)

    print("Product added successfully.\n")

# Stop if the customer did not add any products.
if len(product_names) == 0:
    print("\nNo products were added. No bill was created.")
else:
    # Calculate the total price of each product and the subtotal.
    subtotal = 0

    for index in range(len(product_names)):
        line_total = prices[index] * quantities[index]
        line_totals.append(line_total)
        subtotal = subtotal + line_total

    # Ask for a discount percentage between 0 and 100.
    while True:
        discount_text = input("\nDiscount percentage (0-100): ").strip()

        if discount_text.replace(".", "", 1).isdigit():
            discount_percent = float(discount_text)

            if 0 <= discount_percent <= 100:
                break

        print("Enter a valid discount percentage from 0 to 100.")

    discount_amount = subtotal * discount_percent / 100
    final_amount = subtotal - discount_amount

    # Display the receipt.
    print("\n" + "=" * 75)
    print("                              CUSTOMER BILL")
    print("=" * 75)
    print(f"{'No.':<5}{'Product':<25}{'Price (Rs.)':>14}{'Qty':>8}{'Total (Rs.)':>16}")
    print("-" * 75)

    for index in range(len(product_names)):
        print(
            f"{index + 1:<5}"
            f"{product_names[index]:<25}"
            f"{prices[index]:>14.2f}"
            f"{quantities[index]:>8}"
            f"{line_totals[index]:>16.2f}"
        )

    print("-" * 75)
    print(f"{'Subtotal:':>53} Rs. {subtotal:>10.2f}")
    print(f"{'Discount (' + str(discount_percent) + '%):':>53} Rs. {discount_amount:>10.2f}")
    print(f"{'Final Amount:':>53} Rs. {final_amount:>10.2f}")
    print("=" * 75)

    # Use list slicing to show a short preview of the first three products.
    preview_names = product_names[:3]

    print("\nQUICK PRODUCT PREVIEW")
    for product in preview_names:
        print(f"- {product}")

    if len(product_names) > 3:
        remaining_products = len(product_names) - 3
        print(f"...and {remaining_products} more product(s).")

    print("\nThank you for shopping!")
