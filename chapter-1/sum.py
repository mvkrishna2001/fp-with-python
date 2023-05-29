from typing import List

def sum_of_list(l: List[float]) -> float:
    if len(l) == 0:
        return 0
    return l[0] + sum_of_list(l[1:])
    
def avg(l: List[float]) -> float:
    return sum_of_list(l)/len(l)

print(avg([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]))