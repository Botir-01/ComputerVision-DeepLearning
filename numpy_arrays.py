import numpy as np

mylist = [1,2,3]

# Turning a default Python array into numpy array
myarray = np.array(mylist)

# numpy version of a range
np.arange(0,10,2)

# creating two dimensional array with float(0)
np.zeros((10,5))

# creating two dimensional array with float(1)
np.ones(shape=(2,5))

# creating an array with 10 random numbers
np.random.seed(101)
arr = np.random.randint(0,100,10)
arr2 = np.random.randint(0,100,10)
print(arr)
print(arr2)

# finding a maximum value
arr.max()

# finding an index of a maximum value
arr.argmax()

# finding a minimum value
arr.min()

# finding an index of a minimum value
arr.argmin()

# finding the average value
arr.mean()

# reshaping an existing array
newArray = arr.reshape((2, 5))

# indexing
mat = np.arange(0, 100).reshape(10, 10)
row = 8
col = 5
here = mat[row, col]

# slicing
newArrRow = mat[:, 1]
newArrCol = mat[1, :]

# grabbing a chunk of data
chunk = mat[0:3, 0:3] # = 0 reassignment

# copying a metric
newMat = mat.copy()


