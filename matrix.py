__author__ = 'DELL'
#import numpy
X=[[1,2,3],[4,5,6]]
Y=[[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)

