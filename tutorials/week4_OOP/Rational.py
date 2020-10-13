class Rational:
    #greatest common divisor
    def  gcd(self, n, d):
        if d == 0:
            return n
        else:
            return self.gcd(d, n % d)
    #constructor
    def __init__(self, number = 0, demon = 1):
        if demon == 0:
            print("demon must not be zero!")
        else:
            common = self.gcd(number, demon)
            self.number = number // common
            self.demon = demon // common
    #override add operator
    def __add__(self, other):
        if isinstance(other, int):
            return self + Rational(other)
        else:
            common = self.gcd(self.number, self.demon)
            _number = self.number * other.demon + other.number * self.demon
            _demon = self.demon * other.demon
            return Rational(_number, _demon)
    #override string convert method
    def __str__(self):
        return str(self.number) + "/" + str(self.demon)
