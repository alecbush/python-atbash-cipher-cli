from . import utils


def cipher(text=''):
    return ''.join(
        cipher_char(char) for char in list(str(text))
    )


def cipher_char(char=' '):
    if not char.isalpha():
        return char
    value = utils.char_value(char)
    offset = utils.decimal_offset(char)
    return chr((25 - value) + offset)
