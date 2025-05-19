# ini="aaaa"
# sub="aa"
# count=0
# n=len(ini)
# m=len(sub)
# for i in range(n-m+1):
#     if ini[i:i+m]==sub:
#         count+=1
# print(count)       
#all pssible substrings
def print_substrings(s):
    n = len(s)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Collect the substring from index i to j
            result.append(s[i:j])
    
    # Sort substrings by length in reverse order
    result.sort(key=len, reverse=True)
    return result

# Single test case
s = "abc"
substrings = print_substrings(s)
print("Substrings sorted by length in reverse:", substrings)
