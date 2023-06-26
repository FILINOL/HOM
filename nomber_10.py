coins = input().split()
n = len(coins)
heads = coins.count('H') 
tails = n - heads 
if heads <= tails:
    print(heads) 
else:
    print(tails) 