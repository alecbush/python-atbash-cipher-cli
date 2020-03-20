def cipher(text=''):
    return ''.join(
        cipher_char(char) for char in list(str(text))
    )


def cipher_char(char=' '):
    if not char.isalpha():
        return char
    offset = ord('A') if char.isupper() else ord('a')
    value = ord(char) - offset
    return chr((25 - value) + offset)
