# List of restaurant dictionaries
restaurant_list_dictionaries = [
    {
        "restaurant_id" : 1,
        "restaurant_name" : "Manila Bay Kitchen",
        "restaurant_cuisine" : "Filipino, Bar, Pizza, Seafood, International",
        "restaurant_location" : "Sheraton Manila Bay, Manila"
    },
    {
        "restaurant_id" : 2,
        "restaurant_name" : "Cafe Ilang-Ilang",
        "restaurant_cuisine" : "Local cuisine, Italian, Chinese, Japanese, American, Filipino",
        "restaurant_location" : "One Rizal Park Manila Hotel"
    },
    {
        "restaurant_id" : 3,
        "restaurant_name" : "The Aristocrat Restaurant",
        "restaurant_cuisine" : "Filipino",
        "restaurant_location" : "San Andres Street, Manila"
    },
    {
        "restaurant_id" : 4,
        "restaurant_name" : "Estoria Manila",
        "restaurant_cuisine" : "Filipino, Bar, Cafe, Spanish, Asian",
        "restaurant_location" : "Ermita Ermita Plaza, Manila"
    },
    {
        "restaurant_id" : 5,
        "restaurant_name" : "Barbara's Heritage Restaurant",
        "restaurant_cuisine" : "Filipino, International, Asian",
        "restaurant_location" : "Intramuros, Manila"
    }
]
# Loop through the list of dictionaries
for restaurants in restaurant_list_dictionaries:
    # Print the data
     print(f"Restaurant Name: {restaurants['restaurant_name']}, Restaurant Cuisine: {restaurants['restaurant_cuisine']}, Restaurant Location: {restaurants['restaurant_location']}")