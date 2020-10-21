from functools import reduce
#Use comprehension
def flattenA(lst):
    return [x for y in lst for x in y]

#Use recursive
def flattenB(lst):
    return [] if len(lst) == 0 else lst[0] + flattenB(lst[1:])

#Use high-order function
def flattenC(lst):
    return reduce(lambda x, y : x + y, lst, [])

if __name__ == "__main__":
    lst = [[1,2,3],['a','b','c']]
    print(flattenA(lst))
    print(flattenB(lst))
    print(flattenC(lst))