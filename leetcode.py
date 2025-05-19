firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
res1=''
res2=''
res3=''
# Output: true
for i in firstWord:
    if i=='a':
        res1=res1+'0'
    if i=='b':
        res1=res1+'1'
    if i=='c':
        res1=res1+'2'
for i in secondWord:
    if i=='a':
        res2=res2+'0'
    if i=='b':
        res2=res2+'1'
    if i=='c':
        res2=res2+'2'
for i in targetWord:
    if i=='a':
        res3=res3+'0'
    if i=='b':
        res3=res3+'1'
    if i=='c':
        res3=res3+'2'
print(res3)        
# print(int(res1)+int(res2)==int(res3))        
       


