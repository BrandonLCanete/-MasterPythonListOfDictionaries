# List of employee dictionaries
employee_list_dictionaries = [
    {
        "employee_id" : 1,
        "employee_name" : "Arthur Morgan",
        "employee_job_title" : "Designer",
        "employee_department" : "IT",
        "employee_salary" : "20,000.00",
        "employee_schedule_work" : "Monday to Friday"
    },
    {
        "employee_id" : 2,
        "employee_name" : "Henry Goose",
        "employee_job_title" : "Developer",
        "employee_department" : "IT",
        "employee_salary" : "30,000.00",
        "employee_schedule_work" : "Monday to Saturday"
    },
    {
        "employee_id" : 3,
        "employee_name" : "Jeffrey Morrey",
        "employee_job_title" : "Advertiser",
        "employee_department" : "HR",
        "employee_salary" : "25,000.00",
        "employee_schedule_work" : "Monday to Thursday"
    },
    {
        "employee_id" : 4,
        "employee_name" : "Godfrey Huther",
        "employee_job_title" : "Engineer",
        "employee_department" : "Construction",
        "employee_salary" : "35,000.00",
        "employee_schedule_work" : "Monday to Friday"
    },
    {
        "employee_id" : 5,
        "employee_name" : "Angeline Grace",
        "employee_job_title" : "Secretary",
        "employee_department" : "HR",
        "employee_salary" : "33,000.00",
        "employee_schedule_work" : "Monday to Saturday"
    }
]
# Loop through the list of dictionaries
for employees in employee_list_dictionaries:
    # Print the data
    print(f"Employee Name: {employees['employee_name']}, Employee Job Title: {employees['employee_job_title']}, Employee Department: {employees['employee_department']}, Employee Salary : {employees['employee_salary']}, Employee Schedule Work: {employees['employee_schedule_work']}")