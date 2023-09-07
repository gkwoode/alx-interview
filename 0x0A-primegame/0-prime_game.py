#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
  """
  Determine the winner of the game between Maria and Ben.

  Args:
    x: The number of rounds.
    nums: The array of numbers.

  Returns:
    'Maria' if Maria won the most rounds, 'Ben' if Ben won the most rounds, or
    None if the winner cannot be determined.
  """
  maria_wins = 0
  ben_wins = 0
  for i in range(x):
    # Check if Maria can win the round.
    if canWin(nums):
      maria_wins += 1
    else:
      ben_wins += 1
    # Remove all multiples of the prime number that was chosen.
    nums = [n for n in nums if not isPrime(n)]

  # Return the winner of the most rounds.
  if maria_wins > ben_wins:
    return 'Maria'
  elif ben_wins > maria_wins:
    return 'Ben'
  else:
    return None


def canWin(nums):
  """
  Check if Maria can win the current round.

  Args:
    nums: The array of numbers.

  Returns:
    True if Maria can win, False otherwise.
  """
  for n in nums:
    # If there is a prime number in the set, Maria can win.
    if isPrime(n):
      return True

  # If there are no prime numbers in the set, Ben wins.
  return False


def isPrime(n):
  """
  Check if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True
