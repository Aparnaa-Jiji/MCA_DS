import numpy as np
arr = np.array([[2,4,6,8],[1,3,5,7],[1,2,3,4],[5,6,7,8]])

# to display all elements excluding the first row
print(arr[1:])

#to display all elements excluding last row
print(arr[0:,0:3])

#to display all elements of 1st and 2nd column in 2nd and 3rd row
print(arr[1:3,0:2])

#to display the elements of 2nd and 3rd column
print(arr[0:,1:3])

# to display 2nd  and 3rd element of 1st row

print(arr[0:1,1:3])
