#!/usr/bin/python3
"""Island perimeter computing module.
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_next_prime(start, nums):
        for num in nums:
            if num > start and is_prime(num):
                return num
        return None

    def play_round(nums):
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
