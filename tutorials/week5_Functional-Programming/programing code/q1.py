from functools import reduce
#q1 comprehension
def lessThan1(lst, n):
    return [x for x in lst if x < n]

#q2 high-order function
def lessThan2(lst, n):
    return list(filter(lambda x: x < n, lst))

#q3 recursive
def lstSquare1(n:int):
    return[1] if n == 1 else lstSquare1(n - 1) + [n * n]


#q4 comprehension
def lstSquare2(n:int):
    return [x * x for x in range(1, n+1)]

#q5 recursive
def flatten1(lst):
    return [] if len(lst) == 0 else lst[0] + flatten1(lst[1:])

#q6 high-order function
def flatten2(lst):
    return reduce(lambda x, y: x + y, lst, [])

#q7 recursive
def dist1(lst, n):
    return [] if len(lst) == 0 else [(lst[0], n)] + dist1(lst[1:], n)

#q8 high-order function
def dist2(lst, n):
    return list(map(lambda x: (x, n), lst))

#q9
def powGen(x):
    def makePower(exp):
        return pow(exp, x)
    return makePower

#q10
def increase(num):
    return num + 1

def square(num):
    return num * num

def compose(*args):
    cps = compose(*args[:-1]) if len(args) > 2 else args[-2]
    return lambda num: cps(args[-1](num))

def compose2(*args):
    def foo(x):
        return reduce(lambda acc, func: func(acc), args[::-1], x)
    return foo
def f(x):
    return lambda y: y**x

if __name__ == "__main__":
    n = 4
    lst = [1,2,3]
    squa = f(3)

    print(squa(2))