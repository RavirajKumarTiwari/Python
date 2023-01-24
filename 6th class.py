import numpy as np

arr = np.array(
    [1, 2, 4]
)

print(arr, type(arr))
print("Shape of the array is ",arr.shape)
print(arr[2])

print("---2D array---\n")

arr2D = np.array([
    [2, 3],
    [5, 6],
    [7, 8]
])

print(arr2D, arr2D.shape)
print(arr2D[0, 0], arr2D[0, 1]) #accessing element of array 

arr2D[0] = [20, 30]
print(arr2D)

zeros = np.zeros((4, 5))
print(zeros)

ones = np.ones((3,))
print(ones)
print(zeros.dtype)

consts = np.full((3, 3), 9)
print(consts)

rand = np.random.random((4, 4))
print(rand)

# print("---3D array---\n")

# arr3D = np.array([
#     [
#         [2, 3],
#         [5, 6],
#         [7, 8]
#     ],
#     [
#         [2, 3],
#         [5, 6],
#         [7, 8]
#     ],
#     [
#         [2, 3],
#         [5, 6],
#         [7, 8]
#     ]
# ])
# print("print the 3D array:\n",arr3D)

# print("\nelements of 3D array\n")
# print(arr3D[0])
# print(arr3D[0, 0])
# print(arr3D[0, 0, 0])