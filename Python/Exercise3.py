x=float(123)
print(x)	#123.0	

x=float('123')
print(x)	#123.0

x=float('123.23')
print(x)	#123.23

x=int(123.23)
print(x)	#123

#x=int('123.23')
#print(x)	ValueError: invalid literal for int() with base 10: '123.23'

x=int(float('123.23'))
print(x)	#123

x=str(12)
print(x)	#12

x=str(12.2)
print(x)	#12.2

x=bool('a')
print(x)	#True

x=bool(0)
print(x)	#False

x=bool(0.1)
print(x)	#True