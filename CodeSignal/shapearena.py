# Challenge

# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side.

# ------------------------------------------------------------------

# Example

# For n = 2, the output should be
# solution(n) = 5;
# For n = 3, the output should be
# solution(n) = 13.

# ------------------------------------------------------------------

# Solution

def solution(n):
/*************  ✨ Codeium Command ⭐  *************/
    """
    Calculate the area of a polygon for a given n.

    An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side.

    Parameters
    ----------
    n : int
        The number of sides of the polygon.

    Returns
    -------
    area : int
        The area of the n-interesting polygon.

    Examples
    --------
    >>> solution(1)
    1
    >>> solution(2)
    5
    >>> solution(3)
    13
    """

def solution(n):
    return (n - 1) * (n - 1) + 1    # (n - 1)^2 + 1
