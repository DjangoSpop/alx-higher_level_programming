for char_code in range(ord('a'), ord('z') + 1):
    if chr(char_code) != 'q' and chr(char_code) != 'e':
        print(chr(char_code), end='')

# Output:
# abcdfghijklmnoprstuvwxyz
