prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
answer=[]
for i in range(1,len(prices)):
    if prices[i-1]>=prices[i]:
        answer.append(prices[i-1]-prices[i])
    else:
        answer.append(prices[i])
print(answer)            