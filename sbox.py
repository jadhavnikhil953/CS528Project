#!/bin/python3

import string
import keygen


def substitute_encrypt(message, key):
    key_dict = {key: value for (key, value) in zip(sorted(key), key)}
    encrypted_text = []
    for letter in message:
        encrypted_text.append(key_dict[letter])
    return "".join(encrypted_text)


def substitute_decrypt(message, key):
    key_dict = {key: value for (key, value) in zip(sorted(key), key)}
    decrypted_text = []
    rev_key_dict = {v: k for (k, v) in key_dict.items()}
    for letter in message:
        decrypted_text.append(rev_key_dict[letter])
    return "".join(decrypted_text)


def main():
    key = keygen.keygen("printable", 100)
    print("key = ", key)

    message = (input("Enter a message : "))
    print("message = ", message)
    encrypted_text = substitute_encrypt(message, key)
    print("encrypted text = ", encrypted_text)
    decrypted_text = substitute_decrypt(encrypted_text, key)
    print("decrypted text = ", decrypted_text)


if __name__ == '__main__':
    main()
