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
        assert cut.key == list('zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA')

    def test_set_key2(self):
        '''
        Test key generation. Use a extrem string for the seed
        '''
        cut = Key()
        cut.set_key('1234567890!@#$%^&()_+ABCDEFGHIabcdefghiZYXzyxRSTtsr')
        assert cut.key == list('1234567890!@#$%^&()_+ABCDEFGHIabcdefghiZYXzyxRSTtsr')

    def test_encode(self):
        '''
        Test basic encoding with know values
        '''
        key = Key()
        key.set_key("".join(alphabet[::-1]))
        encoder = Encode()
        secret = encoder.encode(key, 'Hello, world.')
        assert secret == 'sVOOL, DLIOW.'

    def test_encode2(self):
        '''
        Test extrem encoding with know values
        '''
        key = Key()
        key.set_key('1234567890!@#$%^&()_+ABCDEFGHIabcdefghiZYXzyxRSTtsr')
        encoder = Encode()
        # pylint: disable=line-too-long
        secret = encoder.encode(key, 'Now is the time for all good men to come to the aide of their country.')
        assert secret == 'FIR (h Z^0 Z(E0 @If 2CC $II8 E0G ZI 6IE0 ZI Z^0 2(80 I@ Z^0(f 6IXGZfs.'

    def test_deeode(self):
        '''
        Test basic decoding with know values
        '''
        key = Key()
        key.set_key("".join(alphabet[::-1]))
        decoder = Decode()
        message = decoder.decode(key, 'sVOOL, DLIOW.')
        assert message == 'Hello, world.'

    def test_deeode2(self):
        '''
        Test extrem decoding with know values
        '''
        key = Key()
        key.set_key('1234567890!@#$%^&()_+ABCDEFGHIabcdefghiZYXzyxRSTtsr')
        decoder = Decode()
        # pylint: disable=line-too-long
        message = decoder.decode(key, 'FIR (h Z^0 Z(E0 @If 2CC $II8 E0G ZI 6IE0 ZI Z^0 2(80 I@ Z^0(f 6IXGZfs.')
        assert message == 'Now is the time for all good men to come to the aide of their country.'
