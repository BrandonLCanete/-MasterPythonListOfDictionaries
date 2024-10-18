# List of product dictionaries
product_list_dictionaries = [
    {
        "product_id" : 1,
        "product_name" : "Kopiko Black 3 in 1 Twin Pack",
        "product_type" : "Coffee",
        "product_price" : "12.00",
        "product_net_weight" : "60 g"
    },
    {
        "product_id" : 2,
        "product_name" : "Piattos Sour Cream & Onion",
        "product_type" : "Chips",
        "product_price" : "45.00",
        "product_net_weight" : "85 g"
    },
    {
        "product_id" : 3,
        "product_name" : "Coke Original",
        "product_type" : "Soft Drink",
        "product_price" : "125.00",
        "product_net_weight" : "1.5 L"
    },
    {
        "product_id" : 4,
        "product_name" : "Golden Fiesta Cooking Oil",
        "product_type" : "Lipids",
        "product_price" : "72.25",
        "product_net_weight" : "485 ml"
    },
    {
        "product_id" : 5,
        "product_name" : "Tender Juicy Hotdog Regular",
        "product_type" : "Sausage",
        "product_price" : "226.70",
        "product_net_weight" : "1 kg"
    }
]

# Loop through the list of dictionaries
for products in product_list_dictionaries:
    # Print the data
    print(f"Product Name: {products['product_name']}, Product Type: {products['product_type']}, Product Price: {products['product_price']}, Product Net Weight: {products['product_net_weight']}")