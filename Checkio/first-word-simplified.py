# You are given a string and you have to find its first word.

def first_word(text: str) -> str:
    """
    Returns the first word of the given text string.
    
    Args:
        text (str): The input text string.
    
    Returns:
        str: The first word of the input text.
    """
    return text.split()[0]
