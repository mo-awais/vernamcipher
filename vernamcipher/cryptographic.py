__copyright__ = """
Copyright (c) 2022 Mohammed Awais
All Rights Reserved

Author: Mohammed Awais
Email: me@mohammedawais.me
GitHub: https://github.com/mo-awais
Website: https://www.mohammedawais.me/
"""

import secrets
import string
import re


class Cryptographic:
    @staticmethod
    def generate_key(length: int) -> str:
        """
        Uses secret.py to generate a truly random key of a specified length, from an ASCII string of letter and digits.

        Args:
            length (int): required length of key.
        Returns:
            key (str): Truly random key or ASCII alphanumerical characters.
        """

        alpha_numerical = string.ascii_letters + string.digits
        key = ''

        for x in range(length):
            key += secrets.choice(alpha_numerical)

        return key

    @staticmethod
    def exclusive_operations(data: str, key: str) -> str:
        """
        Converts plaintext and key into binary ASCII representation and applies XOR operations.

        Args:
            data (str): string to be encrypted or decrypted.
            key (str): generated or imported ASCII key to apply encryption with.
        Returns:
            ciphertext_string (str): XOR operated ASCII ciphertext.
        """

        if len(key) < len(data):
            raise ValueError("Generated key must be same length to or longer than the plaintext.")

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

        if len(data) > 1:
            for letter_plaintext in data:
                binary_plaintext = f'{ord(letter_plaintext):07b}'

                plaintext_binary.append(binary_plaintext)
        else:
            binary_plaintext = f'{ord(data):07b}'

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
