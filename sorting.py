# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first +second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)
sort_again = sorted(full)

# Print out full_sorted
print("This list is sorted in ascending order", sort_again)
print("This list is sorted in descending order", full_sorted)