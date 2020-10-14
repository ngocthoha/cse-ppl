from abc import ABC
from dataclasses import dataclass

class Expr(ABC):
    def eval(self):
        pass

@dataclass
class Var(Expr):
    name: str
    def eval(self):
        return Number(1)

@dataclass
class Number(Expr):
    num: float
    def print(self):
        print(self.num)
    def eval(self):
        return Number(self.num)

@dataclass
class UnOp(Expr):
    operator: str
    arg: Expr
    def eval(self):
        if self.operator == "+":
            return Number(self.arg.eval().num)
        elif self.operator == "-":
            return Number(-self.arg.eval().num)

@dataclass
class BinOp(Expr):
    operator: str
    left: Expr
    right: Expr
    def eval(self):
        if self.operator == "+":
            return Number(self.left.eval().num + self.right.eval().num)
        elif self.operator == "-":
            return Number(self.left.eval().num - self.right.eval().num)
        elif self.operator == "*":
            return Number(self.left.eval().num * self.right.eval().num)
        elif self.operator == "/":
            return Number(self.left.eval().num / self.right.eval().num)

if __name__ == "__main__":
    t = BinOp("*", BinOp("+", Var("x"), Number(0.2)), Number(3))
    t.eval().print()
