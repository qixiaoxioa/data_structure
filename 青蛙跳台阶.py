# 青蛙跳台阶,一次跳一层或两层,跳n层总共有多少种跳法
def frog_drump(n):
    if n <= 2:
        return n
    return frog_drump(n-1)+frog_drump(n-2)
print(frog_drump(3))