#Find all numbers between 1 and 100 divisible by both 3 and 5.
num=100
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print(i)


