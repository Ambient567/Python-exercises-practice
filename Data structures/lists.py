#Lists Basics revision

#Creating lists
numbers = [1, 2, 3, 4, 5]
tools = ["AI", "ML", "GenAI", "NLP"]
mixed = [1, "AI", True, 3.5]

#Lists are ordered, mutable (can change), and allow duplicates

#Accessing elements (Indexing)
items = ["apple", "banana", "cherry"]
print(items[0])
print(items[1])
print(items[-1])  # last element

#Be careful of index out of bounds
print(items[10])  # throws error

#Use bounds checking
n = len(items)
print(items[n-1])

#Modifying elements
items[1] = "orange"
print(items)

#List Concatenation
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)

#Repeating lists
print(list1 * 3)  # [1, 2, 1, 2, 1, 2]

#Slicing
nums = [10, 20, 30, 40, 50, 60]
print(nums[0:3])
print(nums[:3])
print(nums[3:])
print(nums[-2:])
print(nums[0:10])  # no error
print(nums[0:6:2])  # step
print(nums[::-1])   # reverse list

#COMMON List METHODS

#Adding elements
fruits = ["apple", "banana"]
fruits.append("cherry")   # adds to end
print(fruits)

fruits.insert(1, "orange")  # insert at index
print(fruits)

#Extending list
more_fruits = ["grape", "melon"]
fruits.extend(more_fruits)
print(fruits)

#Removing elements
fruits.remove("banana")  # removes first match
print(fruits)

popped = fruits.pop()  # removes last element
print(popped)
print(fruits)

del fruits[0]  # delete by index
print(fruits)

#Clearing list
fruits.clear()
print(fruits)

#Searching
nums = [1, 2, 3, 2, 4]
print(nums.index(2))  # first occurrence
print(nums.count(2))  # count occurrences

#Sorting
nums.sort()  # ascending
print(nums)

nums.sort(reverse=True)
print(nums)

#Reverse list
nums.reverse()
print(nums)

#Copying lists
a = [1, 2, 3]
b = a.copy()
print(b)

#Important: reference vs copy
x = [1, 2, 3]
y = x
x.append(4)
print(y)  # y also changes (same reference)

#List length
print(len(nums))

#Checking membership
print(2 in nums)
print(10 not in nums)

#Looping through lists
for item in ["AI", "ML", "NLP"]:
    print(item)

#List comprehension (short way to create lists)
squares = [x**2 for x in range(5)]
print(squares)

#Filtering with list comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

#Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[0][1])  # access inner element

#Unpacking lists
a, b, c = [10, 20, 30]
print(a, b, c)

#List as stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())

#List as queue (basic)
queue = []
queue.append(1)
queue.append(2)
print(queue.pop(0))  # removes first element (slow for large lists)
