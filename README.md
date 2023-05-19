# CS528Project

## Introduction
Encryption techniques come in various forms, ranging from simple Caesar ciphers to advanced algorithms like AES. This project explores three fundamental techniques used in encryption: Substitution cipher, Transposition cipher (also known as Permutation cipher), and bitwise XORing. When Substitution cipher and Transposition cipher are combined, they form a Substitution-Permutation Network (SPN). The SPN technique is widely used in popular encryption algorithms such as AES, 3-Way, Kalyna, Kuznyechik, PRESENT, SAFER, SHARK, and Square.

## Concepts Used in the Project

### A. Substitution Cipher
The Substitution cipher operates on the principle of substituting one character with another. For example, the letter 'A' can be substituted with 't' or the digit '4' can replace 'd'. To keep track of the substitutions, a mapping is used. This mapping is essentially a string with randomly arranged character values, corresponding to their respective indices arranged in a specific order. The key characteristic of this cipher is that it maintains the length of the message without adding any redundancy.

### B. Permutation Cipher
Also known as the Transposition cipher, the Permutation cipher works by constructing a matrix of characters, taking its transpose, and then dismantling it to obtain the ciphertext. The number of columns in the matrix serves as the encryption key. It's important to note that the length of the message is typically not an exact multiple of the rows and columns, resulting in some empty spaces. These spaces are filled with random ASCII characters, introducing redundancy in the ciphertext. The formula to calculate the number of extra characters added is: `extra_characters_added = rows * columns - length_of_message`.

### C. Key Transformation
The algorithm utilizes two keys: k0 and k1. Initially, k0 is not directly used in encryption. The data is encrypted once using k1. Then, k0 is used to encrypt k1, resulting in k2. This key transformation is achieved through a substitution cipher. The key remains the same length as before, and no redundant data is introduced. Similarly, k3 is obtained by encrypting k2 with k1. This technique is called cipher block-chaining, where the encrypted data is used to re-encrypt the next block of data. While XOR operations are commonly used for this purpose, the substitution cipher approach is also feasible. This process generates a list of kn keys that can be used to encrypt the data multiple times. The initial key for the entire algorithm is obtained by concatenating k0 and k1.

### The SP-Network Implementation
The algorithm consists of two sub-stages. In the first sub-stage, the input text is passed through the p-box (Permutation cipher). The output of the p-box is then used as input for the s-box (Substitution cipher). These two sub-stages form a single stage of the algorithm. The number of stages is determined by the user input (n).
The process of plain_text → p-box → s-box → encrypted_text is repeated n times.
In the p-box, prime numbers are used as keys for each stage. For example, the first stage uses 2, the second stage uses 3, and the third stage uses 5. This is done as a defense mechanism against analyzing repeating character sequences. Sufficient repetitions provide a significant level of defense, as a substantial number of prime factors are already exhausted, making analysis based on that factor difficult.
Fig.1 – Code Snippet for Permutation/Transposition Cipher

In the s-box, each stage uses a different key computed earlier, such as k1, k2, k3, and so on. The algorithm employs a 

100-character key, selecting characters from all printable ASCII characters. Consequently, a character can be transformed into any of the 100 ASCII characters. Decryption is performed by reversing this process.
