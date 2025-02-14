#LISTS
students = ["student1", "student2", "student3", "student1"]
students.append("student4")
students.insert(1, "student5")
students.remove("student2")
removed_item = students.pop()
position = students.index("student5")
print(students)
print(removed_item)
print(position)
count = students.count("student3")
print(count)


numbers = [4, 2, 7, 1, 3]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

number_length = len(numbers)
print("number length: ", number_length)


#SETS
my_set = {8, 20, 18, 9, 77, 46, 23}  # set with numbers
# my_set = {11, "apple", 5.6, True}  # set with different data types


my_set.remove(20)
my_set.discard(78)
my_set.add(78)
print(my_set)


set1 = {34, 87, 45, 17, 14}
set2 = {99, 73, 15, 84, 14}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print(union_set)
print(intersection_set)
print(difference_set)
set1_length = len(set1)
print(set1_length)


# TUPLES
my_tuple = (24, 65, 13)
print(my_tuple[2])
count_65 = my_tuple.count(65)
print(count_65)
#index_of_19 = my_tuple.index(19)
#print(index_of_19)

a, b, c = my_tuple
print(a)
print(b)
print(c)

length_my_tuple = len(my_tuple)
print(length_my_tuple)


#DICTIONARIES

employee_info = {"name": "Alice", "job_title": "Manager", "salary": 5000}
print(employee_info)

salary = employee_info["salary"]
print(salary)

employee_info["location"] = "New York"
employee_info["salary"] = 3000
print(employee_info)

del employee_info["location"]
print(employee_info)


keys = employee_info.keys()
print(keys)

values = employee_info.values()
print(values)

items = employee_info.items()
print(items)

len_employee_info = len(employee_info)
print(len_employee_info)

print("name" in employee_info)
print("address" in employee_info)

print(employee_info.get("name"))
print(employee_info.get("job_title"))




























