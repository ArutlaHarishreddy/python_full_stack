for over in range(1,20):
    for balls in range(1,7):
        print("overs:",over,".",balls)

#using break for loop
print("Here we using break statement") #it stops the loop from the condition
for j in range(1,6):
    if j==3:
        break
    print(j)


#using continue for loop
print("Here we using continue statement")  #it breaks only one iteration which we mentioned
for k in range(1,6):
    if k==3:
        continue
    print(k)


#using pass for loop
print("Here we using pass statement")
for l in range(1,6):
    if l==3:
        pass
    print(l)