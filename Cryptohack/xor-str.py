# ============================================================================== #
# xor-starter.py --------------------------------------------------------------- # 
# ============================================================================== #
# Python 3.x.x ----------------------------------------------------------------- #
# Author: Frederick Pellerin --------------------------------------------------- #
# GitHub: https://github.com/TheRealFREDP3D ------------------------------------ #
# Twitter: https://twitter.com/TheRealFredP3D ---------------------------------- #
# ============================================================================== #
# xor_str() -------------------------------------------------------------------- #
# ------------------------------------------------------------------------------ #
# This function takes a string label as input and returns a new string where --- #
# each character of the input string is XORed with the integer 13 -------------- #
# (binary 00001101). The XOR operation is performed on the ASCII values of the - #
# characters. The result is then converted back to a character using the chr --- #
# function and concatenated to the result string. The function finally returns - #
# the result string. ----------------------------------------------------------- # 
# ============================================================================== #
# In simple terms, this function is a form of encryption where each character -- #
# in the input string is 'shifted' by 13 in the ASCII table. The decryption ---- #
# would be the reverse operation, where each character is XORed with 13 again. - #
# ============================================================================== #

def xor_str(label):
    result = ''
    for char in label:
        result += chr(ord(char) ^ 13)
    return result

# ---------------------------------------------------------------------------- #

label = 'label'
flag = xor_str(label)
print(flag)
