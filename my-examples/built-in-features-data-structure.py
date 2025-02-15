my_list = [1, 2, 3, 4]  # This is a list of numbers


my_list = [1, "apple", 3.14]  # A list with a number, a string, and a float


my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4]


my_list = [1, 2, 3]
my_list.insert(1, 10)  # Inserts 10 at position 1 (between 1 and 2)
print(my_list)  # Output: [1, 10, 2, 3]


my_list = [1, 2, 3, 4]
my_list.remove(3)  # Removes the item 3
print(my_list)  # Output: [1, 2, 4]

my_list = [1, 2, 3, 4]
item = my_list.pop()  # Removes and returns the last item (4)
print(item)  # Output: 4
print(my_list)  # Output: [1, 2, 3]


my_list = [1, 2, 3, 4]
position = my_list.index(3)  # Finds the position of 3
print(position)  # Output: 2


my_list = [1, 2, 2, 3, 4]
count = my_list.count(2)  # Counts how many times 2 appears
print(count)  # Output: 2


my_list = [4, 2, 3, 1]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]


my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]


my_list = [1, 2, 3, 4]
length = len(my_list)
print(length)  # Output: 4


my_set = {1, 2, 3}


my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
print(my_set)  # Output: {1, 2, 3, 4}


my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}


my_set = {1, 2, 3}
my_set.discard(4)  # Does nothing because 4 is not in the set
print(my_set)  # Output: {1, 2, 3}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
combined = set1.union(set2)
print(combined)  # Output: {1, 2, 3, 4, 5}


set1 = {1, 2, 3}
set2 = {2, 3, 4}
common = set1.intersection(set2)
print(common)  # Output: {2, 3}


set1 = {1, 2, 3}
set2 = {2, 3, 4}
diff = set1.difference(set2)
print(diff)  # Output: {1}


print(len(my_set))  # Output: 3


my_tuple = (1, 2, 3)


my_tuple = (1, 2, 3)
print(my_tuple[1])  # Output: 2


my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # Output: 2


my_tuple = (1, 2, 3)
print(my_tuple.index(2))  # Output: 1


print(len(my_tuple))  # Output: 3


my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


my_dict = {"name": "Alice", "age": 25}


print(my_dict["name"])  # Output: Alice


my_dict["age"] = 26  # Update the age
my_dict["city"] = "New York"  # Add a new key-value pair
print(my_dict)  # Output: {"name": "Alice", "age": 26, "city": "New York"}


del my_dict["city"]
print(my_dict)  # Output: {"name": "Alice", "age": 26}


print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
print(my_dict.values())  # Output: dict_values(['Alice', 26])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 26)])


print(len(my_dict))  # Output: 2


print("name" in my_dict)  # Output: True
print("address" in my_dict)  # Output: False


print(my_dict.get("age"))  # Output: 26
print(my_dict.get("address"))  # Output: None


my_list = [1, 2, 3]
print(len(my_list))  # Output: 3


my_list = [1, 2, 3]
my_set = set(my_list)  # Convert list to set
print(my_set)  # Output: {1, 2, 3}

my_tuple = tuple(my_list)  # Convert list to tuple
print(my_tuple)  # Output: (1, 2, 3)


employees = ["Alice", "Bob", "Charlie"]

employees.append("David")  # Adds David to the list of employees

employees.insert(0, "Eve")  # Adds Eve at the beginning as the team lead

employees.remove("Charlie")  # Removes Charlie from the list of employees

last_employee = employees.pop()  # Removes the last employee from the list

position = employees.index("Alice")  # Finds where Alice is in the list

count_of_managers = employees.count("Manager")  # Count how many Managers there are

employees.sort()  # Sorts employees alphabetically

employees.reverse()  # Reverses the order of the employees

number_of_employees = len(employees)  # Get the number of employees on the list




departments = {"HR", "Finance", "Engineering"}
departments.add("Marketing")  # Adds the Marketing department

departments.remove("Finance")  # Removes the Finance department

departments.discard("Legal")  # Removes "Legal" if it exists, nothing happens if not

office1 = {"HR", "Finance"}
office2 = {"Engineering", "Marketing"}
all_departments = office1.union(office2)  # Combines all departments from both offices

common_departments = office1.intersection(office2)  # Finds common departments

difference = office1.difference(office2)  # Finds departments in office1 but not office2

number_of_departments = len(departments)  # Finds how many unique departments exist


project = ("Website Redesign", 50000, "2025-05-01")

project_name = project[0]  # Gets the project name

project_count = project.count("Website Redesign")  # Counts how many times the project appears

project_index = project.index("Website Redesign")  # Finds the position of the project in the tuple

project_length = len(project)  # Finds how many details are in the project (name, budget, deadline)

name, budget, deadline = project  # Unpacks the tuple into three variables



employee_info = {"name": "Alice", "job_title": "Manager", "salary": 70000}

salary = employee_info["salary"]  # Gets Alice's salary

employee_info["location"] = "New York"  # Adds a location key for Alice
employee_info["salary"] = 75000  # Updates Alice's salary to 75,000

del employee_info["location"]  # Removes the location information from Alice's record

keys = employee_info.keys()  # Gets all the keys ("name", "job_title", "salary")

values = employee_info.values()  # Gets all the values ("Alice", "Manager", 75000)

items = employee_info.items()  # Gets all key-value pairs

length = len(employee_info)  # Finds how many key-value pairs are in the employee’s record

has_salary = "salary" in employee_info  # Checks if "salary" is a key in the dictionary

department = employee_info.get("department", "Not Assigned")  # If no department, returns "Not Assigned"

number_of_projects = len(project)  # Finds how many projects there are
number_of_employees = len(employees)  # Finds how many employees are on the list

employee_tuple = tuple(employees)  # Converts the list of employees into a tuple

