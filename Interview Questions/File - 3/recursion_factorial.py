#17. Implement a recursive function to calculate factorial.
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))