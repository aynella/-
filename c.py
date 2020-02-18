import math
n=float(input())
if math.ceil(n)-n<=0.5:
    print(math.ceil(n))
else:
    print(math.ceil(n)-1)
