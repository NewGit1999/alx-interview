#!/usr/bin/python3
"""who's the winner"""


def isWinner(x, nums):
    """determines the winner of the game"""

    def win_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def the_game(n):
        nbprm = [i for i in range(2, n + 1) if win_prime(i)]
        return len(nbprm) % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        if the_game(nums[i]):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
