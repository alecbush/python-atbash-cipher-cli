def char_value(char):
    return ord(char) - decimal_offset(char)


def decimal_offset(char):
    return ord('A') if char.isupper() else ord('a')
