s = input()
result = ''

for ch in s:
    ch = ord(ch) - 65
    ch = ch - 3 + 26
    ch = ch % 26
    ch += 65

    result += chr(ch)

print(result)
