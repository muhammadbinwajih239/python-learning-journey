products = []
prices = []
quantities = []

# Adding products using append()
products.append("Notebook")
prices.append(100)
quantities.append(1)

products.append("Pen")
prices.append(20)
quantities.append(2)

products.append("Pencil")
prices.append(10)
quantities.append(1)


# Function to calculate product total
def calculate_total(price, quantity):
    return price * quantity


notebook_total = calculate_total(prices[0], quantities[0])
pen_total = calculate_total(prices[1], quantities[1])
pencil_total = calculate_total(prices[2], quantities[2])

subtotal = notebook_total + pen_total + pencil_total


# Function to calculate discount
def calculate_discount(amount, percentage):
    discount = amount * percentage / 100
    return discount


discount = calculate_discount(subtotal, 10)
final_amount = subtotal - discount


# Display bill
print("===== MINI BILL =====")

print("Products:", products)
print("First two products:", products[:2])

print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)
