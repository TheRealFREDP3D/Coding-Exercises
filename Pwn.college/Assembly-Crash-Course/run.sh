# To interact with any level you will send raw bytes over stdin to this pr># To efficiently solve these problems, first run it to see the challenge i># Then craft, assemble, and pipe your bytes to this program.

# For instance, if you write your assembly code in the file asm.S, you can># as -o asm.o asm.S

# Note that if you want to use Intel syntax for x86 (which, of course, you># .intel_syntax noprefix

# Then, you can copy the .text section (your code) to the file asm.bin:    
# objcopy -O binary --only-section=.text asm.o asm.bin

# And finally, send that to the challenge:
# cat ./asm.bin | /challenge/run

# You can even run this as one command:
as -o asm.o asm.S && objcopy -O binary --only-section=.text ./asm.o ./asm.bin && cat ./asm.bin | /challenge/run