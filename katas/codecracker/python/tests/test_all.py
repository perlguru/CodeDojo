'''
Test for Code Cracker kata.
'''

from codecracker.codecracker import Decode, Encode, Key, alphabet



class TestCodeCracker:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Decode()
        assert isinstance(cut, Decode)

        cut = Encode()
        assert isinstance(cut, Encode)

    def test_set_key(self):
        '''
        Test key generation. Use a reversed alphabet as the seed
        '''
        cut = Key()
        cut.set_key(alphabet[::-1])
        assert cut.key == list('zyxwvutsrqponmlkjihgfedcba')

    def test_encode(self):
        '''
        Test basic encoding with know values
        '''
        key = Key()
        key.set_key("".join(alphabet[::-1]))
        encoder = Encode()
        secret = encoder.encode(key, 'helloworld')
        assert secret == 'svooldliow'

    def test_deeode(self):
        '''
        Test basic decoding with know values
        '''
        key = Key()
        key.set_key("".join(alphabet[::-1]))
        decoder = Decode()
        message = decoder.decode(key, 'svooldliow')
        assert message == 'helloworld'
