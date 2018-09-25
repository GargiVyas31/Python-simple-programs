__author__ = 'DELL'
set1 = set(["a","b","c"])
#ADDITION
set1.add("d")
set2= frozenset(["e","f"])
#set2.add("g") thisives an error

set3 = set([1,2,3,"a"])
print("Union ",set1.union(set3))
print("Intersection",set1.intersection(set3))
print("Difference ",set1.difference(set3))
print(set3)
set3.clear()
print(set3)