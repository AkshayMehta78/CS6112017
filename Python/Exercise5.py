result = 0
x = 11
while(result < 20):
	if( x%5 & x%7 & x%11):
		print ('Number found : ', x)
		result += 1
	x += 1	