import random
import math


def game(A: list[int]) -> int:  # tuple[int, list[int]]:
    res = 0
    steps = []
    pos = 0
    end = len(A) - 1
    if end < 1:
        return (0, [])

    steps += [A[pos]]
    while pos != end:
        die = (math.floor(random.random() * 10) % 6) + 1
        if (pos + die) <= end:
            pos += die
            steps += [A[pos]]

    for x in steps:
        res += x

    return res  # , steps)


RANGE = 6


def solution(A):

    # Boolshit,
    # Make dynamic programming array
    # which calculats the min value for reaching the specific place.
    pass


def main():
    print("Start main()")

    test_cases = [
        # Empty board
        ([], 0),
        # Single element board
        ([1], 1),
        # Two elements board
        ([100, 50], 150),
        # Board with all zeros
        ([0] * 10, 0),
        # Example case
        ([1, -2, 0, 9, -1, -2], 8),
        # Small board with positive and negative numbers
        ([10, -5, 2, 1, -8], 5),
        # Board with consecutive numbers (no valid moves)
        ([1, 2, 3, 4, 5], 15),
        # Board with all negative numbers
        ([-5, -2, -7, -1, -9], -15),
        # Board with all positive numbers
        ([8, 3, 6, 1, 2], 20),
        # Larger board with mixed values
        ([-2, 9, 5, -4, 1, 2, -3, 6, 8, -1], 28),
        # Board with negative values near the end
        ([10, 10, 10, -10000, -10000], -9970),
        # Test case 4: Mix of positive and negative numbers, the result depends on the dice roll
        ([10, -5, 7, -8, 6], 23),
        # Test case 1: List of 13 elements, mix of positive and negative numbers
        ([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13], 49),
        # Test case 3: List of 20 elements, alternating between a large positive and negative number
        ([10000, -10000] * 10, 90000),
        # Test case 7: List of 30 elements, alternating between three numbers
        ([1, -1, 0] * 10, 10),
        # Test case 8: List of 14 elements, all the same negative number
        ([-5] * 14, -20),
        # Test case 9: List of 16 elements, alternating between four numbers
        ([1, -1, 2, -2] * 4, 10),
        # Test case 10: List of 17 elements, mix of positive and negative numbers
        ([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17], 81),
        # Test case: List of 20 elements, sequence of more than six negative numbers followed by positive numbers
        ([-5, -4, -3, -2, -1, -6, -7, -8, -9, -10, 1, 2, 3, 4], 4),
        # Test case: List of 20 elements, sequence of more than six negative numbers followed by positive numbers
        (
            [
                -5,
                -4,
                -3,
                -2,
                -1,
                -6,
                -7,
                -8,
                -9,
                -10,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                -1,
                -2,
                -3,
                -4,
                -5,
                -6,
                -7,
                -8,
                -9,
                -10,
            ],
            31,
        ),
        # Real Test case ...
        ([-5, -4, -3, -2, -1, -6, -7, -8, -9, -10, -10, -2, 10, 4], 0),  # should be 2
        # TBD ...
        ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, 14, 15], 0)
        # TBD ...
        ([0, -1, -10, -1, -10, -10, -10, -1, -10, -10, -10, -10, -10, 2, 10, 0], 0),
    ]

    for i in test_cases:
        print(i[0], solution(i[0]), i[1])
        # print(i, game(i))


if __name__ == "__main__":
    main()
