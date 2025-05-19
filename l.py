def even_list(nums):
    even=[]
    for i in range(len(nums)):
        if nums[i]%2==0:
            even.append(nums[i])
    return even

def max_min_tuple(k):
    maxi=max(k)
    mini=min(k)
    return maxi,mini


def count(s):
    freq={}
    for c in s:
        if c in freq:
            freq[c]+=1
        else:
            freq[c]=1
    return freq

def finding(a,b):
    return a|b,a&b,a - b,a ^ b

def conversion(tup):
    return dict(tup)
            


