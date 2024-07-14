# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

# The initial and final markers are always different.
# The initial and final markers are always 1 char size.
# The initial and final markers always exist in a string and go one after another.

def between_markers(text: str, start: str, end: str) -> str:
    """
    Given a string `text`, a starting marker `start`, and an ending marker `end`,
    this function returns the substring enclosed between the two markers.

    Parameters:
        text (str): The input string.
        start (str): The starting marker.
        end (str): The ending marker.

    Returns:
        str: The substring enclosed between the two markers.

    Raises:
        IndexError: If the starting or ending markers are not found in the string.

    Example:
        >>> between_markers("Hello <world>!", "<", ">")
        'world'
    """
    # your code here
    return text.split(start)[1].split(end)[0] 