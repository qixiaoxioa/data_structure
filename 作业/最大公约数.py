# 暴力
def max_common_divisor(a,b):
    big = max(a,b)
    small = min(a,b)
    if big % small == 0 :
        return small
    for i in range(small//2,0,-1):
        if big % i ==0 and small % i ==0:
            return i
print(max_common_divisor(20,8))
# 辗转相除法
def get_greatest_common_divisor(a,b):
    big = max(a,b)
    small = min(a,b)
    if big % small == 0 :
        return small
    return get_greatest_common_divisor(small,big % small)
print(get_greatest_common_divisor(90,24))

# 辗转相除法原理

# 更相减损法
def get_greatest_common_divisor1(a,b):
    if a-b==0:
        return a
    big = max(a,b)
    small = min(a,b)
    return get_greatest_common_divisor1(a-b,small)
print(get_greatest_common_divisor(90,24))