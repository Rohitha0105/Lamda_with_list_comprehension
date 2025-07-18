nums = [11,22,33,44,55,66,77,88]
e = list(filter(lambda num: num%2 == 0, nums))
print(e)

nums = [11,22,33,44,55,66,77,88]
e = list(filter(lambda num: num%2 != 0, nums))
print(e)

nums = [11,22,33,44,55,66,77,88]
e = list(map(lambda num: num%2 == 0, nums))
print(e)

nums = [11,22,33,44,55,66,77,88]
e = list(map(lambda num: num%2 != 0, nums))
print(e)