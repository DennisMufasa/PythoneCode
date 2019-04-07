"""Printing prime numbers,
all() returns true if all elements in a loop are true"""
for i in range(20,50):
    if all(i%p for p in range(2,9)):
        print(i)