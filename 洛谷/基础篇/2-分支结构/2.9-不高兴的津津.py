max_time = 8
answer = 0

for i in range(7):
    school, mother = map(int, input().split())
    total = school + mother

    if total > max_time:
        max_time = total
        answer = i + 1

print(answer)