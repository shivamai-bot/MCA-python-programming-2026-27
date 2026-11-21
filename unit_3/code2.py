
# Accept student information
name = input("Enter student's full name: ").strip()
email = input("Enter email address: ")
mobile = input("Enter mobile number: ")

# Extract first name and last name using slicing
first_space = name.find(" ")
last_space = name.rfind(" ")

if first_space != -1:
    first_name = name[:first_space]
    last_name = name[last_space + 1:]
else:
    first_name = name
    last_name = name

# Reverse student's name
reverse_name = name[::-1]

# Extract email username and domain
username, domain = email.split("@", 1)

# Extract last four digits of mobile number
last_four = mobile[-4:]

# Display student information
print("\n--- Student Information ---")

# Using f-string formatting
print(f"Full Name: {name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Reversed Name: {reverse_name}")

# Using format() method
print("Email Username: {}".format(username))
print("Email Domain: {}".format(domain))

# Using f-string formatting
print(f"Last Four Mobile Digits: {last_four}")

# Positive and Negative Indexing
print("\n--- String Indexing ---")
print("First Character:", name[0])
print("Last Character:", name[-1])

# String formatting
print("\nStudent: %s | Mobile: %s" % (name, mobile))