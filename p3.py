dsum = (lambda f: lambda n:0 if n==0 else n %10 +f(f)(n//10)) (lambda f: lambda n:0 if n==0 else n %10 +f(f)(n//10))
print(dsum(1234))