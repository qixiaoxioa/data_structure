from typing import List
def singleNumber(nums:list):
    res = 0
    for i in nums:
        res = res ^ i
    return res