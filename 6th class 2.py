import numpy as np

arr = np.array([
    [5, 4, 3, 1],
    [7, 3, 9, 3],
    [6, 4, 2, 4]
])
print(arr, arr.shape)
# print(arr[:2])

s_arr = arr[:2, 1:3]
print(s_arr)
print(s_arr.shape)

#Questions ???........
# Extract last row and col 0, col 1
# Extract second row
# Extract 3rd column
# Extract col 1, col 2

print(arr)

print("Otuput of question")
print("\nExtract last row and col 0, col 1\n",arr[-1, :2])

print("\nExtract second row\n", arr[-2, :])

print("\nExtract 3rd column\n", arr[:, 2:3])

print("\nExtract col 1, col 2\n", arr[:, 1:3])


print("____________")
print(arr)
bool_idx = [arr > 3]
print(bool_idx)

print(arr[arr > 3])

x = np.array([
    [2, 4],
    [5, 3]
])
print(x)
y = np.array([
    [6, 7],
    [3, 5]
])
print(y)
# print(x + y)
# print(np.add(x, y))
# print(np.subtract(x, y))
# print(np.multiply(x, y))
# print(np.divide(x, y))
# print(np.square(x))
# print(np.sqrt(x))

v = np.array([4, 5])
w = np.array([3, 6])

print(v.dot(w)) #dot product of two array
print(np.dot(v, w)) #another method to find dot product

print(x.dot(w))
print(np.dot(x, w))

print(x.dot(y))
print(np.dot(x, y))

print(x)
print(x.T) # Transopose of matrix

u = np.array([
    [3, 0, 5],
    [6, 7, 3],
    [6, 8, 4]
])
print(u)
print(u.T)


print("Sum of all elements of u:", np.sum(u))
print("Sum of all each col of u:", np.sum(u, axis=0))
print("Sum of all row col of u:", np.sum(u, axis=1))

x = np.array([
    [3, 4, 5],
    [2, 6, 3],
    [8, 4, 1]
])

v = np.array([1, 0, 1])

# For loop route
y = np.empty_like(x) # Empty array like x array
print(y)

# Adding v vector in x vector using for loop
for i in range(len(x)):
    y[i, :] = x[i, :] + v

print(x)
print(y)

# Mathematical Approch

stacked_v = np.tile(v, (3, 1)) #Brodcasting

print(stacked_v)

print(x + stacked_v)

print(x + v)

# Reshaping
x = np.array([1, 2, 3])
print(np.reshape(x, (3, 1)))

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(x)
print(np.reshape(x, (3, 2)))