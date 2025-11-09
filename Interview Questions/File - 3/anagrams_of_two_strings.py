#Implement a function to check if two strings are anagrams
text1="listen"
text2="silent"
is_anagram=True
if len(text1) != len(text2):
    print("Not Anagram")
else:
    for i in text1:
        if i not in text2:
            is_anagram=False
            break
    else:
        is_anagram=True

if is_anagram:
    print("Anagram")
else:
    print("Not anagram")


#method-2
from collections import Counter
def anagram(text1,text2):
    return Counter(text1.lower().replace(" "," ")) == Counter(text2.lower().replace(" "," "))

text1="silent"
text2="listen"

print(anagram(text1,text2))#
        