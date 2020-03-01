def cipher_text(text=''):
    return ''.join(
        _cipher_char(char) for char in list(str(text))
    )


def _cipher_char(char=' '):
    if not char.isalpha():
        return char
    return chr((25 - _char_value(char)) + _decimal_offset(char))


def _char_value(char):
    return ord(char) - _decimal_offset(char)


def _decimal_offset(char):
    return ord('A') if char.isupper() else ord('a')
