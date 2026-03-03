# Number of elements in set A
n = int(input())

# Set A
A = set(map(int, input().split()))

# Number of other sets
N = int(input())

for _ in range(N):
    operation, length = input().split()
    other_set = set(map(int, input().split()))
    
    if operation == "update":
        A.update(other_set)
    elif operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

# Print sum of final set A
print(sum(A))