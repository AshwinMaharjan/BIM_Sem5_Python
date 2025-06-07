# Function to perform set operations
def set_operations(set1, set2):
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)
    difference_result = set1.difference(set2)
    
    return union_result, intersection_result, difference_result

# Read sets from the user
set1_input = input("Enter elements of the first set separated by spaces: ").split()
set2_input = input("Enter elements of the second set separated by spaces: ").split()

# Convert input strings to sets
set1 = set(set1_input)
set2 = set(set2_input)

# Perform set operations
union_result, intersection_result, difference_result = set_operations(set1, set2)

# Display the results
print("\nSet Operations Results:")
print(f"Union of sets: {union_result}")
print(f"Intersection of sets: {intersection_result}")
print(f"Difference of sets (set1 - set2): {difference_result}")
