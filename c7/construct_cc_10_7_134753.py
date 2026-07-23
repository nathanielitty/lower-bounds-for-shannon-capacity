import sys
import itertools

def conflicts(x,P):
 for y in P:
  if max([min((xi-yi)%7,(yi-xi)%7) for xi,yi in zip(x,y)])<=1:
   return True
 return False
  

R = {tuple(map(int, line.split())): 0 for line in sys.stdin if line.strip()}

PAIRS = (
 ((1,3,4,4,6),(2,3,5,4,6)),
 ((3,4,0,3,5),(2,4,6,3,5)),
 ((5,3,1,3,4),(5,3,2,3,5)),
 ((4,4,6,1,6),(5,4,6,0,6)),
 ((6,0,6,4,5),(6,1,6,5,5)),
 ((0,3,5,6,5),(6,3,5,0,5)),
 ((6,4,3,4,0),(6,4,2,4,6)),
 ((6,4,5,3,2),(6,5,5,3,1)),
)

deleted = {r for r,_ in PAIRS}
B = tuple(w for w in R if w not in deleted)

X = [((2-w[1])%7,w[3],w[0],(2-w[2])%7,w[4]) for w in R]
print(str(X[267]))
X[267] = (1,5,6,3,5)

J0 = [0,5,6]
J1 = [1,2,3,4,7]

PH = [PAIRS[j][0] for j in J0] + [PAIRS[j][1] for j in J1]
PV = [PAIRS[j][1] for j in J0] + [PAIRS[j][0] for j in J1]

A = [x for x in X if conflicts(x,PV)]
D = [x for x in X if conflicts(x,PH)]

C = list(x[0]+x[1] for x in itertools.product(B,repeat=2))
for x in X:
 for j in range(8):
   C.append(x + PAIRS[j][((j in J0) and (x in A)) or ((j in J1) and (x in D))])
   C.append(PAIRS[j][((j in J0) and (x in D)) or ((j in J1) and (x in A))] + x)

for x in C:
 print(" ".join(map(str,x)))
 

     
