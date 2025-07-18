fact = (lambda f: (lambda n:1 if n==0 else n * f(f) (n-1))) (lambda f: (lambda n:1 if n==0 else n * f(f) (n-1)))
print(fact(4))