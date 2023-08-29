'''
Code Cracker kata app
'''

from codecracker.codecracker import Decode, Encode, Key, alphabet

def main():
    '''
    Thin layer to exercise Hello class
    '''
    key = Key()
    key.set_key("".join(alphabet[::-1]))
    message = "Hello, world."
    print("Message: ", message)
    encoded = Encode().encode(key, message)
    print("Encoded: ", encoded)
    decoded = Decode().decode(key, encoded)
    print("Decoded: ", decoded)

if __name__ == "__main__":
    main()
