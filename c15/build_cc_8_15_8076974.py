import sys
import itertools

def conflicts(x,y):
    if max([min((xi-yi)%15,(yi-xi)%15) for xi,yi in zip(x,y)])<=1:
        return True
    else:
        return False

R = [tuple(map(int, line.split())) for line in sys.stdin if line.strip()]

DELETE = [
    (13,0,0,9),   
    (13,14,0,7),  
    (13,13,0,5),  
    (13,14,13,4), 
    (13,14,11,3),
    (13,0,9,3),
    (13,0,7,2),
    (13,0,5,1),
    (14,1,3,1),
    (14,1,1,0),   
    (14,1,0,13),
    (13,0,0,11)]
    


ADD = [
    (13,0,0,8),
    (13,14,0,6),
    (13,14,14,4),
    (13,14,12,3),
    (13,0,10,3),
    (13,0,8,2),
    (13,0,6,1),
    (14,1,4,1),
    (14,1,2,0),
    (14,1,0,14),
    (14,1,0,12),
    (13,0,0,10)]

for x in DELETE:
    R.remove(x)

for x in ADD:
    R.append(x)


Di = [(1,0,14,9),(4,0,8,9),(11,14,1,10),(14,1,0,14)]
Qi = [(1,1,14,9),(3,0,8,9),(11,0,1,10),(14,2,0,14)]

B = [x for x in R if x not in Di]

Ti = []
Ti.append([(x[0],(x[1]-1)%15,x[2],x[3]) for x in R])
Ti.append([((-x[1]+5)%15,(x[0]-1)%15,(-x[2]+7)%15,(-x[3]+3)%15) for x in R])
Ti.append([(x[0],(x[1]-1)%15,x[2],x[3]) for x in R])
Ti.append([(x[0],(x[1]-1)%15,x[2],x[3]) for x in R])

C = list(x[0]+x[1] for x in itertools.product(B,repeat=2))

W0 = [
    [["D","Q","–"],["D","–","Q"],["D","Q","–"],["D","Q","–"]],
    [["D","–","–"],["D","Q","–"],["–","D","–"],["D","–","–"]],
    [["D","Q","–"],["D","–","D"],["D","Q","–"],["D","Q","–"]],
    [["D","Q","–"],["D","–","Q"],["D","Q","–"],["D","Q","–"]],
]

W1 = [
    [["Q","D","–"],["Q","–","Q"],["Q","D","–"],["Q","D","–"]],
    [["Q","–","–"],["Q","D","–"],["–","D","–"],["Q","–","–"]],
    [["Q","D","–"],["D","–","D"],["Q","D","–"],["Q","D","–"]],
    [["Q","D","–"],["Q","–","Q"],["Q","D","–"],["Q","D","–"]]
    ]

for i in range(4):
    for x in Ti[i]:
        for j in range(4):
            if conflicts(x,Di[j]) and conflicts(x,Qi[j]):
                if W0[i][j][2]=="D":
                    C.append(Di[i]+x)
                elif W0[i][j][2]=="Q":
                    C.append(Qi[i]+x)
                # otherwise omit
                break # no further j
            elif conflicts(x,Di[j]):
                if W0[i][j][0]=="D":
                    C.append(Di[i]+x)
                elif W0[i][j][0]=="Q":
                    C.append(Qi[i]+x)
                break
            elif conflicts(x,Qi[j]):
                if W0[i][j][1]=="D":
                    C.append(Di[i]+x)
                elif W0[i][j][1]=="Q":
                    C.append(Qi[i]+x)
                break
            if j==3: # default case if it conflicts with nothing
                C.append(Di[i]+x)

for i in range(4):
    for x in Ti[i]:
        for j in range(4):
            if conflicts(x,Di[j]) and conflicts(x,Qi[j]):
                if W1[i][j][2]=="D":
                    C.append(x+Di[i])
                elif W1[i][j][2]=="Q":
                    C.append(x+Qi[i])
                # otherwise omit
                break # no further j
            elif conflicts(x,Di[j]):
                if W1[i][j][0]=="D":
                    C.append(x+Di[i])
                elif W1[i][j][0]=="Q":
                    C.append(x+Qi[i])
                break
            elif conflicts(x,Qi[j]):
                if W1[i][j][1]=="D":
                    C.append(x+Di[i])
                elif W1[i][j][1]=="Q":
                    C.append(x+Qi[i])
                break
            if j==3: # default case if it conflicts with nothing
                C.append(x+Di[i])
        

for x in C:
    print(" ".join(map(str,x)))
 
