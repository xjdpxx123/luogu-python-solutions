x, n = map(int, input().split())

kilometers = 0

for i in range(n):
    weekday = (x - 1 + i) % 7 + 1
    """
    原编号 1～7
    先减 1，变成 0～6
    做 % 7 循环
    再加 1，变回 1～7
    """

    if weekday <= 5:
        kilometers += 250

print(kilometers)