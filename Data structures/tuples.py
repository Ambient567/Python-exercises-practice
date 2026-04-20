#Python Basics revision
#Tuples

#Creating tuples
numbers = (1, 2, 3, 4, 5)
tools = ("AI", "ML", "GenAI", "NLP")

#Single element tuple (IMPORTANT: needs comma)
single = (10,)
print(type(single))

#Without comma, it's not a tuple
not_tuple = (10)
print(type(not_tuple))

#Tuples are ordered, immutable (cannot change), and allow duplicates

#Accessing elements (Indexing)
items = ("apple", "banana", "cherry")
print(items[0])
print(items[1])
print(items[-1])

#Be careful of index out of bounds
print(items[10])  # throws error

#Use bounds checking
n = len(items)
print(items[n-1])

#Slicing
nums = (10, 20, 30, 40, 50, 60)
print(nums[0:3])
print(nums[:3])
print(nums[3:])
print(nums[-2:])
print(nums[0:10])  # no error
print(nums[0:6:2])  # step
print(nums[::-1])   # reverse tuple

#Tuples are immutable
t = (1, 2, 3)
# t[0] = 10  # ERROR: cannot modify tuple

#But you can reassign the whole tuple
t = (10, 20, 30)
print(t)

#Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)


#Repeating tuples
print(t1 * 3)

#COMMON Tuple METHODS (very limited)

nums = (1, 2, 3, 2, 4)
print(nums.count(2))  # count occurrences
print(nums.index(2))  # first occurrence

#Tuple length
print(len(nums))

#Checking membership
print(2 in nums)
print(10 not in nums)

#Looping through tuples
for item in ("AI", "ML", "NLP"):
    print(item)

#Tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c)

#Extended unpacking
a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]

#Swapping variables using tuples
x = 5
y = 10
x, y = y, x
print(x, y)

#Nested tuples
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[0][1])

#Converting between list and tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)

new_list = list(tup)
print(new_list)

#Tuples as dictionary keys (because they are immutable)
coords = {(1, 2): "Point A", (3, 4): "Point B"}
print(coords[(1, 2)])

#Why use tuples?
# - Faster than lists
# - Safe (cannot be changed)
# - Useful for fixed data (coordinates, configs)