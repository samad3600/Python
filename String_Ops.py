# String Operations in Python

# Initializing strings
str1 = "Hello"
str2 = "World"
str3 = "  Python Programming  "

# Concatenation
concat_str = str1 + " " + str2
print("Concatenation:", concat_str)

# Repetition
repeat_str = str1 * 3
print("Repetition:", repeat_str)

# Slicing
slice_str = str3[2:8]
print("Slicing:", slice_str)

# Length of the string
length = len(str3)
print("Length:", length)

# Stripping whitespace
stripped_str = str3.strip()
print("Stripped:", stripped_str)

# Upper and lower case
upper_str = str1.upper()
lower_str = str2.lower()
print("Upper case:", upper_str)
print("Lower case:", lower_str)

# Replace
replaced_str = str3.replace("Python", "Java")
print("Replace:", replaced_str)

# Split
split_str = str3.split()
print("Split:", split_str)

# Join
join_str = "-".join(split_str)
print("Join:", join_str)

# Find
find_index = str3.find("Python")
print("Find:", find_index)

# Check if string starts with a substring
starts_with = str1.startswith("He")
print("Starts with 'He':", starts_with)

# Check if string ends with a substring
ends_with = str2.endswith("ld")
print("Ends with 'ld':", ends_with)
