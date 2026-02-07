import math

def factorial_large(n):
    val = math.factorial(n)
    return [int(d) for d in str(val)]


n = 5
print("Factorial Digits:", factorial_large(n))