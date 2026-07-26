n = int(input())

numbers = input().split()

while len(numbers) != n:
    print("输入数量不正确，请重新输入")
    numbers = input().split()

for i in range(n):
    numbers[i] = int(numbers[i])

min_value = 1001

for i in range(n):
    if numbers[i] < min_value:
        min_value = numbers[i]

print(min_value)