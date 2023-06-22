#  Write a python program to get a list sorted in increasing order by 
# the last elements in a each tuple from agiven list of non empty tuples.

a = [(2,5),(1,2),(4,4),(2,3),(2,1)]
def last(x1):
    return x1[-1]

def sort(x2):
    return sorted(x2,key=last)
print("sorted :",sort(a))









 