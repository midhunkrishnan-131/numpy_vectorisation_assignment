import numpy as np

a = np.array([1, 2, 3, 4, 5])

b = a[1:4]
b[0] = 99
print("After changing the slice view:", a)

c = a[[0, 2, 4]]
c[0] = -1
print("After changing the fancy-indexing copy:", a)

# Explanation:
# Basic slicing creates a view, so changing b also changes a.
# Fancy indexing creates a copy, so changing c does not change a.
