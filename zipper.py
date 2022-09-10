from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    res = a.copy()
    for i in range(0, len(a)):
        res.insert(i*2+1, b[i])
        print(res)
    return res


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))