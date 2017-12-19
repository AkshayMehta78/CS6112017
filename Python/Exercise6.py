def is_prime(a):
    result = True 
    for i in range(2, a):
       if a%i == 0:
           result = False
    return result
print(is_prime(13))

    
    
    