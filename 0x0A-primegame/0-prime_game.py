#!/usr/bin/python3
"""Island perimeter computing module.
"""


def isWinner(x, nums):
    """
    Determine the winner of a prime number removal game for multiple rounds.

    Args:
    - x (int): Number of rounds.
    - nums (list): List of integers representing the sets for each round.

    Returns:
    - str: Name of the player that won the most rounds.
           If the winner cannot be determined, returns None.

    Notes:
    - Assumes Maria always goes first and both players play optimally.
    - Rounds are played by choosing prime numbers and removing them and their multiples.

    Constraints:
    - n and x will not be larger than 10000.
    - Do not import any packages.

    Example:
    >>> x = 3
    >>> nums = [4, 5, 1]
    >>> isWinner(x, nums)
    'Ben'
    """

    def is_prime(num):
        """
        Check if a number is prime.

        Args:
        - num (int): Number to check.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_next_prime(start, nums):
        """
        Find the next prime number in a list.

        Args:
        - start (int): Number to start searching from.
        - nums (list): List of numbers to search.

        Returns:
        - int: Next prime number in the list, or None if not found.
        """
        for num in nums:
            if num > start and is_prime(num):
                return num
        return None

    def play_round(nums):
        """
        Simulate a round of the prime number removal game.

        Args:
        - nums (list): List of numbers to play the round with.

        Returns:
        - str: Name of the winner of the round ('Maria' or 'Ben').
        """
        maria_turn = True
        while True:
            prime = find_next_prime(1 if maria_turn else 2, nums)
            if prime is None:
                return "Ben" if maria_turn else "Maria"
            nums = [num for num in nums if num % prime != 0]
            maria_turn = not maria_turn

    wins_count = {"Maria": 0, "Ben": 0}
    for num in nums:
        winner = play_round(list(range(1, num + 1)))
        wins_count[winner] += 1

    if wins_count["Maria"] > wins_count["Ben"]:
        return "Maria"
    elif wins_count["Ben"] > wins_count["Maria"]:
        return "Ben"
    else:
        return None
