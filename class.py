import random
import numpy as np

print("random.random() ->", random.random())  # Single [0,1)
print("random.uniform(5,10) ->", random.uniform(5, 10))  # Single [5,10]

print("\nnp.random.rand(2,2):")
print(np.random.rand(2,2))  # 2x2 [0,1)

print("\nnp.random.uniform(100,200,(2,2)):")
print(np.random.uniform(100,200,(2,2)))  # 2x2 [100,200)
find out all