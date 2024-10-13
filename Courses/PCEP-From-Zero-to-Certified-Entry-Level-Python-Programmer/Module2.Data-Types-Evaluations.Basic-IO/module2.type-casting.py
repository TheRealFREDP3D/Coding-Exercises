# -----------------------------------------------------------------------------
# type casting
#
# Definition: 
# Changing between data types (E.g. strings to floats) is called 'type casting' 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# height_cm = input('Height converter: Enter height in cm: ')
# print('Your height in feet is:', height_cm / 30.48 )

# Error
# >>> TypeError: unsupported operand type(s) for /: 'str' and 'float'

# input() function return a 'string'
# can't divide a 'string' by a 'float'
# -----------------------------------------------------------------------------

# float()
# try to convert a string to a float
# Ex. float(height_cm)

# height_cm = input('Height converter: Enter height in cm: ')
# float_height = float(height_cm)
# #print('Your height in feet is:', float_height / 30.48 )

# >>> Height converter: Enter height in cm: 56
# >>> Your height in feet is: 1.837270341207349

# -----------------------------------------------------------------------------
# Function as another function argument

float_height = float(input('Height converter: Enter height in cm: '))
print('Your height in feet is:', float_height / 30.48 )

# >>> Height converter: Enter height in cm: 56
# >>> Your height in feet is: 1.837270341207349
# -----------------------------------------------------------------------------

# float() - Convert to a 'float'
# int() - Convert to 'integer'
# str() - Convert a 'int' or 'float' to 'string' 

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++