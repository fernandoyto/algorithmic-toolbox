# Uses python3
import sys
from math import inf

def get_change(m):
    possible_coins = [1, 3, 4]

    minimum_coins = [None] * (m + 1)
    minimum_coins[0] = 0

    for m in range(1, m + 1):
        minimum_coins[m] = inf
        for coin in possible_coins:
            if m >= coin:
                total_coins = minimum_coins[m - coin] + 1
                if total_coins < minimum_coins[m]:
                    minimum_coins[m] = total_coins
                
    return minimum_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
