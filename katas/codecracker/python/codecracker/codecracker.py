'''
The Code Cracker kata written in object oriented fashion.
'''

alphabet = list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')

# pylint: disable=too-few-public-methods
class Key():
    '''
    Very simple class to contain our Alphabet and key.
    '''
    key = []

    def set_key(self, keystr):
        '''
        Read the string representation from a file
        '''
        self.key = list(keystr)

        return self.key

# pylint: disable=too-few-public-methods
class Decode():
    '''
    Very simple class to contain our Decode implementation.
    '''

    def decode(self, key, secret):
        '''
        Decode a secrect
        '''
        decrypted = ""
        for letter in secret:
            try:
                nextchar = alphabet[key.key.index(letter)]
            except ValueError:
                nextchar = letter

            decrypted += nextchar

        return decrypted

# pylint: disable=too-few-public-methods
class Encode():
    '''
    Very simple class to contain our Encode implementation.
    '''
    def encode(self, key, message):
        '''
        Encode a message
        '''
        encrypted = ""
        for letter in message:
            try:
                nextchar = key.key[alphabet.index(letter)]
            except ValueError:
                nextchar = letter

            encrypted += nextchar

        return encrypted
