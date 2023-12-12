# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    # >>> is_word(word_list, 'bat') returns
    True
    # >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("../resources/ps4/story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def get_letter_ciphered(letter, shift, is_uppercase):
    ordinal_shift = chr(
        ((ord(letter) - ord('a') + shift) % 26)
        + ord('a')
    )
    if is_uppercase:
        ordinal_shift = chr(
            ((ord(letter) - ord('A') + shift) % 26)
            + ord('A')
        )

    return ordinal_shift

### END HELPER CODE ###

WORDLIST_FILENAME = '../resources/ps4/words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        '''
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        letter_shift_dict = {}
        for letter in 'abcedfghijklmnopqrstuvwxyz':
            letter_shift_dict[letter] = get_letter_ciphered(letter, shift, is_uppercase=False)
            letter_shift_dict[letter.upper()] = get_letter_ciphered(letter.upper(), shift, is_uppercase=True)
        return letter_shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher_shift_dict = self.build_shift_dict(shift)
        cipher_message_text = ''
        for char in self.get_message_text():
            if char in cipher_shift_dict.keys():
                cipher_message_text += cipher_shift_dict[char]
            # Separators ...etc
            else:
                cipher_message_text += char
        return cipher_message_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        super().__init__(text)
        self.encryption_dict = super().build_shift_dict(shift=shift)
        self.message_text_encrypted = super().apply_shift(shift=shift)
        self.text = text
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.message_text_encrypted = super().build_shift_dict(shift=shift)
        self.encryption_dict = super().apply_shift(shift=shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
        self.text = text

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        for word in self.text.split():
            print(f"word {word}")


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    msg = PlaintextMessage('Aaa, bbb', 1)
    print(msg.get_message_text_encrypted())
    # print(msg.get_valid_words())
    # print(msg.apply_shift(1))

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story

    pass #delete this line and replace with your code here


# Kept working on the OOP, while understanding what I truly want which is to be HPMM Tchill I DA, and no ICH maybe just supports me, and fighting the ARtO NoLB/EF/OE 1% Tchill I DA, I'd have already won by just 1% and that's it kh'kh'kh...
