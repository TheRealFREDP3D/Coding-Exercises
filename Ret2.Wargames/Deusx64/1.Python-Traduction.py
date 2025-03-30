# This function emulates the test assembly code.


def test(arg_1, arg_2):
    """It takes two integer arguments, performs a series of arithmetic operations based on the assembly instructions, and returns True if the final final_value is 31337, False otherwise.


    push rdi
    push rsi
    pop rdi
    pop rsi

    instructions
    swaps the values in the registers. (Last In / First Out)

    arg_1 contains the original value of arg_2
    arg_2 contains the original value of arg_1
    """
    final_value = 0  # Initialize rax
    final_value = arg_2  # mov rax, rsi (now arg_2)
    final_value = final_value + arg_2  # add rax, rsi (now arg_2)
    final_value = final_value + 1024  # add rax, $1024
    arg_1 = arg_1 - 256  # sub rdi, $256 (now arg_1)
    final_value = final_value + arg_1  # add rax, rdi (now arg_1)

    if final_value == 31337:
        return True
    else:
        return False


arg_1 = int(input("Arg. 1: "))
arg_2 = int(input("Arg. 2: "))

print(test(arg_1, arg_2))
