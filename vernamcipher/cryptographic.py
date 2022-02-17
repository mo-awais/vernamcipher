__copyright__ = """
Copyright (c) 2022 Mohammed Awais
All Rights Reserved

Author: Mohammed Awais
Email: awais@mohammedawais.me
GitHub: https://github.com/mo-awais
Website: https://www.mohammedawais.me/
"""

import urllib.error
import urllib.request as request
import re


class CryptographicV2:
    @staticmethod
    def generate_key() -> str:
        """
        Uses the Quantum Random Number Generator (QRNG), provided by the Australian National University. The QRNG uses
        sophisticated quantum physics to generate truly-random alpahnumeric strings.

        The QRNG only generates a 1024-block. All plaintext must be 1024 blocks.

        Returns:
            key (str): Truly random key or ASCII alphanumerical characters.
        """

        try:
            key_request = request.urlopen("https://qrng.anu.edu.au/wp-content/plugins/colours-plugin/get_block_alpha.php")
            key = key_request.readline().decode()

            while not key.isalnum():
                key = key.replace("_", "")

            return key
        except (urllib.error.URLError, urllib.error.HTTPError, urllib.error.ContentTooShortError) as error:
            return error

    @staticmethod
    def exclusive_operations(data: str, key: str) -> str:
        """
        Converts plaintext and key into binary ASCII representation and applies XOR operations.

        Args:
            data (str): string to be encrypted or decrypted.
            key (str): generated or imported truly-random key to apply encryption with.
        Returns:
            ciphertext_string (str): XOR operated ASCII ciphertext.
        """

        if len(key) < len(data):
            raise ValueError("Generated key must be same length to or longer than the plaintext.")

        plaintext_binary = []
        key_binary = []
        ciphertext = []
        ciphertext_string = ''

        for letter_key in key:
            binary_key = f'{ord(letter_key):07b}'

            key_binary.append(binary_key)

        for letter_plaintext in data:
            binary_plaintext = f'{ord(letter_plaintext):07b}'

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
