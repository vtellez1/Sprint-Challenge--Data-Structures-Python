import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
"""
Runtime of the starter code: O(n^2) 
Explanation: two nested loops, we have to run outer loop n times and inner loop for n times 
(n being length of list) so worse case scenario, we run n * n or n^2

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""
b = BinarySearchTree('names')
# Loop through names_1 list to add each name to tree
for name_1 in names_1:
    b.insert(name_1)
# Loop through names_2 to compare to tree and check for duplicates
# If duplicate name found, add the list
for name_2 in names_2:
    if b.contains(name_2):
        duplicates.append(name_2)

# Binary Search Trees typically have runtime of O(log(n))
# which is increasingly better than what we had before of O(n^2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
