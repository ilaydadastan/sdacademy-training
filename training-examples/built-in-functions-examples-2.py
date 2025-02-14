
# loops in data structures
colors = ("red", "green", "blue")
for color in colors:
    print(color)


names = ["ilayda", "dmitri", "tiit"]
for name in names:
    print(name)

# SETS EXAMPLE

departments = {"HR", "Finance", "Engineering"}
print(departments)

departments.add("Marketing")
print(departments)

departments.remove("Finance")
print(departments)

office1 = {"HR", "Finance", "Marketing"}
office2 = {"Engineering", "Test", "Business Analyst"}

all_departments = office1.union(office2)
print(all_departments)

number_of_departments = len(all_departments)
print(number_of_departments)


# TUPLE
# project name, budget, deadline
project = ("website redesign", 2000, "2025-10-02")
print(project)

project_name = project[0]
print(project_name)

projects = ["website redesign", "website redesign", "app launch"]
project_count = projects.count("website redesign")
print(project_count)

name, budget, deadline = project
print(name, budget, deadline)


# LISTS

employees = ["Alice", "Bob", "Charlie"]
employees.append("David")
employees.insert(0, "Eve")
employees.remove("Bob")
employees.pop()
employees.sort()
employees.reverse()
print(employees)


patient_queue = ["John Doe", "Jane", "Alice"]

trending_hashtags = {"#AI", "#Python", "#MachineLearning"}









