# You are tasked with writing a function that takes a positive integer, `n`, as an input and returns the number of consecutive equal digits in the number. Specifically, your function should identify pairs of digits in `n` that are equal and consecutive and return the count of these pairs.
#
# For instance, if `n = 113224`, it contains two groups of consecutive equal digits: `11` and `22`. Therefore, the output should be `2`. For `n = 444`, the output should also be `2`, as there are two groups of `44` in this number.
#
# Keep in mind that `n` will be a positive integer ranging from 111 to 10810^8108, inclusive.
#
# Note: You are not permitted to convert the number into a string or any other iterable structure for this task. You should work directly with the number.

# *********************
# YOUR CODE HERE


def solution(n):
    """
    Counts the number of consecutive duplicate digits in the given integer.
    This function analyzes the digits of the input number and returns how many times
    adjacent digits are the same.

    Args:
        n (int): The integer to be analyzed for consecutive duplicate digits.

    Returns:
        int: The count of consecutive duplicate digits found in the input.

    Examples:
        >>> solution(1223)
        1
        >>> solution(455667)
        2
    """

    count = 0
    while n >= 10:
        if n % 10 == n // 10 % 10:
            count += 1
        n = n // 10
    return count


# Example

print(solution(1223))
print(solution(455667))

# *********************
