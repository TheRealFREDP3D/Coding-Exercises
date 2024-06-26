# -----------------------------------------------------------------------------
# variables
# Definition: named place in memory to store data
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# naming rules
# ------------------------------------------------------------------------------------------------
# 1. start with ['a-z', 'A-Z', '_']
#    CORRECT NAMES: '_correctName', 'correctname', 'Correct_name'
#    BAD NAMES: '0incorrectName', '0Incorrect', '2iNcOrREcT;
#
# 2. case sensitive: 'a != A'
#
# 3. don't use Python reserve words
#    Ex.:  from, and, global, ...
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# CODE
# -------------------------------------------------------------------------------------------------
greeting = 'Hello Friend!'  # variable name = variable value
print('greeting')  # print the word greeting
print(greeting)  # print var. value
greeting = 'Hi, everybody!'  # new value
print(f'{greeting}')  # print new value, f'string
# >>>              greeting
# >>>         Hello Friend!
# >>>        Hi, everybody!
# >>>              greeting
# -------------------------------------------------------------------------------------------------
