#Use list comprehension approach
def doubleA(lst):
    return [ele * 2 for ele in lst]

#Use recursive approach
def doubleB(lst):
    return [] if len(lst) == 0 else [lst[0] * 2] + doubleB(lst[1:])

#Use high-order function approach
def doubleC(lst):
    return list(map(lambda x: x * 2, lst))

if __name__ == "__main__":
    lst = [1,2,3]
    print(doubleA(lst))
    print(doubleB(lst))
    print(doubleC(lst))