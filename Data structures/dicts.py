#Python Basics revision
#Dictionaries

#Creating dictionaries (key:value pairs)
student = {
    "name": "Alice",
    "age": 21,
    "course": "Informatics"
}

empty_dict = {}
another = dict(name="Bob", age=25)

#Keys must be immutable (str, int, tuple)
#Values can be any type (list, dict, int, etc.)

#Accessing values
print(student["name"])        # direct (error if key missing)
print(student.get("age"))     # safe access
print(student.get("grade"))   # None if not found
print(student.get("grade", "N/A"))  # default value

#Be careful of KeyError
#print(student["missing"])  # ERROR

#Adding / Updating values
student["age"] = 22          # update
student["grade"] = "A"       # add new
print(student)

#Removing elements
student.pop("age")           # removes and returns value
print(student)

del student["course"]        # delete key
print(student)

#student.clear()             # removes all items

#Dictionary length
print(len(student))

#Checking membership (checks KEYS only)
print("name" in student)     # True
print("Alice" in student)    # False

#Looping through dictionary
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

#Copying dictionary
a = {"x": 1, "y": 2}
b = a.copy()
print(b)

#Reference vs copy (IMPORTANT)
x = {"a": 1}
y = x
x["b"] = 2
print(y)  # y also changes (same reference)

#Nested dictionaries
users = {
    "user1": {"name": "Alice", "age": 21},
    "user2": {"name": "Bob", "age": 25}
}
print(users["user1"]["name"])

#COMMON Dictionary METHODS
data = {"a": 1, "b": 2, "c": 3}

print(data.keys())     # all keys
print(data.values())   # all values
print(data.items())    # key-value pairs

#Update dictionary
data.update({"d": 4, "a": 10})
print(data)

#Remove last inserted item (Python 3.7+)
data.popitem()
print(data)

#Set default (adds key if not exists)
data.setdefault("e", 5)
print(data)

#Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)

#Filtering with dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

#Merging dictionaries (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2
print(merged)

#Converting list to dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
new_dict = dict(zip(keys, values))
print(new_dict)


# =========================
# 🔑 EXAM NOTES (IMPORTANT)
# =========================

# 1. Dictionary Structure
# {key: value}
# Example: {"name": "Alice", "age": 21}

# 2. Rules
# - Keys must be immutable (str, int, tuple)
# - No duplicate keys allowed
# - Values can be any type

# 3. Access
# d[key] -> KeyError if missing
# d.get(key) -> safe (returns None or default)

# 4. Mutability
# - Dictionaries are mutable
# - You can add, update, delete items

# 5. Membership
# - 'in' checks KEYS only, not values

# =========================
# ⚠️ COMMON EXAM TRAPS
# =========================

# Duplicate keys overwrite
# {"a": 1, "a": 2} -> {"a": 2}

# Invalid key type (mutable)
# {[1,2]: "value"} -> ERROR

# Valid key
# {(1,2): "value"} -> OK

# KeyError
# d["missing"] -> ERROR

# Safe alternative
# d.get("missing") -> None

# =========================
# 🚀 EXAM PATTERNS
# =========================

# Count frequency
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# Swap keys and values
d = {"a": 1, "b": 2}
swapped = {v: k for k, v in d.items()}
print(swapped)

# Sort dictionary
d = {"b": 2, "a": 1}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)

# =========================
# 💡 WHEN TO USE DICTIONARIES
# =========================

# - Fast lookup (VERY IMPORTANT)
# - Key-value relationships
# - Examples:
#   - student records
#   - configurations
#   - counting data