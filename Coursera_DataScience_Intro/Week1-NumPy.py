import numpy as np

numpyList = np.array([1, 2, 3])
print(numpyList)
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)
print(m.shape) # Number of rows and columns as a tuple
print(np.arange(0,20,2))  # Evenly spaced values within a given interval
print(np.linspace(0,10,9))  # 9 evenly spaced values from 0 to 10
print(m.reshape(1,6))  # Create a new array
print(m.resize(1,6))  # In-place
print(np.ones((3,2)) ) # an array of given size filled with ones

# Diagonal matrix
print(np.eye(3))  # A diagonal matrix of ones
print(np.diag(np.array([1,2,3])))

# Repeating list
print(np.array([1,2,3]*3))
print(np.repeat([1,2,3],3))

# Combine arrays
p = np.ones([2,3])
print(np.vstack([p, 2*p]))  # Row wise
print(np.hstack([p, 2*p]))  # Column wise

# Operations
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
print(x**2)
print(x.dot(y))  # Dot product
multiDim =  np.array([x,x**2])
print(multiDim.T)  # Matrix transpose
print(multiDim.dtype)
multiDim = multiDim.astype('f')
print(x.sum(), x.max(), x.mean(), x.std(), x.argmax())

print(multiDim[multiDim % 2 == 0])  # Select values
aCopy = x.copy()

# Iterate
test = np.random.randint(0, 10, (4,3))
print(test)
for row in test:
    print(row)
for i, row in enumerate(test):
    print('row', i, 'is', row)

# Iterate over multiple iterables
test2 = test**2
for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j)