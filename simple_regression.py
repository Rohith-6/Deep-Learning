import numpy as np
from numpy import pi
a = np.array([[1,2,3,4],[4,5,6,7]])
print(a.ndim) #Number of rows
print(a.shape) #(Number of rows, No.of elements in each row"columns")
print(a.size) # Product of elements of shape.
print(a.dtype)
print(a.dtype.name)
print(a.itemsize)
print(np.arange(0,12))
print(np.empty((2,2), dtype = "float32"))
print()
#Linespace operation.
x = np.linspace(0, 2*pi, 100)
f = np.sin(x)

#zero_like and ones_like in numpy array
z = np.arange(6)
z = z.reshape((2,3))
print(z)
print()
y_zeros = np.zeros_like(z)
y_ones = np.ones_like(z)
print(y_ones)
print(y_zeros)
print()

#np.random.rand
print(np.random.rand(2,2))
print()
# a random 2x2 matrix from N(0,1)
print(np.random.randn(2,2))
print()
# To create a random 2x2 matrix for N(mu, sigma**2)
# Use the following sigma*np.random.randn() = mu
# example for 2x2 matrix values form N(3,6.25)
rand_norm = 2.5 * np.random.randn(2,2)+ 3
print(rand_norm)
print()

#np.fromfunction
# Deals with the coordinates.
#Construct an array by executing a function over each coordinate.
#The resulting array therefore has a value fn(x, y, z) 
#at coordinate (x, y, z).
func = lambda i,j:i==j
func2 = lambda i,j:i+j
print(np.fromfunction(func, (3,3), dtype = int))
print()
print(np.fromfunction(func2, (3,3), dtype = int))
print()