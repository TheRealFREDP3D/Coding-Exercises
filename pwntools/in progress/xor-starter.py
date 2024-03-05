from pwn import xor
target = "label"
xor_key = 13

target_unicode = target.encode('utf-8')
print(target_unicode) 

# XOR each character with the integer 13. Convert these integers back to a string
result = xor(target_unicode ^ xor_key).decode('utf-8')
print("result")
