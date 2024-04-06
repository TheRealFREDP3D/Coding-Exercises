# -----------------------------------------------------------------------------
# more print
# -----------------------------------------------------------------------------
# a commentary                  # not executed by Python interpreter
print('Hello')                  # 'string' = "string" = `string`
# >>>    Hello
# -----------------------------------------------------------------------------
# print('I'm studying Python')  # BAD = {'''} 3X same character    
print("I'm studying Python")    # OK = [ "'" ], [ '"' ], [ `'` ], [ `"` ] ... 
print()                         # print() = print("\n") = "new line" = [ENTER]
print('I\'m studying Python')   # escape with \
# >>> I'm studying Python
# >>>
# >>> I'm studying Python
# -----------------------------------------------------------------------------
msg1 = 'Hello'                  # msg1: variable, 'Hello': string
msg2 = 'World!'                 # msg2: another variable, 'World!' string
# empty line are not printed

# -----------------------------------------------------------------------------
print(msg1+' '+msg2)            # concatenate two strings:
# >>>   Hello World!            # variable1.value+'[SPACE]'+variable2.value
print(f'{msg1} {msg2}')         # f'string
# >>>   Hello World!            # Same result
# -----------------------------------------------------------------------------
