class Exp():
    def __init__(self, exp):
        self.exp = exp
    def eval(self):
        return self.exp.eval()
    def printPrefix(self):
        pass
class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.left = left
        self.right= right
        self.operator = operator
    def eval(self):
        if self.operator == '-':
            return self.left.eval() - self.right.eval()
        if self.operator == '+':
            return self.left.eval() + self.right.eval()
        if self.operator == '*':
            return self.left.eval() * self.right.eval()
        if self.operator == '/':
            return self.left.eval() / self.right.eval()
    def printPrefix(self):
        return self.operator + " " + self.left.printPrefix() + self.right.printPrefix()
class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
    def eval(self):
        if self.operator == '-':
            return -self.operand.eval()
        elif self.operator == '+':
            return self.operand.eval()
    def printPrefix(self):
        return self.operator + ". " + self.operand.printPrefix()
        
class IntLit(UnExp):
    def __init__(self, val):
        self.value = val
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value) + " "
class FloatLit(UnExp):
    def __init__(self, val):
        self.value = val
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value) + " "

if __name__ == "__main__":
    t = Exp(
        BinExp(
            UnExp("-", IntLit(4)), "+", BinExp(
                IntLit(3), "*", IntLit(2)
            )
        )
    )
    print(t.eval())