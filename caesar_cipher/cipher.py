import nltk
nltk.download("words", quiet=True)
nltk.download("names", quiet=True)
from nltk.corpus import words, names
import re

def encrypt(plain, shift):
    encrypted = None
    word_list = plain.split()
    for word in word_list:
        encrypted_word = ''
        for char in word:
            if char.islower():
                encrypted_word += get_shifted_char(char, shift, 97)
            elif char.isupper():
                encrypted_word += get_shifted_char(char, shift, 65)
            else:
                encrypted_word += char

        if encrypted:
            encrypted += ' ' + encrypted_word
        else:
            encrypted = encrypted_word

    return encrypted


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)


def crack(cipher):
    count = 26
    while count > 0:
        text = decrypt(cipher, count)
        count -= 1
        word_count = count_words(text)
        percentage = int(word_count / len(text.split()) * 100)

        if percentage > 50:
            return text
    return ''


def count_words(text):
    word_list = words.words()
    name_list = names.words()
    words_to_check = text.split()
    word_count = 0

    for word in words_to_check:
        stripped_word = re.sub(r'[^A-Za-z]+', '', word)
        if stripped_word.lower() in word_list:
            word_count += 1
        else:
            continue

    return word_count


def get_shifted_char(char, shift, casing):
    """
    Takes in a character and returns the shifted version of that character according to the Caesar Cipher
    :param char: char
    :param shift: int
    :param casing: int
    :return: string
    """
    ord_num = ord(char) - casing
    shifted_char = (ord_num + shift) % 26
    return str(chr(shifted_char + casing))

if __name__ == '__main__':
    encryption = encrypt("Hello World", 5)
    decryption = decrypt(encryption, 5)
    cracking = crack(decryption)
    print("encrypted:", encryption)
    print("decrypted:", decryption)
    print("cracked:", cracking)