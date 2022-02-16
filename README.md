# Updates!

The vernamcipher project is now using truly-random keys. Credit to The Australian National University for their Quantum Random Number Generator (no affiliation).
With this latest update, the vernamcipher package is officially using the strongest encryption methods with truly-random keys.

Please refer below for an in-depth explanation and usage examples.

# What is the Vernam Cipher?

The Vernam Cipher was invented in 1917 by the American scientist Gilbert Vernam. It is the only cipher still proven to be unbreakable.
All other ciphers and encryption methods are based on computational security and integrity, therefore they are theoretically discoverable given enough time, computational power and ciphertext.

# Encryption Process

A **one-time pad** or **key** is used to encrypt plaintext. The one-time pad must be equal to or longer in characters than the plaintext.
In practice, the key must be truly random and used only once. Once for encryption and once for decryption.
Since the key is random, so will be the distribution of the characters meaning that no amount of cryptanalysis will produce any meaningful results.

# Example

As an example, Bob wants to encrypt the letter **M** and send it to Alice. Bob randomly generates a random key which is the same length as the plaintext, in this case **1 character long**.
The plaintext and key are both converted into their ASCII binary representation.

An **XOR** operation is carried out between the binary character value of the first character of the plaintext and the first character of the **one-time pad**.

| Plaintext: M | Key: + | XOR |
|:--:|:--:|:--:|
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |
| 1 | 1 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

As you can see from the table above, the **XOR** operations generate a 7-bit binary value of **1100110**, which corresponds to the letter **f** on the ASCII table.
Alice would then use the ciphertext **f** against the key *+* and follow the same process to decrypt the ciphertext.

# Cryptanalysis and Perfect Security

Ciphers which use computer-generated random keys can be broken since mathematically generated random numbers are not truly random, they only appear to be.
A truly random sequence must be collected from a physical and unpredictable phenomenon such as white noise, the time of a hard disk or radioative decay.
To ensure it is mathematically impossible to break, truly random keys must be used.

# Disclaimer

The truly-random keys are NOT generated on the computer or system being used. They are provided by the ANU QRNG. No computer can generate truly-random values on cryptographically strong.

# Installation
vernamcipher does not require any additional dependencies and can work on a fresh Python install, without any additional requirements.

## Requirements

Python 3.8+
macOS or Linux (Windows not officially supported, but might work)
Working internet connect required to access QRNG when generating keys.

```pip3 install vernamcipher```

# Usage

### Generate a cryptographically-strong, random key

```python
from vernamcipher.cryptographic import Cryptographic

key = Cryptographic.generate_key()
```

### Encrypt

```python
from vernamcipher.cryptographic import Cryptographic

plaintext = "Hello World"
key = Cryptographic.generate_key()

encrypted_data = Cryptographic.exclusive_operations(plaintext, key)
```

### Decrypt

```python
from vernamcipher.cryptographic import Cryptographic

encrypted = "tTuPl"
key = Cryptographic.generate_key()

decrypted_data = Cryptographic.exclusive_operations(encrypted, key)
```