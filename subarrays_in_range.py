def get_subarray(A, B, C):
    return A[B:C+1]

# Get input from the user
A = list(map(int, input("Enter the elements of array A: ").split()))
B = int(input("Enter the starting index B: "))
C = int(input("Enter the ending index C: "))

output = get_subarray(A, B, C)
print("Subarray from index B to C:", output)