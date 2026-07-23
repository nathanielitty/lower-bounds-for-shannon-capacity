import sys
import itertools

R = [tuple(map(int, line.split())) for line in sys.stdin if line.strip()] # CC(3,11,148)

DL = [(0,0,2),(3,0,2),(1,3,2),(3,2,2)]
DR = [(0,0,2),(3,0,2)]

BL = [x for x in R if x not in DL]
BR = [x for x in R if x not in DR]

X = [((x[0]+1)%11,(x[1]+10)%11,(x[2]+10)%11) for x in R]
Y = [((x[0]+1)%11,(x[1]+1)%11,(x[2]+10)%11) for x in R]

C = [x[0]+x[1] for x in itertools.product(BL,BR)]
for x in X:
    if x in [(1,10,1),(10,0,2)]:
        for z in [(0,1,2),(1,3,2),(2,1,2)]:
            C.append(z + x)
    elif x in [(2,0,4),(4,10,1),(4,10,3),(4,1,1),(4,1,3),(0,0,4)]:
        for z in [(1,0,2),(1,2,2),(3,0,2),(3,2,2)]:
            C.append(z + x)
    elif x in [(2,2,1),(2,2,3),(0,2,1),(0,2,3)]:
        for z in [(1,0,3),(1,3,2),(3,0,2),(3,2,2)]:
            C.append(z + x)
    else:
        for z in DL:
            C.append(z + x)

for y in Y:
    if y in [(1,1,1)]:
        for z in [(1,1,2)]:
            C.append(y + z)
    elif y in [(1,10,2),(2,2,4),(2,0,4),(3,10,2),(4,1,1),(4,1,3),(4,3,1),(4,3,3),(0,2,4),(0,0,4)]:
        for z in [(0,0,2),(2,0,2)]:
            C.append(y + z)
    elif y in [(2,4,1),(2,4,3),(10,2,2),(10,0,2),(0,4,1),(0,4,3)]:
        for z in [(1,0,3),(3,0,2)]:
            C.append(y + z)
    else:
        for z in DR:
            C.append(y + z)
            
for w in C:
    print(" ".join(map(str,w)))
