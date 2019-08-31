# challenge:
#   handles 0
#   handles negative values
class Frac:
    _n = 1
    _d = 1
    def __init__(self, n, d):
        self._n = n
        self._d = d
        self._simplify()
        
    def _simplify(self):
        import math
        gcd = math.gcd(self._n, self._d)
        self._n //= gcd
        self._d //= gcd
        
    def __str__(self):
        return f'{self._n}/{self._d}'
    
    def invert(self):
        #tmp = self._n
        #self._n = self._d
        #self._d = tmp
        self._n, self._d = self._d, self._n
    
    def multi(self, f):
        self._n *= f._n
        self._d *= f._d
        self._simplify()
        
    def add(self, f):
        # a/b + c/d = (ad+bc)/bd
        self._n = self._n*f._d + self._d*f._n
        self._d = self._d * f._d
        self._simplify()
        
    def eval(self):
        return self._n / self._d
    
f1 = Frac(2, 3)
print(f1)
f1.invert()
print(f1)

f2 = Frac(1, 3)
f1.multi(f2)
print(f1)

f1.add(f2)
print(f1)

print(f1.eval())




