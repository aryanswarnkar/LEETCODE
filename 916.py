words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
res=""
k=[]
for i in words2:
    res+=i
for i in words1:
    if res in i:
        k.append(i)
print(k)        