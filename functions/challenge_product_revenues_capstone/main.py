# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


# Function to calculate revenue
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, quantity in zip(prices, quantities_sold):
        revenue.append(price * quantity)
    return revenue

# Function to sort and print formatted output
def formatted_output(revenues):
    sorted_revenues = sorted(revenues)  # uses sorted()
    for product, revenue in sorted_revenues:
        print(f"{product} has total revenue of ${revenue:.2f}.")

# Calculate revenue
revenue = calculate_revenue(prices, quantities_sold)

# Combine products and revenue using zip()
revenue_per_product = list(zip(products, revenue))

# Display results
formatted_output(revenue_per_product)