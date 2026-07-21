n = int(input())

price_total = 10**100  # 先设成一个很大的数

for i in range(3):
    num, price = map(int, input().split())

    # 购买这种包装需要花的钱
    current_price = (n + num - 1) // num * price

    # 保留目前最小的花费
    if current_price < price_total:
        price_total = current_price

print(price_total)