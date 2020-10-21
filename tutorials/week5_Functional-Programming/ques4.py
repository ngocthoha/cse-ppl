from functools import reduce

def compose1(*args):
    def compose(f, g):
        return lambda x: f(g(x))
    return reduce(compose, args, lambda x: x)

def identity(x):
    return x

def compose2(*args):
    if args:
        rest = compose2(*args[1:])
        return lambda x: args[0](rest(x))
    else:
        return identity

if __name__ == "__main__":
    def double(x): return 2 * x
    def increase(x): return x + 1
    def square(x): return x ** 2

    composedA1 = compose1(double, increase)
    composedA2 = compose1(square, increase, double)
    print(composedA1(3))
    print(composedA2(3))

    composedB1 = compose2(double, increase)
    composedB2 = compose2(square, increase, double)
    print(composedB1(3))
    print(composedB2(3))

