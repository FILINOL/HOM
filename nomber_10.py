coins = ["H", "T", "H", "H", "T", "T"]
heads = 0
tails = 0

for coin in coins:
    if coin == "H":
        heads += 1
    else:
        tails += 1

if heads == len(coins) or tails == len(coins):
    flips = 0
else:
    target = "H" if heads > tails else "T"
    flips = sum(coin != target for coin in coins)

print(flips)