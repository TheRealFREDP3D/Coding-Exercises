def translation(text: str) -> str:
    vowels = "aeiouy"
    result = []
    i = 0
    
    while i < len(text):
        ch = text[i]
        if ch == " ":
            result.append(" ")
            i += 1
        elif ch in vowels:
            result.append(ch)
            i += 3
        else:
            result.append(ch)
            i += 2
  
    return "".join(result)


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
