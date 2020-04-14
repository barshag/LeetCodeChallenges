import math

def sortfirst(val): 
    return val[0]  

points = [[1,3],[-2,2]]
K = 1
retList =[]

for point in points:
    retList.append ([math.sqrt(point[0]**2+point[1]**2), point])

retList.sort(key =sortfirst)
print (retList[:K])
    
