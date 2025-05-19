gifts =[25,64,9,4,100]
k=4
# Output: 29
while k!=0:
    gifts.sort()
    gifts[len(gifts)-1]=int((max(gifts)**0.5)//1)
    k=k-1
print(sum(gifts))    