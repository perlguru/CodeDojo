'''
Code Cracker kata app
'''

from codecracker.codecracker import Decode, Encode

def main():
    '''
    Thin layer to exercise Hello class
    '''
    message = Encode("Hello, world.")
    print(message)
    print(Decode(message))

if __name__ == "__main__":
    main()
