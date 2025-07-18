from itertools import permutations

s = "aab"
unique_perms = set(permutations(s))

# Convert each tuple back to string
result = [''.join(p) for p in unique_perms]

# Optional: sort for consistent order
result.sort()

print(result)