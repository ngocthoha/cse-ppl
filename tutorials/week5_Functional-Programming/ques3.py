from functools import reduce
#Use comprehension
def lessThanA(n, lst):
    return [x for x in lst if x < n]

#Use recursive
def lessThanB(n, lst):
    return [] if len(lst) == 0 else (([lst[0]] if lst[0] < n else []) + lessThanB(n, lst[1:]))

#Use high-order function
def lessThanC(n, lst):
    return list(filter(lambda x: x < n, lst))

def lessThanD(n, lst):
    return reduce(lambda x,y: x + [y] if y < n else x, lst)

if __name__ == "__main__":
    lst = [1,2,3,4,5]
    n = 4
    print(lessThanA(n, lst))
    print(lessThanB(n, lst))
    print(lessThanC(n, lst))
    print(lessThanD(n, lst))
