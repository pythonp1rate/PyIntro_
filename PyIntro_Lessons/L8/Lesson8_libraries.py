# In this file, we will write a program
# that plots some data
# For this we will use an external 
# package/library called matplotlib

# we use import to import libraries
# For matplotlib in particular, 
# we want to use the pyplot module specifically
import matplotlib.pyplot as plt

x = [-4, -2 , 0, 2, 4]
y = [16, 4, 0, 4, 16]

plt.plot(x, y)
plt.show()