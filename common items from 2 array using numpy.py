import numpy as np

a1 = np.array([1,2,3,4,5])
a2 = np.array([3,4,5,6,7])

same = np.intersect1d(a1,a2)

print("The First array is:",a1)

print("The Second array is:",a2)

print("The common element in both array is:",same)