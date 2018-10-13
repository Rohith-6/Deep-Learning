import numpy as np
# to create a structured data type
dt = np.dtype([('name',np.unicode_, 100), ('grades', np.float64, (2,))])
x = np.array([('sarah', (10.0,8.0)), ('Ram', (10.0,10.0))], dtype = dt)
print("Names are: ",x['name'])
print("Grades of sarah: ", x[0]['grades'])
