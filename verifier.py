import re
import sys


def parsesoltext(soltext: str,n: int) -> list[list[int]]:
    """Given program output, extract a 2-d solution array from the last n lines that have solution-like format."""
    array: list[list[int]] = []
    lines = soltext.splitlines()
    for line in lines:
        rows = re.findall(r'((?:\-?\d+[, ]+){1,}\-?\d+)',line)
        if len(rows)>0:
            row = rows[0]
            elems = re.findall(r'\-?\d+',row)
            array = array + [[int(e) for e in elems]]
    return array[(-n):]

def getsol(soltext: str,parmlist: list[int]) -> list:
    """Extract solution array from raw program output soltext."""
    # utils.parsesoltext will do the work; just need to specify how many rows (how many lines of text) the solution array will have
    m = parmlist[2]
    array = parsesoltext(soltext,m)
    return array 

def v(soltext: str,parmlist: list[int]) -> bool:
    """Verify that the solution in raw program output soltext is a valid solution with parameters in parmlist."""
    n = parmlist[0]
    k = parmlist[1]
    m = parmlist[2]
    C = getsol(soltext,parmlist)

    if len(C)!=m:
        return False
    for i in range(m):
        if len(C[i])!=n:
            return False
        for x in C[i]:
            if x<0 or x>=k:
                return False
        for j in range(i+1,m):
            okflag = False
            for p in range(n):
                if (((C[i][p]-C[j][p])%k)>1) and (((C[j][p]-C[i][p])%k)>1):
                    okflag = True
            if not okflag:
                return False

    return True

x = sys.stdin.read()

m = len(x.splitlines())
array = parsesoltext(x,m)
n = len(array[0])
k = max([max(r) for r in array])+1
print("inferred n " + str(n) + " k " + str(k) + " m " + str(m))

print(str(v(x,[n,k,m])))


