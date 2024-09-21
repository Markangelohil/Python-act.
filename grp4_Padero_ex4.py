
def check_condition(value):
   
    if value > 10:
        return True
    else:
        return False

test_value = 15
result = check_condition(test_value)
print(f"Condition result for {test_value}: {result}")

test_value = 5
result = check_condition(test_value)
print(f"Condition result for {test_value}: {result}")

# List - Ordered and mutable
my_list = ["apple", 25, True, "banana", 100, False]
print("List:", my_list)

# Tuple - Ordered and immutable
my_tuple = ("orange", 50, False, "grape", 200, True)
print("Tuple:", my_tuple)

# Set - Unordered, mutable, and unique items
my_set = {"car", 30, True, "bike", 50, False}
print("Set:", my_set)

# Dictionary - Key-value pairs, mutable and unordered before Python 3.7 (but ordered now)
my_dict = {
    "name": "John",
    "age": 28,
    "is_student": False,
    "city": "New York",
    "grade": 85,
    "is_graduated": True
}
print("Dictionary:", my_dict)
