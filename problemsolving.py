import math
def is_perfect(n):
    s = math.sqrt(n)
    s = int(s)
    if s*s == n:
        return True
    else:
        return False

def is_fibo(n):
    if is_perfect(5*n*n+4) or is_perfect(5*n*n+4):
        print ("%d is a faibonacci series" %n)

    else:
        print ("%d is not a faibonacci series" %n)

a = int(input("enter the number:\n"))
is_fibo(a)
