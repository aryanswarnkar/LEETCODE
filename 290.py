# false when characters will not match words
# splitiing the string str
# two hashmaps
# aba   cat cat cat
# a-> cat   cat -> a
# b-> cat   cat-> b assigned to differet char thereforfalse.
# c->
# 0(n+m)
# words=s.split(" ")
# if len(pattern)!=len(words):
#     return False
# char={}
# wordtochar={}
# for c,w in zip(pattern,words):
#     if c in char and char[c]!=w:
#         return False
#     if w in wordtochar and wordtochar[w]!=c:
#         return False

#     char[c]=w
#     wordtochar[w]=c
# return True    
def greet(name="Guest"):
    if name == "Guest":
        print("Hello Welcome")
    else:
        print(f"Hello,{name}! Welcome")

greet("ooops")

greet()
