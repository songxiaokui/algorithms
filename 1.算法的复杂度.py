# 时间复杂度
# 空间复杂度

# 大O表示法
# O(n)
def calculate_n(n: int):
    result = 0
    for i in range(n+1):
        result += i
    return result


# O(1)
def calculate2_n(n: int):
    return (n * (n + 1)) / 2


# 递归
# 0 1 1 2 3 5 8
def fibonacci(n: int):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(calculate_n(1000))
    print(calculate2_n(1000))
    print(fibonacci(10))
