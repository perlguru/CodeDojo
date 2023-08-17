'''
Test for Hello, world. kata.
'''

from hello.hello import Hello

class TestHello:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Hello()
        assert isinstance(cut, Hello)

    def test_greeting(self):
        '''
        Intent:
        Test value retrieval.
        '''
        cut = Hello()
        assert cut.greeting() == "Hello, world."

    def test_greet(self, capsys):
        '''
        Intent:
        Test system level output.
        '''
        cut = Hello()
        cut.greet()
        captured = capsys.readouterr()
        assert captured.out == "Hello, world.\n"
