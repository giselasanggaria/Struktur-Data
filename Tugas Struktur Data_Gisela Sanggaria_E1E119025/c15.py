from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data1 = [1, 4, 8, 9, 5]
data2 = [1, 10, 7, 2, 5, 7]

print(areDistinct(data1))
print(areDistinct(data2))
