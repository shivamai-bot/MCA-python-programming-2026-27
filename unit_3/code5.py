
# Create employee dictionary
employees = {
    101: {"name": "Rahul", "department": "IT", "salary": 50000},
    102: {"name": "Amit", "department": "HR", "salary": 40000},
    103: {"name": "Priya", "department": "Finance", "salary": 60000}
}

# Add employee
employees[104] = {"name": "Neha", "department": "IT", "salary": 45000}

# Update employee salary
employees[101]["salary"] = 55000

# Delete employee
del employees[103]

# Display dictionary
print("--- Employee Details ---")
print("Keys:", employees.keys())
print("Values:", employees.values())
print("Items:", employees.items())

# Search employee by ID
emp_id = int(input("\nEnter Employee ID to search: "))

if emp_id in employees:
    print("Employee Found:", employees[emp_id])
else:
    print("Employee Not Found")

# Dictionary Comprehension
salary = int(input("\nEnter minimum salary: "))

high_salary = {
    emp_id: details
    for emp_id, details in employees.items()
    if details["salary"] > salary
}

print("\nEmployees Earning Above", salary)
print(high_salary)