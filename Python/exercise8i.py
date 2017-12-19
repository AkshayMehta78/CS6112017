def set_first_elem_to_zero(n):
	n[0]=0
	return n

list1 = [4 ,5 , 6]
z=set_first_elem_to_zero(list1)
print (z)
print (list1) #Orignal list also changes
