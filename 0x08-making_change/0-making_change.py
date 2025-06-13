#!/usr/bin/python3
"""
Module to solve the coin change problem
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    Args:
        coins (list): list of the values of the coins
        total (int): total amount to make change for
    Returns:
        int: minimum number of coins to make the change, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Initialize DP array with total + 1 (an impossible large value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
