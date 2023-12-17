# Encrypt each letter of the text and save the next letter
import random


def get_words(self):
    word_list = []
    with open("words.txt") as fh:
        word_list = fh.read().split()
    return word_list

class SubMessage:
    def __init__(self, text):
        self.text = text
        self.valid_words = get_words()

    def get_valid_words(self):
        return self.valid_words

    def build_transpose_dict(self, vowels_permutation):
        encryption_dict = {}
        alphabet_list = 'abcdefijklmnopqrstuvwxyz'.split()
        for vowel in 'aeiou':
            random_letter = alphabet_list.pop(random.randint(0, 25))
            encryption_dict[vowel] = random_letter
            encryption_dict[vowel.upper()] =  random_letter.upper()

        return encryption_dict

    def apply_transpose(self):
        encryption_dict = self.build_encryption_dict()
        encrypted_text = ''
        for letter in self.text:
            if letter in encryption_dict.keys():
                encrypted_text += letter
            else:
                encrypted_text += encryption_dict[letter]
        return encrypted_text


if __name__ == "__main__":
    print("adf")
