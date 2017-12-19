a = [5 , 6 , 9]
print("List a",a)

b = a 
print("List b",b)

b[1] = 22
print("List b",b)
print("List a",a)

c = a [:]
c[2] = 55
print("List c",c)
print("List a",a)