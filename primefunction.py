def prime(x,y):
    for i in range(x,y):
        if all(i%p for p in range(2,9)):
            prime=i
            print(prime)



primeNo=prime(10,30)
print(primeNo)