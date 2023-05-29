def power(a,n=2):
    return a**n
    
    
def fib(N):
    F=[]
    a,b=0,1
    while len(F)<N:
        a,b=b,a+b
        F.append(a)
    return F