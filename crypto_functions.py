def caesar_cipher(original_text, n):
    transform_asc_ii = [ord(i) for i in original_text]

    # E(x) = (x + N)
    cipher_asc_ii = [x + n for x in transform_asc_ii]

    caesar_message = [chr(i) for i in cipher_asc_ii]

    return ''.join(caesar_message)


def caesar_decipher(caesar_text, n):
    transform_asc_ii = [ord(i) for i in caesar_text]

    # E(x) = (x + N)
    original_asc_ii = [x - n for x in transform_asc_ii]

    original_message = [chr(i) for i in original_asc_ii]

    return ''.join(original_message)


def decipher_input(ciphered_input):

    valid_text = None
    max_score = 0
    score = 0

    file = open("words.txt", "r")

    # make sure that any punctuation would not interfere when comparing the decrypted text with the words
    all_words = [word.upper().replace('\n', '') for word in file]

    # cycling through all english alphabet rotations to identify witch rotation makes sense
    for i in range(0, 26):
        decrypted_text = caesar_decipher(ciphered_input, i).upper()

    # cleaning the punctuations on the decrypted text and compare it with the words of txt file.
        for word in decrypted_text.split(' '):
            word_without_punctuation = ''.join(ch for ch in word.upper() if ch not in set(string.punctuation))
            if word_without_punctuation in all_words:
                score += 1

    # if the words are founded, then the decrypted text is saved as the last known possibility and the amount of words founded to.
        if score > max_score:
            max_score = score
            valid_text = decrypted_text

    return valid_text


def vigenere_cipher(input_text, input_keyword):
    alphabet_rotation_letter = {'A': 0, 'a': 0, 'B': 1, 'b': 1, 'C': 2, 'c': 2, 'D': 3,
                                'd': 3, 'E': 4, 'e': 4, 'F': 5, 'f': 5, 'G': 6, 'g': 6, 'H': 7, 'h': 7,
                                'I': 8, 'i': 8, 'J': 9, 'j': 9, 'K': 10, 'k': 10, 'L': 11, 'l': 11, 'M': 12,
                                'm': 12, 'N': 13, 'n': 13, 'O': 14, 'o': 14, 'P': 15, 'p': 15, 'Q': 16,
                                'q': 16, 'R': 17, 'r': 17, 'S': 18, 's': 18, 'T': 19, 't': 19, 'U': 20, 'u': 20,
                                'V': 21, 'v': 21, 'W': 22, 'w': 22, 'X': 23, 'x': 23, 'Y': 24, 'y': 24,
                                'Z': 25, 'z': 25
                                }

    # matching keyword lenght with text lenght
    extended_key = input_keyword * (len(input_text) // len(input_keyword) + 1)
    extended_key_target = extended_key[:len(input_text)]

    # transrform the key string in a list
    extended_key_list = [char for char in extended_key_target]

    # save all rotations based on key position in original alphabet
    rotation_key = []
    for i in range(len(extended_key_list)):
        rotation_key.append(*[alphabet_rotation_letter[extended_key_list[i]]])

    transform_asc_ii = [ord(char) for char in input_text]

    # concatenate each list position, the given key rotation and original letter position.
    cipher_asc_ii = []
    for i in range(len(extended_key_list)):
        cipher_asc_ii.append(rotation_key[i] + transform_asc_ii[i])

    vigenere_cipher = [chr(i) for i in cipher_asc_ii]

    return ''.join(vigenere_cipher)


def vigenere_decipher(encrypted_text, input_keyword):
    alphabet_rotation_letter = {'A': 0, 'a': 0, 'B': 1, 'b': 1, 'C': 2, 'c': 2, 'D': 3,
                                'd': 3, 'E': 4, 'e': 4, 'F': 5, 'f': 5, 'G': 6, 'g': 6, 'H': 7, 'h': 7,
                                'I': 8, 'i': 8, 'J': 9, 'j': 9, 'K': 10, 'k': 10, 'L': 11, 'l': 11, 'M': 12,
                                'm': 12, 'N': 13, 'n': 13, 'O': 14, 'o': 14, 'P': 15, 'p': 15, 'Q': 16,
                                'q': 16, 'R': 17, 'r': 17, 'S': 18, 's': 18, 'T': 19, 't': 19, 'U': 20, 'u': 20,
                                'V': 21, 'v': 21, 'W': 22, 'w': 22, 'X': 23, 'x': 23, 'Y': 24, 'y': 24,
                                'Z': 25, 'z': 25
                                }

    # matching keyword lenght with encrypted text lenght
    extended_key = input_keyword * (len(encrypted_text) // len(input_keyword) + 1)
    extended_key_target = extended_key[:len(encrypted_text)]

    # transform the key string in a list
    extended_key_list = [char for char in extended_key_target]

    # save all rotations based on key position in original alphabet
    rotation_key = []
    for i in range(len(extended_key_list)):
        rotation_key.append(*[alphabet_rotation_letter[extended_key_list[i]]])

    transform_asc_ii = [ord(char) for char in encrypted_text]

    cipher_asc_ii = []
    for i in range(len(extended_key_list)):
        cipher_asc_ii.append(transform_asc_ii[i] - rotation_key[i])

    vigenere_cipher = [chr(i) for i in cipher_asc_ii]

    return ''.join(vigenere_cipher)


def asymmetric_encrypt(original_text, n, e):

    letter_to_ascii = [ord(letter) for letter in original_text]
    cipher_ascii = [pow(ascii_number, e, n) for ascii_number in letter_to_ascii]

    return cipher_ascii

#encrypt is asymmetric_encryp's return
def asymmetric_decrypt(encrypt):

    decipher_asymmetric = [pow(ciphered_number, d, n) for ciphered_number in encrypt]
    original_message = [chr(i) for i in decipher_asymmetric]

    return ''.join(original_message)

def keys_generator():
    import random
    import math

    p = random.getrandbits(10)
    q = random.getrandbits(10)

    while miller_rabin(p, 40) == False and miller_rabin(q, 40) == False:
        p = random.getrandbits(10)
        q = random.getrandbits(10)

    n = p * q

    phi_n = (p - 1) * (q - 1)

    # getting the first number that the greatest common divisor is iqual to 1
    e = random.getrandbits(phi_n)
    
    while math.gcd(e, phi_n) != 1:
        e = random.getrandbits(phi_n)

    d = pow(e, -1, phi_n)
    
    return n, d, e
