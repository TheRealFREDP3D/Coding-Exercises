"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40  # The expected bake time in minutes for the lasagna
PREPARATION_TIME = 2     # Preparation time per layer in minutes

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Takes the actual minutes the lasagna has been in the oven as an argument and 
    returns the remaining bake time based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time for the lasagna.
    
    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes) for the lasagna.

    Multiplies the number of layers by PREPARATION_TIME to get the total 
    preparation time required.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total elapsed time for preparing and baking the lasagna.
    
    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Adds the preparation time for the layers and the elapsed bake time 
    to get the total elapsed time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time