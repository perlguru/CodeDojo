'''
Mastermind kata app
'''

from mastermind.mastermind import Mastermind

def main():
    '''
    Thin layer to exercise Mastermind class

    Totally faked :)
    '''
    print()
    print('A typical session')
    print(['Secret'], ['Guess'], ['Result'])
    cut = Mastermind()
    cut.set_secret(['red', 'blue', 'green'])
    cut.set_guess(['blue', 'green', 'red'])
    result = cut.compare_guess_to_secret()
    print(cut.get_secret(), cut.get_guess(), result)
    cut.set_guess(['red', 'green', 'blue'])
    result = cut.compare_guess_to_secret()
    print(cut.get_secret(), cut.get_guess(), result)
    cut.set_guess(['red', 'blue', 'green'])
    result = cut.compare_guess_to_secret()
    print(cut.get_secret(), cut.get_guess(), result)
    if cut.get_secret() == cut.get_guess():
        print("Solved")

if __name__ == "__main__":
    main()
