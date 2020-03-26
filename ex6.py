def is_prime(n):
    prime = True
    for i in range(2,n):
        if(n%i==0):
            prime=False
    if(n==1):
        prime=False
    return prime

