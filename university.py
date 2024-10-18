# List of university dictionaries
university_list_dictionaries = [
    {
        "university_id" : 1,
        "university_name" : "University of the Philippines",
        "university_location" : "Diliman, Quezon City",
        "university_size" : "493 hectares",
        "university_founded_date" : "February 12, 1949",
        "university_campus" : "Suburban",
    },
    {
        "university_id" : 2,
        "university_name" : "Ateneo de Manila University",
        "university_location" : "Katipunan Ave, Quezon City",
        "university_size" : "83 hectares",
        "university_founded_date" : "December 10, 1859",
        "university_campus" : "Urban"
    },
    {
        "university_id" : 3,
        "university_name" : "University of Santo Tomas",
        "university_location" : "España Blvd, Sampaloc, Manila",
        "university_size" : "21.5 hectares",
        "university_founded_date" : "April 28, 1611",
        "university_campus" : "Urban"
    },
    {
        "university_id" : 4,
        "university_name" : "De La Salle University",
        "university_location" : "Taft Ave, Malate, Manila",
        "university_size" : "5.4 hectares",
        "university_founded_date" : "June 16, 1911",
        "university_campus" : "Urban"
    },
    {
        "university_id" : 5,
        "university_name" : "Mapúa University",
        "university_location" : "Muralla St, Intramuros, Manila",
        "university_size" : "1.79 hectares",
        "university_founded_date" : "January 25, 1925",
        "university_campus" : "Urban"
    }
]
# Loop through the dictionaries
for universities in university_list_dictionaries:
    # Print the data
    print(f"University Name: {universities['university_name']}, University Location: {universities['university_location']}, University Size: {universities['university_size']}, University Founded Date: {universities['university_founded_date']}, University Campus: {universities['university_campus']}")