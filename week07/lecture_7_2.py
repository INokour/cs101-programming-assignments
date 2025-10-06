# Practice 1
colors = []
colors.append("red")
print(colors)
colors.append("blue")
print(colors)
colors.append("green")
print(colors)

# Practice 2
# Start with this list:
numbers = [10, 30, 40]

numbers.insert(1, "20")
print(numbers)
numbers.insert(0, "5")
print(numbers)
numbers.insert(len(numbers), "50")
print(numbers)

# Practice 3
sorted_list = [15, 25, 35, 45]

sorted_list.insert(2, 30)
sorted_list.insert(0, 10)
sorted_list.insert(len(sorted_list), 50)
print(sorted_list)

# Example 1
fruits = ["apple", "banana"]
# Use extend() to add:
fruits.extend(["orange", "grape"])
print(fruits)

numbers = [1, 2]
numbers.extend([3, 4, 5])
print(numbers)

# Example 2
# Predict the output, then test: 
# Case 1:
list1 = [1, 2]
list1.append([3, 4])
# What is list1 now? 1,2,[3, 4]
print(list1)
# Case 2:
list2 = [1, 2]
list2.extend([3, 4])
# What is list2 now? 1,2,3,4
print(list2)
# Case 3:
list3 = ['a']
list3.extend('bc')
# What is list3 now? a, bc
print(list3)

# Example 3
# You have three sources of data:
morning_temps = [65, 68, 70]
afternoon_temps = [75, 78]
evening_temps = [72, 70, 68]
all_temps = []

for temps in [morning_temps, evening_temps, afternoon_temps]:
    all_temps.extend(temps)

print(all_temps)


# Exercise 1
# Start with:
animals = ["cat", "dog", "bird", "dog", "fish"]

animals.remove("bird")
print(animals)
animals.pop()
print(animals)
del animals[0]
print(animals)

# Exercise 2
# Start with:
queue = ["Alice", "Bob", "Charlie", "David", "Eve"]
queue.remove("David")
print(f"Serving: {queue[1]}") 
del queue[1]
queue.pop()
print(queue)

# Excercise 3
data = [10, 20, 30, 40, 50]
to_remove = 25 # Not in list!

if to_remove in data:
    queue.remove(to_remove)
if len(data) >= 10:
    queue.pop(10)

print(queue)

del queue[len(queue) // 2]
print(queue)
del queue[1:len(queue)-1]
print(queue)

# Write code to:
# 1. Safely try to remove 'to_remove' (check first)
# 2. Safely pop index 10 (check bounds first)
# 3. Delete the middle element (calculate middle index)
# 4. Clear all but first and last elements using del with slice