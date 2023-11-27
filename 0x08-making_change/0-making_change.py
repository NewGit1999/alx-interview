#!/usr/bin/python3
"""fowest number of coins"""


def makeChange(coins, total):
    """determine the fewest number of coins needed"""
    if total < 0:
        return 0
    if total == 0:
        return 0

    nb = [float('inf')] * (total + 1)
    nb[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                nb[i] = min(nb[i], nb[i - coin] + 1)

    if nb[total] == float('inf'):
        return -1
    else:
        return nb[total]
