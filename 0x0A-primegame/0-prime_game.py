#!/usr/bin/python3
"""
0-prime_game.py
Maria and Ben's prime number game
"""

def sieve(n):
    """Return a list with the number of primes <= i for i in range(n + 1)"""
    is_prime = [False, False] + [True for _ in range(2, n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # prefix sum of number of primes ≤ i
    primes_count = [0] * (n + 1)
    count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            count += 1
        primes_count[i] = count
    return primes_count


def isWinner(x, nums):
    """
    Determines the winner of each round of Prime Game
    Returns: name of the player with the most wins, or None if tie
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_counts = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
