__copyright__ = """
Copyright (c) 2022 Mohammed Awais
All Rights Reserved

Author: Mohammed Awais
Email: me@mohammedawais.me
GitHub: https://github.com/mo-awais
Website: https://www.mohammedawais.me/
"""

import secrets
import re


class Cryptographic:
    @staticmethod
    def generate_key(length: int) -> str:

        return secrets.token_urlsafe(length)

    @staticmethod
    def plaintext_operations(plaintext: str, key: str) -> str:
        plaintext_binary = []
        key_binary = []
        ciphertext = []
        ciphertext_string = ''

        if len(key) > 1:
            for letter_key in key:
                binary_key = f'{ord(letter_key):07b}'

                key_binary.append(binary_key)
        else:
            binary_key = f'{ord(key):07b}'

            key_binary.append(binary_key)

        if len(plaintext) > 1:
            for letter_plaintext in plaintext:
                binary_plaintext = f'{ord(letter_plaintext):07b}'

                plaintext_binary.append(binary_plaintext)
        else:
            binary_plaintext = f'{ord(plaintext):07b}'

            plaintext_binary.append(binary_plaintext)

        plaintext_binary = ''.join(plaintext_binary)
        key_binary = ''.join(key_binary)

        for index in range(len(plaintext_binary)):
            if plaintext_binary[index] != key_binary[index]:
                ciphertext.append("1")
            else:
                ciphertext.append("0")

        ciphertext = ''.join(ciphertext)
        ciphertext = re.findall('.......', ciphertext)

        for binary_value in ciphertext:
            ascii_int = int(binary_value, 2)
            ascii_character = chr(ascii_int)

            ciphertext_string += ascii_character

        return ciphertext_string
