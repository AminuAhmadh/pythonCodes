def factorial(n: int):
    fact = 1
    for factor in range (n, 1,- 1):
        fact *= factor
    print ("The factorial of", n, "is", fact)



factorial(8)
