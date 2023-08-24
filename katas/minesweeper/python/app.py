'''
Hello World kata app
'''

from hello.hello import Hello

def main():
    '''
    Thin layer to exercise Hello class
    '''
    greeter = Hello()
    greeter.greet()

if __name__ == "__main__":
    main()
