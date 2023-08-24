#!/usr/bin/python3
"""Change come from within"""

def makeChange(coins, total):
  """
    Returns the minimum number of
	coins needed to make change for total.

    Args:
      coins: A list of coin values.
      total: The amount of change to make.

    Returns:
      The minimum number of coins
	needed to make change for total.
      If total is 0 or less, returns 0.
      If total cannot be met by
	any number of coins you have, returns -1.
  """

  if total <= 0:
    return 0

  dp = [float('inf')] * (total + 1)
  dp[0] = 0

  for coin in coins:
    for i in range(coin, total + 1):
      dp[i] = min(dp[i], dp[i - coin] + 1)

  return dp[total] if dp[total] != float('inf') else -1
