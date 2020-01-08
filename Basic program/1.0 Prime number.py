# prime Number:

#Method 1:
def checkPrime(n):
    if (n <= 1):
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


#Method 2:
def checkPrime1(n):
    if n<=1:
        return False
    
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i+1
    return True


# Method 3: Best Method O(sq(n))
def checkPrime3(n):
    if n<=1:
        return False
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i = i+1
    return True
    
    
    

print(checkPrime(5))
print(checkPrime1(9))
print(checkPrime3(47))

for i in range(50):
    print(i,checkPrime3(i), "\n")


#SAMPLE pull req.

