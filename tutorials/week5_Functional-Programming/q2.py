from functools import reduce


def flattenA(lst):
    return [y for x in lst for y in x]


def flattenB(lst):
    return [] if len(lst) == 0 else lst[0] + flattenB(lst[1:])


def flattenC(lst):
    return list(reduce(lambda x, y: x + y, lst))


if __name__ == "__main__":
    lst = [[1, 2, 3], ['a', 'b', 'c'], [1.1, 2.1, 3.1]]
    print(flattenA(lst))
    print(flattenB(lst))
    print(flattenC(lst))
