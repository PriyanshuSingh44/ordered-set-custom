# test_ordered_set.py

from ordered_utils import ordered_set

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
unique_fruits = ordered_set(data)

print("Original:", data)
print("Ordered Set:", unique_fruits)
