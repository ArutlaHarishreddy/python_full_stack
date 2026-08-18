#Min Element
n=[2,6,78,1,66]
mini=n[0]
for num in n:
    if num<mini:
        mini=num
print(mini)

#another method
n=min(n)
print(n)