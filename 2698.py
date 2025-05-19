k = 18

def dsum(k):
    total = sum(int(i) for i in str(k))  # Sum of digits
    return total if total < 10 else dsum(total)  # Recursively reduce

print(dsum(k))

  