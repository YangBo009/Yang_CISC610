def factorial(n):
    num = 1
    if n<1:
        print "the number is less than 1"
    else:
        while n >= 1:
            num = num * n
            n = n - 1
        return num

print factorial(6)

