from functools import reduce


def composeA(*funcs):
    def foo(*args):
        return funcs[0](*args) if len(funcs) == 1 else funcs[0](composeA(*funcs[1:])(*args))
    return foo


def composeB(*funcs):
    def foo(*args):
        return reduce(lambda acc, func: func(acc), funcs[::-1], *args)
    return foo


if __name__ == "__main__":
    def double(x): return 2 * x
    def increase(x): return x + 1
    def square(x): return x ** 2

    composedA1 = composeA(double, increase)
    composedA2 = composeA(square, increase, double)
    print(composedA1(3))
    print(composedA2(3))

    composedB2 = composeB(square, increase, double)
    composedB1 = composeB(double, increase)
    print(composedB1(3))
    print(composedB2(3))
