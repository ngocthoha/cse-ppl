from abc import ABC, abstractmethod

class Exp(ABC):
    def eval(self):
        pass
    def printPrefix(self):
        pass

class IntLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value) + " "

class FloatLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value) + " "

class UnExp(Exp):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def eval(self):
        if self.op == "+":
            return self.arg.eval()
        elif self.op == "-":
            return -self.arg.eval()
    def printPrefix(self):
        return self.op + ". " + self.arg.printPrefix()
        
class BinExp(Exp):
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right

    def eval(self):
        if self.op == "+":
            return self.left.eval() + self.right.eval()
        elif self.op == "-":
            return self.left.eval() - self.right.eval()
        elif self.op == "*":
            return self.left.eval() * self.right.eval()
        elif self.op == "/":
            return self.left.eval() / self.right.eval()
    def printPrefix(self):
        return self.op + " " + self.left.printPrefix() + self.right.printPrefix()


if __name__ == "__main__":
    x = BinExp("+", IntLit(3), BinExp("*", IntLit(4), FloatLit(2.0)))
    print(x.eval())
    x = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*", IntLit(2)))
    print(x.printPrefix())