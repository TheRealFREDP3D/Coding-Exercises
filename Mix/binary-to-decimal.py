def binary_to_decimal(binary_string: str):
    """
    Convert a binary string to a decimal number.

    Parameters
    ----------
    binary_string : str
        A string of 0s and 1s representing the binary number

    Returns
    -------
    int
        The decimal equivalent of the binary number
    """
    if not isinstance(binary_string, str):
        raise TypeError("Input must be a string")
    if not binary_string:
        raise ValueError("Input string is empty")

    decimal_number = 0
    power = 0

    for digit in reversed(binary_string):
        decimal_number += 2**power
        power += 1
    return decimal_number


binary_string = input('Enter a binary number:\n')
print(f'''
    Converting to decimal...
    {binary_to_decimal(binary_string)}
    '''
)

# Example
# *******
# binary_string = "10011000" 
# Output: 152