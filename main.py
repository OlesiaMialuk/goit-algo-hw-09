def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            change[coin] = num_coins
            amount -= num_coins * coin
    return change

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_coin = [0] * (amount + 1)

    for coin in coins:
        for j in range(coin, amount + 1):
            if min_coins[j - coin] + 1 < min_coins[j]:
                min_coins[j] = min_coins[j - coin] + 1
                last_coin[j] = coin

    result = {}
    while amount > 0:
        result[last_coin[amount]] = result.get(last_coin[amount], 0) + 1
        amount -= last_coin[amount]

    return result
# Жадібний алгоритм
print("Жадібний алгоритм:")
print(find_coins_greedy(113))

# Алгоритм динамічного програмування
print("Динамічне програмування:")
print(find_min_coins(113))
