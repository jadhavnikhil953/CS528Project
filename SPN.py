#!/bin/python3

import sbox
import pbox
import keygen
import fileinput



def encrypt(plain_text, key, prime, stage):
    print("plain text = ", plain_text)
    encryptedecrypted_text_1 = pbox.encrypt(plain_text, prime)
    encryptedecrypted_text_2 = sbox.substitute_encrypt(encryptedecrypted_text_1, key)
    return encryptedecrypted_text_2


def decrypt(plain_text, cipher_text, key, prime, stage):
    decrypted_text_2 = sbox.substitute_decrypt(cipher_text, key)
    padding = pbox.padding(plain_text, prime)
    decrypted_text_1 = pbox.decrypt(decrypted_text_2, prime, padding)
    return decrypted_text_1


def main():
    key_list = []
    key = keygen.generate_final_key()
    key_list.append(key[:100])
    key_list.append(key[100:])

    stages = int(input("how many stages? > "))
    for i in range(stages):
        key_list.append(sbox.substitute_encrypt(key_list[i+1], key_list[1]))

    primes = keygen.list_primes(stages)
    print("key = ", key)
    print("primes = ", primes)
    print("\n========================================\n")
    
    input_text1 = ""
    for line in fileinput.input(files ='input.txt'):
        input_text1 = input_text1 + line
    print(input_text1)
    
    cipher_text = []
    cipher_text.append(input_text1)
    print(cipher_text)
    print("\n--- Encryption ---")
    for i in range(stages):
        cipher_text.append(encrypt(cipher_text[i], key_list[i+1], primes[i], i+1))
        print(f"After stage {i+1} encryption = ", cipher_text[i+1])

    print("\n========================================\n")

    decrypted_text = []
    decrypted_text.insert(0, cipher_text[-1])
    print("--- Decryption ---")
    print("text to be decrypted = ", decrypted_text[0])

    for i in range(stages, 0, -1):
        decrypted_text.insert(0, decrypt(cipher_text[i-1], cipher_text[i], key_list[i], primes[i-1], i))
        print(f"After stage {i} decryption = ", decrypted_text[0])
        if i == 1:
            f = open("output.txt","w+")
            f.write(decrypted_text[0])
            f.close()


if __name__ == '__main__':
    main()
