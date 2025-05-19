words = ["a","aba","ababa","aa"]
# Output: 4
c=0
for i in range(len(words)):
    if any(str(i) in x for x in words):
        c+=1
print(c)       
