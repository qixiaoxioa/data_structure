def jiecheng(n):
    if n <= 2:
        return n
    return jiecheng(n-1)*n
print(jiecheng(3))