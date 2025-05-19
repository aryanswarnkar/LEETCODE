words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
def vovels(s):
    if s[0] in "aeiou" and s[-1] in "aeiou":
        return True
    else:
        False
arr=[]        
for i in queries:
    a,b=i
    c=0
    for j in range(a-1,b):
        if vovels(words[j]):
            c+=1
    arr.append(c)

print(arr)



