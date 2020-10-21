def square(num):
    return num * num

def increase(num):
    return num + 1

def double(num):
    return num * 2

#Use recursive approach
def compose(*args):
    cps = compose(*args[:-1]) if len(args) > 2 else args[-2]
    return lambda num: cps(args[-1](num))

if __name__ == "__main__":
    print(compose(square, increase, double)(3))