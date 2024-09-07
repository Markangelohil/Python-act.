# A program for you calculate the length of a string.


user_string = input("Enter a string: ")

length = 0

for char in user_string:
    length += 1

print("The length of the string is:", length)


#  A program count the number of characters in a string.

user_string = input("Enter a string: ")

char_count = len(user_string)

print("The number of characters in the string is:", char_count)


#  A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

user_string = input("Enter a string: ")

first_char = user_string[0]

modified_string = first_char

for char in user_string[1:]:
    if char == first_char:
        modified_string += '$'
    else:
        modified_string += char

print("Modified string:", modified_string)


#  A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

string1 = input(" first string: ")
string2 = input("second string: ")

if len(string1) < 2 or len(string2) < 2:
    print("Both strings must have at least 2 characters.")
else:

    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]

    result = new_string1 + " " + new_string2

    print("Resulting string:", result)
    


# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces

string1 = input(" first name: ")
string2 = input(" middle name: ")
string3 = input(" last name: ")
string4 = input(" year & section: ")

result = string1 + " " + string2 + " " + string3 + " " + string4

print("Concatenated string:", result)


# Using + Concatenate Strings in Python get two strings from user input and concatenate them

string1 = input("first name: ")
string2 = input("last name: ")

result = string1 + " " + string2

print("Concatenated string: ", result )


# Using + Concatenate in Python using your name and your age in a paragraph

name = input(" Name: ")  
age = input(" Age: ")    

paragraph = "My name is " + name + " and I am " + str(age) + " years old."

# Output: Display the paragraph
print(paragraph)
