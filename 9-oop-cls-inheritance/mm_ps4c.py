# Encrypt each letter of the text and save the next letter
import random
import re


def get_words():
    # word_list = []
    with open("words.txt") as fh:
        word_list = fh.read().split()
    return word_list

class SubMessage:
    def __init__(self, text):
        self.text = text
        self.valid_words = get_words()

    def get_message_text(self):
        return self.text

    def get_valid_words(self):
        return self.valid_words

    def set_message_text(self, text):
        self.text = text

    def build_transpose_dict(self, vowels_permutation):
        vowels = ['a', 'e', 'i', 'o', 'u']
        encryption_dict = {}
        for i in range(5):
            vowel = vowels[i]
            encryption_dict[vowel] = vowels_permutation[i]
            encryption_dict[vowel.upper()] = vowels_permutation[i].upper()

        return encryption_dict

    def apply_transpose(self, encryption_dict):
        encrypted_text = ''
        for letter in self.text:
            if letter in encryption_dict.keys():
                encrypted_text += encryption_dict[letter]
            else:
                encrypted_text += letter
        return encrypted_text


def get_permutations(word):
    permutations = []
    if len(word) == 1:
        return [word]

    first_letter = word[0]
    subword = word[1:]
    subword_permutations = get_permutations(subword)
    for subword_permutation in subword_permutations:
        permutations.append(first_letter+subword_permutation)
        for i in range(1, len(subword_permutation)+1):
            permutations.append(subword_permutation[:i]+first_letter+subword_permutation[i:])
    return permutations


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        self.text = text
        super().__init__(text)

    def decrypt_message(self):
        max_valid_words = 0
        # decrypted_texts = []
        vowel_permutations = get_permutations('aeoiu')
        # print(f"vowel_permutations {vowel_permutations}")
        for vowel_permutation in vowel_permutations:
            nb_valid_words = 0
            transposed_text = self.apply_transpose(self.build_transpose_dict(vowel_permutation))
            # print(f"transposed_text {transposed_text}")
            for word in re.findall('(\w+)', transposed_text):
                if word.lower() in self.get_valid_words():
                    nb_valid_words += 1
            if nb_valid_words > max_valid_words:
                max_valid_words = nb_valid_words
                decrypted_text = transposed_text
        return decrypted_text
                # decrypted_texts = [(vowel_permutation, transposed_text)]
            # elif nb_valid_words == max_valid_words:
                # decrypted_texts.append((vowel_permutation, transposed_text))

        # return decrypted_texts






if __name__ == "__main__":
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())