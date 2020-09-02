#just import numpy library
import numpy as np
def determinant(matrix):
    #your code here
    b=np.array(matrix)
    #round up number up or down
    c=round(np.linalg.det(b))
    print(c)
    return c

c=int(input("Enter m size of matrix"))
a=int(input("Enter n size of matrix"))
d=[]

if a==c:
    for j in range(c):
        d.append([])
        for i in range(a):
            b=int(input("Enter Value of I:"))
            d[j].append(b)
else:
    print("nah how tf do ya find determinant of a matrix if m and n ain't the same ya wanker")
print(d)
e=determinant(d)
print(e)
