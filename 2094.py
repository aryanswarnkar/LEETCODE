digits = [2,1,3,0]
digits.sort()
arr=()
# Output: [102,120,130,132,210,230,302,310,312,320]
for i in range(len(digits)):
    for j in range(i+1,len(digits)):
        for k in range(j,len(digits)):
            if int(str(digits[i])+str(digits[j])+str(digits[k]))%2==0:
                arr.append(int(str(digits[i])+str(digits[j])+str(digits[k])))
print(arr)


digits=[2,1,3,0]
