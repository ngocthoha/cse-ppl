from abc import ABC, abstractmethod

class Visitor(ABC):
    def visit(self, exp):
        if exp.type == "IntLit":
            return self.visitIntLit(exp)
        elif exp.type == "FloatLit":
            return self.visitFloatLit(exp)
        elif exp.type == "UnExp":
            return self.visitUnExp(exp)
        elif exp.type == "BinExp":
            return self.visitBinExp(exp)

    def visitIntLit(self, exp):
        pass
    def visitFloatLit(self, exp):
        pass
    def visitUnExp(self, exp):
        pass
    def visitBinExp(self, exp):
        pass

class Exp(ABC):
    def accept(self, visitor):
        return visitor.visit(self)

# Expression

class IntLit(Exp):
    def __init__(self, value):
        self.value = value
        self.type = "IntLit"

class FloatLit(Exp):
    def __init__(self, value):
        self.value = value
        self.type = "FloatLit"

class UnExp(Exp):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg
        self.type = "UnExp"

class BinExp(Exp):
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right
        self.type = "BinExp"

# Visitor
class Eval(Visitor):
    def visitIntLit(self, exp):
        return exp.value

    def visitFloatLit(self, exp):
        return exp.value

    def visitUnExp(self, exp):
        if exp.op == "+":
            return self.visit(exp.arg)
        elif exp.op == "-":
            return -self.visit(exp.arg)

    def visitBinExp(self, exp):
        if exp.op == "+":
            return self.visit(exp.left) + self.visit(exp.right)
        elif exp.op == "-":
            return self.visit(exp.left) - self.visit(exp.right)
        elif exp.op == "*":
            return self.visit(exp.left) * self.visit(exp.right)
        elif exp.op == "/":
            return self.visit(exp.left) / self.visit(exp.right)
        

class PrintPrefix(Visitor):
    def visitIntLit(self, exp):
        return str(exp.value) + " "

    def visitFloatLit(self, exp):
        return str(exp.value) + " "

    def visitUnExp(self, exp):
        return exp.op + ". " + self.visit(exp.arg)

    def visitBinExp(self, exp):
        return exp.op + " " + self.visit(exp.left) + self.visit(exp.right)

class PrintPostfix(Visitor):
    def visitIntLit(self, exp):
        return str(exp.value) + " "

    def visitFloatLit(self, exp):
        return str(exp.value) + " "

    def visitUnExp(self, exp):
        return self.visit(exp.arg) + exp.op + ". "

    def visitBinExp(self, exp):
        return self.visit(exp.left) + self.visit(exp.right) + exp.op + " "

if __name__ == "__main__":
    x = BinExp(IntLit(3), "+", BinExp(IntLit(4), "*", FloatLit(2.0)))
    print(x.accept(Eval()))

    x = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*", IntLit(2)))
    print(x.accept(PrintPrefix()))
    print(x.accept(PrintPostfix()))