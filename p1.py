li = [10,"hi",4.5,"students",3,100]
i = [x for x in li if(lambda v:type(v) == int)(x)]
print(i)