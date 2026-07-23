import sys
from itertools import product


K = 13
A = (
    (1, 0, 0, 0, 11, 12),
    (0, 1, 0, 0, 9, 11),
    (0, 0, 1, 7, 1, 0),
    (0, 0, 0, 0, 1, 0),
)


def mat_vec(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(a*b for a, b in zip(row, x)) % K for row in A)


K = 13
syndromes = {tuple(map(int, line.split())): 0 for line in sys.stdin if line.strip()}
for t in product(range(K), repeat=6):
    if mat_vec(t) in syndromes:
        print(" ".join(map(str,t)))
