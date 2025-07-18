word = ["hi"," ","students"," ","bye"]
a = [s for s in word if(lambda x:x != " ")(s)]
print(a)