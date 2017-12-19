i=2
n = 50
def is_prime(a):
    result = True 
    for i in range(2, a):
       if a%i == 0:
           result = False
    return result

for i in range(2,n):
    if(is_prime(i)):
        print(i)
    i = i + 1    