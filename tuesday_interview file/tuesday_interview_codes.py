#Write a function to generate all unique permutations of a given string or list of numbers using recursion.
def unique_permutations(s):
    if len(s)<=1:
        return [s]
    result=set()
    for i in range(len(s)):
        current=s[i]
        remaining=s[:i]+s[i+1:]

        for p in unique_permutations(remaining):
            result.add(tuple([current]+p))
    return [list(p) for p in result]
s=[1,2,2,3]
for p in unique_permutations(s):
    print(p)

str="AAB"
for p in unique_permutations(list(str)):
    print(p)


