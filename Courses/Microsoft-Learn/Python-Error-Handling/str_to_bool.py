# ============================================================================ #
# str_to_bool.py ------------------------------------------------------------- #
# Python 3.x.x --------------------------------------------------------------- #
# Author: Frederick Pellerin ------------------------------------------------- #
# GitHub: https://github.com/TheRealFREDP3D ---------------------------------- #
# Twitter: https://twitter.com/TheRealFredP3D -------------------------------- #
# ============================================================================ #
# str_to_bool() -------------------------------------------------------------- #
# This function takes a string value as input and attempts to convert it ----- #
# into a boolean. ------------------------------------------------------------ #
# ============================================================================ #

true_values = ['yes', 'y']
false_values = ['no', 'n']

def str_to_bool(value):
    
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')
    
# Example usages
print(str_to_bool('y'))
print(str_to_bool('YES'))
print(str_to_bool('n'))
print(str_to_bool('NO'))
print(str_to_bool('maybe'))




