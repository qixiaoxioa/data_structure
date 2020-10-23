# init 作用
# 1.
# __init__.py的第一个作用就是package的标识，如果没有该文件，该目录就不会认为是package。
# 2.
# __init__.py的另外一个作用就是定义package中的__all__，用来模糊导入，
# 如__init__.py：
#__all__ = ["Pack1Class","Pack1Class1"]
# 3.
# __init__.py首先是一个python文件，所有还可以用来写python模块，
# 但是不建议这么写，尽量保证__init__.py足够轻：

# 辗转相除和更相减损法结合
def get_greatest_commen_division(a,b):
    big = max(a,b)
    small = min(a,b)
    if big % small == 0:
        return small
    return get_greatest_commen_division(a-b,small)
print(get_greatest_commen_division(90,24))


# 荷兰国旗
def sortColors(nums:list):
    a = c = 0
    b = len(nums) - 1
    while c <= b:
        if nums[c] == 0:
            nums[c],nums[a] = nums[a],nums[c]
            a += 1
            c += 1
        elif nums[c] == 2:
            nums[c],nums[b] = nums[b],nums[c]
            b -= 1
        else:
            c += 1


# 最常回文子串
def huiwenshu(nums):
    pass